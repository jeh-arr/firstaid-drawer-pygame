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
        self.emergency_main_btn = Button(1100, 950, assets.emergenccy_menu_btn_img, 1.0, click_sound=assets.back_sfx)

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

        # active buttons per state
        active_buttons = []

        if last_page:
            active_buttons = [("main_menu", self.main_btn)]
        else:
            active_buttons = [("next", self.next_btn)]
            if self.index > 0:
                active_buttons.append(("back", self.back_btn))
            if first_page:
                active_buttons.append(("emergency_menu", self.emergency_main_btn))
            elif self.manager.mode == "emergency":
                active_buttons.append(("emergency", self.emergency_btn))

        # check only active buttons
        for name, btn in active_buttons:
            if btn.draw(self.surface):
                if name == "next":
                    self.index += 1
                elif name == "back":
                    self.index -= 1
                elif name == "main_menu":
                    return "main_menu"
                elif name == "emergency_menu":
                    return "emergency_menu"
                elif name == "emergency":
                    print("[ALERT] Sending emergency SMS...")
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

        # draw only relevant buttons for the current page
        first_page = self.index == 0
        last_page = self.index == len(self.images) - 1

        if last_page:
            self.main_btn.draw(surface)
        else:
            self.next_btn.draw(surface)
            if self.index > 0:
                self.back_btn.draw(surface)
            if first_page:
                self.emergency_main_btn.draw(surface)
            elif self.manager.mode == "emergency":
                self.emergency_btn.draw(surface)