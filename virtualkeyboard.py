# virtualkeyboard.py
import pygame

# Add numeric row at top
keyboard_layout = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M", "BACK"],
    ["SPACE", "ENTER", ""]
]

def handle_input(user_text, key):
    if key == "SPACE":
        user_text += " "
    elif key == "BACK":
        user_text = user_text[:-1]
    elif key not in ("ENTER", ""):
        user_text += key
    return user_text

def draw_keyboard(screen, font):
    screen_w, screen_h = screen.get_size()
    key_w = 80
    key_h = 80
    spacing = 10
    x_min, x_max = 400, 1600  # usable area
    y_start = int(screen_h * 0.55)

    # background
    pygame.draw.rect(screen, (230, 230, 230), (0, y_start - 20, screen_w, screen_h - y_start + 20))

    for row_i, row in enumerate(keyboard_layout):
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
            pygame.draw.rect(screen, (255, 255, 255), rect, border_radius=8)
            pygame.draw.rect(screen, (180, 180, 180), rect, 2, border_radius=8)

            key_surface = font.render(key, True, (0, 0, 0))
            screen.blit(key_surface, (x_start + (w - key_surface.get_width()) // 2, y + (key_h - key_surface.get_height()) // 2))
            x_start += w + spacing
