# views/triage.py
import pygame
from state_manager import State
from button import Button
import assets
from guide_data import guide_data
from utils import send_sms

class Triage(State):
    def __init__(self):
        super().__init__("triage")
        self.bg = None
        self.questions = []
        self.yes_btn = Button(620, 850, assets.yes_btn_img, 1.0, click_sound=assets.click_sfx)
        self.no_btn = Button(1080, 850, assets.no_btn_img, 1.0, click_sound=assets.back_sfx)
        self.index = 0
        self.answered_yes = False
        self.surface = None

        self.font = pygame.font.Font(None, 64)
        self.text_color = (164, 0, 0)

    def on_enter(self):
        # Refresh data 
        injury = self.manager.current_injury
        data = guide_data[injury]
        if not data:
            print(f"[WARN] No guide data for '{self.manager.current_injury}', skipping triage.")
            return

        try:
            self.bg = pygame.image.load(data["question_bg"]).convert()
            self.questions = data.get("questions", [])
            self.severe_bg = data.get("severe_bg")
        except (FileNotFoundError, TypeError):
            print(f"[WARN] Missing triage assets for '{self.manager.current_injury}', skipping triage.")
            self.manager.current_injury = None
            # stay in emergency menu instead of crashing
            self.manager.switch("emergency_menu")
        self.index = 0
        self.answered_yes = False

    def handle_events(self, events):
        if not self.surface:
            return None

        # buttons 
        if self.yes_btn.draw(self.surface):
            self.answered_yes = True
            if self.manager.mode == "emergency":
                send_sms(self.manager.current_injury)
            return "severe"
        if self.no_btn.draw(self.surface):
            self.index += 1
            if self.index >= len(self.questions):
                return "guide"
        return None

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        surface.blit(self.bg, (0, 0))
        if self.index < len(self.questions):
            text = self.questions[self.index]
            rendered = self.font.render(text, True, self.text_color)
            rect = rendered.get_rect(center=(surface.get_width() // 2, 600))
            surface.blit(rendered, rect)
        self.yes_btn.draw(surface)
        self.no_btn.draw(surface)
