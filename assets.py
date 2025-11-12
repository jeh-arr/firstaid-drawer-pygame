# assets.py

import pygame
pygame.init()
# Load images


start_bg = pygame.image.load("images/start.png")
main_menu_bg = pygame.image.load("images/main_menu.png")
emergency_menu_bg = pygame.image.load("images/emergency_menu.png")

# Load sfx
click_sfx = pygame.mixer.Sound("audio/pop_confirm.mp3")
back_sfx = pygame.mixer.Sound("audio/pop_cancel.mp3")

# Load button images
emergency_btn_img = pygame.image.load("images/button/emergency_btn.png")
learning_btn_img = pygame.image.load("images/button/learning_btn.png")
main_menu_btn_img = pygame.image.load("images/button/mainmenu_btn.png")

emergency_call_btn_img = pygame.image.load("images/button/emergency2_btn.png")
emergency_menu_btn_img = pygame.image.load("images/button/mainmenu2_btn.png")
# injury_btn_img = pygame.image.load("images/button/injury_btn.png")
next_btn_img = pygame.image.load("images/button/next_btn.png")
back_btn_img = pygame.image.load("images/button/back_btn.png")
yes_btn_img = pygame.image.load("images/button/yes_btn.png")
no_btn_img = pygame.image.load("images/button/no_btn.png")

# Placeholder vars (set later in main.py)
scale_x = scale_y = scale_min = 1
actual_w = actual_h = 1920