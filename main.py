import pygame, states


pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
# screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("First Aid Drawer")


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    
    currentstates = "mainmenu"
    
    match currentstates:
        case "mainmenu":
            pygame.draw.rect(screen, (0, 255, 0), (50, 50, 200, 100))  # Example button
            pygame.draw.rect(screen, (0, 0, 255), (350, 50, 200, 100))  # Example button
        
    match event.type:
        case pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 10)
            elif event.button == 3:  # Right click
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 10)
        case pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left button held down
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 10)
            elif event.buttons[2]:  # Right button held down
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 10)
        case pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Clear screen on 'c' key press        
                run = False
    pygame.display.update()
    
