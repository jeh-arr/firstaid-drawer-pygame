# views/severe.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data


class Severe(State):
    def __init__(self):
        super().__init__("severe")
        self.bg = None
        self.main_btn = Button(820, 965, assets.main_menu_btn_img, 1.0, click_sound=assets.back_sfx)
        self.surface = None

    def on_enter(self):
        injury = self.manager.current_injury
        data = guide_data[injury]
        self.bg = pygame.image.load(data["severe_bg"]).convert()

    def handle_events(self, events):
        if not self.surface:
            return None
        if self.main_btn.draw(self.surface):
            return "main_menu"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        surface.blit(self.bg, (0, 0))
        self.main_btn.draw(surface)