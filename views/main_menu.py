import pygame
from state_manager import State
from button import Button
import assets

class MainMenu(State):
    def __init__(self):
        super().__init__("main_menu")
        self.bg = assets.main_menu_bg
        self.emergency_btn = Button(635, 690, assets.emergency_btn_img, 1.0, click_sound=assets.click_sfx)
        self.learning_btn = Button(635, 860, assets.learning_btn_img, 1.0, click_sound=assets.back_sfx)
        self.surface = None  # ensure exists

    def handle_events(self, events):
        if not self.surface:
            return None
        if any(pygame.mouse.get_pressed()):
            return None  # ignore until finger fully lifted

        # let button.py handle click detection
        if self.emergency_btn.draw(self.surface):
            self.manager.mode = "emergency"
            return "emergency_menu"
        if self.learning_btn.draw(self.surface):
            self.manager.mode = "learning"
            return "emergency_menu"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        surface.blit(self.bg, (0, 0))
        self.emergency_btn.draw(surface)
        self.learning_btn.draw(surface)
