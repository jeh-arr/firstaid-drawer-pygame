import pygame
from state_manager import StateManager
from views.start import StartScreen
from views.main_menu import MainMenu
from views.emergency_menu import EmergencyMenu
from views.triage import Triage
# from views.severe import Severe
# from views.guide import Guide
import assets  

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("First Aid Drawer")
clock = pygame.time.Clock()

manager = StateManager("start")
manager.add_state(StartScreen())
manager.add_state(MainMenu())
manager.add_state(EmergencyMenu())
manager.add_state(Triage())
# manager.add_state(Severe())
# manager.add_state(Guide())

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
