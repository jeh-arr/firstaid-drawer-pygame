# views/guide.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data
from utils import unlock_drawer_for, send_sms

class Guide(State):
    def __init__(self):
        super().__init__("guide")
        self.index = 0
        self.font = pygame.font.Font(None, 36)
        # Buttons: main, emergency, back, next (positions can be adjusted)
        self.main_btn = Button(80, 920, assets.main_menu_btn_img, 1.0, click_sound=assets.back_sfx)
        self.emergency_btn = Button(540, 920, assets.emergency_small_btn_img, 1.0, click_sound=assets.click_sfx)
        self.back_btn = Button(1000, 920, assets.back_small_btn_img, 1.0, click_sound=assets.back_sfx)
        self.next_btn = Button(1400, 920, assets.next_small_btn_img, 1.0, click_sound=assets.click_sfx)

    def handle_events(self, events):
        if self.main_btn.draw(self.surface):
            return "start"
        if self.emergency_btn.draw(self.surface):
            # immediate emergency SMS
            if self.manager.mode == "emergency":
                send_sms(f"Request assistance: {self.manager.current_injury}")
            return None
        if self.back_btn.draw(self.surface):
            if self.index > 0:
                self.index -= 1
            return None
        if self.next_btn.draw(self.surface):
            imgs = self.images()
            if self.index < len(imgs) - 1:
                self.index += 1
            return None
        return None

    def images(self):
        return guide_data[self.manager.current_injury]["images"]

    def update(self, dt):
        # on first page open: trigger drawer once if emergency mode and not yet opened
        if self.index == 0 and self.manager.mode == "emergency" and not self.manager.drawer_opened:
            unlock_drawer_for(self.manager.current_injury)
            self.manager.drawer_opened = True

    def draw(self, surface):
        self.surface = surface
        imgs = self.images()
        path = imgs[self.index]
        try:
            bg = pygame.image.load(path).convert()
            surface.blit(bg, (0,0))
        except Exception:
            surface.fill((30,30,30))
            txt = self.font.render(f"Guide page {self.index+1}/{len(imgs)}", True, (255,255,255))
            surface.blit(txt, (100, 100))

        # navigation buttons
        self.main_btn.draw(surface)
        self.emergency_btn.draw(surface)
        self.back_btn.draw(surface)
        self.next_btn.draw(surface)
