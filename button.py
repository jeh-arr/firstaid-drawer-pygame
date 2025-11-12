import pygame
import assets
class Button:
    def __init__(self, x, y, image, scale=1.0, click_sound=None):
        # automatically scale image and position based on actual screen ratio
        width = image.get_width()
        height = image.get_height()

        # apply scaling relative to screen
        global_scale = scale * assets.scale_min
        scaled_w = int(width * global_scale)
        scaled_h = int(height * global_scale)
        scaled_x = int(x * assets.scale_x)
        scaled_y = int(y * assets.scale_y)

        self.image = pygame.transform.scale(image, (scaled_w, scaled_h))
        self.rect = self.image.get_rect(topleft=(scaled_x, scaled_y))
        self.click_sound = click_sound
        self.pressed_inside = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        left_pressed = pygame.mouse.get_pressed()[0]

        if left_pressed and self.rect.collidepoint(pos) and not self.pressed_inside:
            self.pressed_inside = True

        if not left_pressed and self.pressed_inside:
            if self.rect.collidepoint(pos):
                if self.click_sound:
                    self.click_sound.play()
                action = True
            self.pressed_inside = False

        surface.blit(self.image, self.rect.topleft)
        return action