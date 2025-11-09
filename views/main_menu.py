# main_menu.py
from state_manager import State
from button import Button
import assets   # assuming you load images here

class MainMenu(State):
    def __init__(self):
        super().__init__("main_menu")
        # self.play_btn = Button(250, 200, assets.play_img, 1.0, click_sound=assets.click_sfx)
        # self.quit_btn = Button(250, 320, assets.quit_img, 1.0)

    def handle_events(self, events):
        # if self.play_btn.draw(self.surface):
        #     return "triage"
        # if self.quit_btn.draw(self.surface):
        #     return "quit"
        return None

    def draw(self, surface):
        surface.fill((30, 30, 30))
        self.surface = surface
        self.play_btn.draw(surface)
        self.quit_btn.draw(surface)
