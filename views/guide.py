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
        self.next_btn = Button(1400, 900, assets.next_btn_img, 1.0, click_sound=assets.click_sfx)
        self.back_btn = Button(300, 900, assets.back_btn_img, 1.0, click_sound=assets.back_sfx)
        self.emergency_btn = Button(850, 900, assets.emergency_btn_img, 1.0, click_sound=assets.click_sfx)
        self.main_btn = Button(820, 900, assets.main_btn_img, 1.0, click_sound=assets.back_sfx)

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

        # Draw buttons and check actions
        if self.index < len(self.images) - 1:
            if self.next_btn.draw(self.surface):
                self.index += 1
        if self.index > 0:
            if self.back_btn.draw(self.surface):
                self.index -= 1
        if self.index == 0:
            # Emergency available throughout, only disabled in learning mode
            if self.emergency_btn.draw(self.surface) and self.manager.mode == "emergency":
                print("[ALERT] Sending emergency SMS...")
                # send_sms(self.manager.current_injury)  # placeholder for future
        if self.index == len(self.images) - 1:
            if self.main_btn.draw(self.surface):
                return "main_menu"
        return None

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

        # draw buttons depending on page
        if self.index == len(self.images) - 1:
            self.main_btn.draw(surface)
        else:
            if self.index > 0:
                self.back_btn.draw(surface)
            self.next_btn.draw(surface)
            if self.manager.mode == "emergency":
                self.emergency_btn.draw(surface)