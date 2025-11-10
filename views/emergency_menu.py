# views/emergency_menu.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data

# fixed button coordinates for 8 injury buttons (tweak to match your design)
BUTTON_POS = [
    (150, 160), (550, 160), (950, 160), (1350, 160),
    (150, 460), (550, 460), (950, 460), (1350, 460)
]

class EmergencyMenu(State):
    def __init__(self):
        super().__init__("emergency_menu")
        self.bg = assets.emergency_menu_bg
        # create buttons in the order of guide_data keys (stable order)
        keys = list(guide_data.keys())
        self.keys = keys  # store order
        self.buttons = []
        for i, key in enumerate(keys):
            x, y = BUTTON_POS[i]
            # if you have individual button images per injury, load here; else use shared image
            btn_img = assets.injury_btn_img if hasattr(assets, "injury_btn_img") else assets.emergency_btn_img
            btn = Button(x, y, btn_img, 1.0, click_sound=assets.click_sfx)
            self.buttons.append((btn, key))

    def handle_events(self, events):
        for btn, key in self.buttons:
            if btn.draw(self.surface):
                # save selected injury in manager and go to triage
                self.manager.current_injury = key
                return "triage"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        surface.blit(self.bg, (0, 0))
        for btn, _ in self.buttons:
            btn.draw(surface)
