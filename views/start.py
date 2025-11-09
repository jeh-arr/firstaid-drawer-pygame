# views/start.py
import pygame
from state_manager import State
import assets

class StartScreen(State):
    def __init__(self):
        super().__init__("start")
        self.bg = assets.start_bg  # e.g. images/start.png
        # self.text = assets.start_text  # pre-rendered text surface (optional)
        self.clicked = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Any click transitions to main menu
                return "main_menu"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.bg, (0, 0))
        # Centered text overlay (optional)
        
