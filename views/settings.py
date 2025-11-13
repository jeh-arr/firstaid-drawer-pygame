import pygame, json, os, sys
from state_manager import State
from button import Button
import virtualkeyboard
import assets

CONFIG_FILE = "config/settings.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"number": "", "location": ""}

def save_config(data):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

class Settings(State):
    def __init__(self):
        super().__init__("settings")
        self.font = pygame.font.Font(None, 60)
        self.data = load_config()
        self.active_field = None
        self.surface = None

        self.number_rect = pygame.Rect(500, 150, 900, 80)
        self.loc_rect = pygame.Rect(500, 270, 900, 80)

        self.save_btn = Button(1200, 400, assets.save_btn_img, 1, click_sound=assets.click_sfx)
        self.back_btn = Button(850, 400, assets.back2_btn_img, 1, click_sound=assets.back_sfx)
        self.quit_btn = Button(500, 400, assets.quit_btn_img, 1, click_sound=assets.back_sfx)

    def handle_events(self, events):
        if not self.surface:
            return None

        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.number_rect.collidepoint(e.pos):
                    self.active_field = "number"
                elif self.loc_rect.collidepoint(e.pos):
                    self.active_field = "location"
                else:
                    key = self.get_key_from_keyboard(e.pos)
                    if key:
                        self.apply_key(key)
                        assets.keyboard_sfx.play()

        # handle buttons every frame
        if self.save_btn.draw(self.surface):
            save_config(self.data)
            print("[CONFIG] Saved:", self.data)
            return "main_menu"

        if self.back_btn.draw(self.surface):
            return "main_menu"

        if self.quit_btn.draw(self.surface):
            pygame.quit(); sys.exit()

        return None

    def apply_key(self, key):
        if not self.active_field:
            return
        val = self.data[self.active_field]
        new_val = virtualkeyboard.handle_input(val, key)
        self.data[self.active_field] = new_val

    def get_key_from_keyboard(self, pos):
        screen_w, screen_h = self.surface.get_size()
        key_w, key_h, spacing = 80, 80, 10
        y_start = int(screen_h * 0.55)
        x_min = 400

        mx, my = pos

        for row_i, row in enumerate(virtualkeyboard.keyboard_layout):
            # same width calculation as draw_keyboard
            total_row_w = sum(
                [300 if k == "SPACE" else 140 if k in ("BACK", "ENTER") else key_w for k in row if k]
            ) + (len(row) - 1) * spacing

            x_start = max(x_min, (screen_w - total_row_w) // 2)
            y = y_start + row_i * (key_h + spacing)

            for key in row:
                if key == "SPACE":
                    w = 300
                elif key in ("BACK", "ENTER"):
                    w = 140
                elif key == "":
                    x_start += key_w + spacing
                    continue
                else:
                    w = key_w

                rect = pygame.Rect(x_start, y, w, key_h)
                if rect.collidepoint(mx, my):
                    return key

                x_start += w + spacing
        return None
    def draw(self, surface):
        self.surface = surface
        surface.fill((255, 255, 255))

        active_color = (0, 100, 255)
        inactive_color = (0, 0, 0)

        pygame.draw.rect(surface,
                         active_color if self.active_field == "number" else inactive_color,
                         self.number_rect, 3)
        pygame.draw.rect(surface,
                         active_color if self.active_field == "location" else inactive_color,
                         self.loc_rect, 3)

        surface.blit(self.font.render(f"Number: {self.data['number']}", True, (0, 0, 0)), (self.number_rect.x + 10, self.number_rect.y + 20))
        surface.blit(self.font.render(f"Location: {self.data['location']}", True, (0, 0, 0)), (self.loc_rect.x + 10, self.loc_rect.y + 20))

        self.save_btn.draw(surface)
        self.back_btn.draw(surface)
        self.quit_btn.draw(surface)

        virtualkeyboard.draw_keyboard(surface, self.font)
