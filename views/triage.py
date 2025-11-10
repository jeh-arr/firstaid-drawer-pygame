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
        self.yes_btn = Button(1400, 850, assets.yes_btn_img, 1.0, click_sound=assets.click_sfx)
        self.no_btn = Button(160, 850, assets.no_btn_img, 1.0, click_sound=assets.back_sfx)
        self.font = pygame.font.Font(None, 40)
        self.current_question = 0
        self.answered_yes = False

    def handle_events(self, events):
        # yes/no are on-screen; they indicate answer for current question.
        if self.yes_btn.draw(self.surface):
            self.answered_yes = True
            # immediate severe path
            if self.manager.mode == "emergency":
                # send SMS alert (use real number/message integration later)
                injury = self.manager.current_injury
                msg = f"Severe case: {injury} - please respond."
                send_sms(msg)
            return "severe"
        if self.no_btn.draw(self.surface):
            # go to next question or to guide if last and all no
            self.current_question += 1
            if self.current_question >= len(self.questions()):
                return "guide"
            return None
        return None

    def questions(self):
        injury = self.manager.current_injury
        return guide_data[injury]["questions"]

    def question_bg(self):
        injury = self.manager.current_injury
        return guide_data[injury]["question_bg"]

    def update(self, dt):
        pass

    def draw(self, surface):
        self.surface = surface
        # draw background image for question (load via assets or raw load)
        try:
            bg = pygame.image.load(self.question_bg()).convert()
        except Exception:
            surface.fill((40, 40, 40))
        else:
            surface.blit(bg, (0, 0))

        # question text
        q = self.questions()[self.current_question]
        wrapped = self._wrap_text(q, 60)
        y = 200
        for line in wrapped:
            surf = self.font.render(line, True, (255,255,255))
            surface.blit(surf, (120, y))
            y += 48

        # draw buttons
        self.no_btn.draw(surface)
        self.yes_btn.draw(surface)

    def _wrap_text(self, text, max_chars):
        words = text.split(" ")
        lines = []
        cur = ""
        for w in words:
            if len(cur) + 1 + len(w) <= max_chars:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines
