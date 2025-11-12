import pygame
from assets import scale_min, scale_x, scale_y
class Button:
    def __init__(self, x, y, image, scale, click_sound=None):
        global_scale = scale * scale_min
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width * global_scale), int(height * global_scale)))
        self.rect = self.image.get_rect(topleft=(int(x * scale_x), int(y * scale_y)))
        self.click_sound = click_sound
        self.pressed_inside = False   # only true if press began on this button

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        left_pressed = pygame.mouse.get_pressed()[0]

        # press started on this button
        if left_pressed and self.rect.collidepoint(pos) and not self.pressed_inside:
            self.pressed_inside = True

        # finger released -> trigger action only if it started on this same button
        if not left_pressed and self.pressed_inside:
            if self.rect.collidepoint(pos):  # released still within button
                if self.click_sound:
                    self.click_sound.play()
                action = True
            self.pressed_inside = False  # reset every release

        # draw button image
        surface.blit(self.image, self.rect.topleft)
        return action