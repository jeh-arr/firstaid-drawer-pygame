import pygame
from state_manager import State
from button import Button
import assets
import time

SECRET_ZONE = pygame.Rect(820, 20, 280, 80)
class MainMenu(State):
    def __init__(self):
        super().__init__("main_menu")
        self.bg = assets.main_menu_bg
        self.emergency_btn = Button(635, 690, assets.emergency_btn_img, 1.0, click_sound=assets.click_sfx)
        self.learning_btn = Button(635, 860, assets.learning_btn_img, 1.0, click_sound=assets.back_sfx)
        self.surface = None  
        self.tap_times = []
    def handle_events(self, events):
        if not self.surface:
            return None
        # if any(pygame.mouse.get_pressed()):
        #     return None  # ignore until finger fully lifted
       
            
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                
                if SECRET_ZONE.collidepoint(e.pos):
                    
                    now = time.time()
                    self.tap_times = [t for t in self.tap_times if now - t < 4]  # 4 sec window
                    self.tap_times.append(now)
                    if len(self.tap_times) >= 3:  # make it 3 taps for testing
                        print("[DEBUG] Secret settings triggered!")
                        return "settings"
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
        pygame.draw.rect(surface, (255, 0, 0), SECRET_ZONE, 2)