# assets.py

import pygame
pygame.init()
# def load_image(path):
#     return pygame.image.load(path).convert_alpha()

# Backgrounds
start_bg = pygame.image.load("images/start.png")
main_menu_bg = pygame.image.load("images/main_menu.png")
emergency_menu_bg = pygame.image.load("images/emergency_menu.png")

# SFX
click_sfx = pygame.mixer.Sound("audio/pop_confirm.mp3")
back_sfx = pygame.mixer.Sound("audio/pop_cancel.mp3")

# Buttons
emergency_btn_img = pygame.image.load("images/button/emergency_btn.png")
learning_btn_img = pygame.image.load("images/button/learning_btn.png")
main_menu_btn_img = pygame.image.load("images/button/mainmenu_btn.png")
emergency_call_btn_img = pygame.image.load("images/button/emergency2_btn.png")
emergency_menu_btn_img = pygame.image.load("images/button/mainmenu2_btn.png")
next_btn_img = pygame.image.load("images/button/next_btn.png")
back_btn_img = pygame.image.load("images/button/back_btn.png")
yes_btn_img = pygame.image.load("images/button/yes_btn.png")
no_btn_img = pygame.image.load("images/button/no_btn.png")

# scale_x = scale_y = scale_min = 1
# actual_w = actual_h = 1920