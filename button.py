import pygame
class Button:
    def __init__(self, x, y, image, scale, click_sound=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
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