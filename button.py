import pygame

class Button:
    def __init__(self, x, y, image, scale, click_sound=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.click_sound = click_sound  

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check if the mouse is over the button and the left mouse button is released
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:  # Trigger action on release
                if self.click_sound:
                    self.click_sound.play()
                action = True  # Perform the action on mouse release
            # Check if the left mouse button is pressed down
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            else:
                self.clicked = False
        
        # Draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action    
