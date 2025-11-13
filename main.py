import pygame
from state_manager import StateManager
from views.start import StartScreen
from views.main_menu import MainMenu
from views.emergency_menu import EmergencyMenu
from views.triage import Triage
from views.severe import Severe
from views.guide import Guide
from views.settings import Settings
import assets, utils 

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# actual_w ,actual_h = screen.get_size()
# screen = pygame.display.set_mode(0, 0)
# actual_w = 1024
# actual_h = 768

# BASE_W, BASE_H = 1920, 1080

BASE_W, BASE_H = 1920, 1080
screen = pygame.display.set_mode((BASE_W, BASE_H), pygame.FULLSCREEN | pygame.SCALED)
# scale_x = actual_w / BASE_W
# scale_y = actual_h / BASE_H
# scale_min = min(scale_x, scale_y)


# assets.scale_x = scale_x
# assets.scale_y = scale_y
# assets.scale_min = scale_min
# assets.actual_w = actual_w
# assets.actual_h = actual_h

# from utils import apply_scaling
# utils.apply_scaling()

pygame.display.set_caption("First Aid Drawer")
clock = pygame.time.Clock()

manager = StateManager("start")
manager.add_state(StartScreen())
manager.add_state(MainMenu())
manager.add_state(EmergencyMenu())
manager.add_state(Triage())
manager.add_state(Severe())
manager.add_state(Guide())
manager.add_state(Settings())

for s in manager.states.values():
    s.manager = manager

running = True
while running:
    dt = clock.tick(60) / 1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    current = manager.get_state()
    next_state = current.handle_events(events)
    if next_state:
        if next_state == "quit":
            running = False
        else:
            manager.switch(next_state)

    current.update(dt)
    current.draw(screen)
    pygame.display.flip()

pygame.quit()
