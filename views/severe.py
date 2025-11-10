# views/severe.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data

class Severe(State):
    def __init__(self):
        super().__init__("severe")
        self.main_btn = Button(800, 900, assets.main_menu_btn_img, 1.0, click_sound=assets.back_sfx)
        self.font = pygame.font.Font(None, 48)

    def handle_events(self, events):
        if self.main_btn.draw(self.surface):
            return "start"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        injury = self.manager.current_injury
        bg_path = guide_data[injury]["severe_bg"]
        try:
            bg = pygame.image.load(bg_path).convert()
            surface.blit(bg, (0,0))
        except Exception:
            surface.fill((100,0,0))
            txt = self.font.render("Help is on the way", True, (255,255,255))
            surface.blit(txt, (400, 300))

        self.main_btn.draw(surface)
