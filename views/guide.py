# views/guide.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data


class Guide(State):
    def __init__(self):
        super().__init__("guide")
        self.images = []
        self.index = 0
        self.bg = None
        self.surface = None
        self.font = pygame.font.Font(None, 64)

        # Buttons
        self.next_btn = Button(1400, 950, assets.next_btn_img, 1.0, click_sound=assets.click_sfx)
        self.back_btn = Button(1150, 950, assets.back_btn_img, 1.0, click_sound=assets.back_sfx)
        self.emergency_btn = Button(875, 947, assets.emergency_call_btn_img, 1.0, click_sound=assets.click_sfx)
        self.main_btn = Button(820, 965, assets.main_menu_btn_img, 1.0, click_sound=assets.back_sfx)
        self.emergency_main_btn = Button(1135, 950, assets.emergenccy_menu_btn_img, 1.0, click_sound=assets.back_sfx)

        self.triggered_solenoid = False

    def on_enter(self):
        """Load correct images for selected injury."""
        injury = self.manager.current_injury
        data = guide_data[injury]
        self.images = [pygame.image.load(img).convert() for img in data["images"]]
        self.index = 0
        self.triggered_solenoid = False

    def handle_events(self, events):
        if not self.surface:
            return None

        first_page = self.index == 0
        last_page = self.index == len(self.images) - 1

        if not last_page and self.next_btn.draw(self.surface):
            self.index += 1
        if self.index > 0 and self.back_btn.draw(self.surface):
            self.index -= 1

        # first page → emergency menu button
        if first_page and self.emergency_main_btn.draw(self.surface):
            return "emergency_menu"

        # show emergency button only after page 1
        if not first_page and self.manager.mode == "emergency" and self.emergency_btn.draw(self.surface):
            print("[ALERT] Sending emergency SMS...")

        if last_page and self.main_btn.draw(self.surface):
            return "main_menu"

    def update(self, dt):
        # Trigger solenoid only once at first page if in emergency mode
        if self.manager.mode == "emergency" and not self.triggered_solenoid:
            print(f"[HARDWARE] Unlocking drawer for: {self.manager.current_injury}")
            # trigger_solenoid(self.manager.current_injury)  # placeholder
            self.triggered_solenoid = True

    def draw(self, surface):
        self.surface = surface
        if self.images:
            surface.blit(self.images[self.index], (0, 0))

        # --- Button visibility logic ---
        last_page = self.index == len(self.images) - 1
        first_page = self.index == 0

        if last_page:
            # last page -> only main menu
            self.main_btn.draw(surface)
        else:
            # show navigation
            if self.index > 0:
                self.back_btn.draw(surface)
            self.next_btn.draw(surface)

            # first page → show "Emergency Menu" button instead of emergency
            if first_page:
                self.emergency_main_btn.draw(surface)
            else:
                # show emergency button only after first page
                if self.manager.mode == "emergency":
                    self.emergency_btn.draw(surface)