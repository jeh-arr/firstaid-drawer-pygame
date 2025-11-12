# views/severe.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data


def load_scaled_image(path):
    img = pygame.image.load(path).convert()
    w = int(img.get_width() * assets.scale_x)
    h = int(img.get_height() * assets.scale_y)
    return pygame.transform.scale(img, (w, h))
class Severe(State):
    def __init__(self):
        super().__init__("severe")
        self.bg = None
        self.main_btn = Button(820, 965, assets.main_menu_btn_img, 1.0, click_sound=assets.back_sfx)
        self.surface = None

    def on_enter(self):
        injury = self.manager.current_injury
        data = guide_data[injury]
        self.bg = load_scaled_image(data["severe_bg"])

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