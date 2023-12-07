from classes.State import State
from classes.Transition import Transition


class Automaton:
    def __init__(self, filename):
        # Reading automaton
        with open("input_automata/" + filename, "r") as file:
            # reading all states
            self.states = []
            all_states = file.readline().split()

            # reading alphabet
            self.alphabet = set(file.readline().split())

            # reading initial state
            self.initial_state = file.readline().strip()

            # reading final states
            self.final_states = set(file.readline().split())

            # creating states
            for state in all_states:
                self.add_state(State(state,
                                     is_initial=state == self.initial_state,
                                     is_final=state in self.final_states))

            # reading transitions and creating states
            while True:
                current_transition = file.readline().split()
                # if the end of the file is reached
                if not current_transition:
                    break
                # gets the state of the current line (first state)
                # creates a transition based on the letter and the to_state (second state)
                # adds transition to the current state
                self.get_state(current_transition[0]).add_transition(
                    Transition(current_transition[1], self.get_state(current_transition[2]))
                )

    def __str__(self):
        output = ""
        for state in self.states:
            output += str(state) + "\n"
        return output

    def add_state(self, state):
        self.states.append(state)
        if state.is_initial:
            self.initial_state = state
        if state.is_final:
            self.final_states.add(state)

    def get_state(self, state_name):
        for state in self.states:
            if state.state_name == state_name:
                return state
