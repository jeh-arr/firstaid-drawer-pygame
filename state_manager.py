import pygame

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

    def add_state(self, state):
        self.states[state.name] = state

    def switch(self, state_name):
        if state_name in self.states:
            self.current_state = state_name

    def get_state(self):
        return self.states[self.current_state]