# views/emergency_menu.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data

BUTTON_SIZE = 280
BUTTON_SPACING = 65
COLUMNS = 4
ROWS = 2
TOTAL_WIDTH = COLUMNS * BUTTON_SIZE + (COLUMNS - 1) * BUTTON_SPACING
TOTAL_HEIGHT = ROWS * BUTTON_SIZE + (ROWS - 1) * BUTTON_SPACING


SCREEN_W, SCREEN_H = 1920, 1080
START_X = (SCREEN_W - TOTAL_WIDTH) // 2
START_Y = (SCREEN_H - TOTAL_HEIGHT) // 2

class EmergencyMenu(State):
    def __init__(self):
        super().__init__("emergency_menu")
        self.bg = assets.emergency_menu_bg

        keys = list(guide_data.keys())
        self.keys = keys
        self.buttons = []

        for idx, key in enumerate(keys):
            row = idx // COLUMNS
            col = idx % COLUMNS
            x = START_X + col * (BUTTON_SIZE + BUTTON_SPACING)
            y = START_Y + row * (BUTTON_SIZE + BUTTON_SPACING)

            # load injury button 
            img_path = f"images/button/{key.lower().split('(')[0].strip().replace(' ', '_').replace('/', '_')}_btn.png"

            try:
                btn_img = pygame.image.load(img_path).convert_alpha()
            except:
                btn_img = assets.emergency_btn_img 

            btn = Button(x, y, btn_img, 1.0, click_sound=assets.click_sfx)
            self.buttons.append((btn, key))

        self.surface = None

    def handle_events(self, events):
        if not self.surface:
            return None
        for btn, key in self.buttons:
            if btn.draw(self.surface):
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
