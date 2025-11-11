import pygame
import time
class State:
    def __init__(self, name):
        self.name = name

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass


class StateManager:
    def __init__(self, start_state):
        self.states = {}
        self.current_state = start_state

        # data 
        self.current_injury = None   # selected injury 
        self.mode = "emergency"      # mode
        self.drawer_opened = False   # drawer bool

    def add_state(self, state):
        self.states[state.name] = state
        state.manager = self
    def switch(self, state_name):
        if state_name in self.states:
            while any(pygame.mouse.get_pressed()):
                pygame.event.pump()
            
            if state_name == "guide":
                self.drawer_opened = False
            self.current_state = state_name
            state = self.states[state_name]
            if hasattr(state, "on_enter"):
                state.on_enter()
    def get_state(self):
        return self.states[self.current_state]
