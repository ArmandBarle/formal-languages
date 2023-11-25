from classes.Automaton import Automaton
from classes.StackTransition import StackTransition
from classes.State import State
import re


class StackAutomaton(Automaton):

    def __init__(self, filename):
        # super(StackAutomaton, self).__init__(filename)
        # Reading automaton
        with open(filename, "r") as file:

            self.states = []
            # reading all states (line 1)
            # save states to create actual states later
            all_states = file.readline().split()

            # reading alphabet (line 2)
            self.alphabet = set(file.readline().split())

            # reading stack alphabet (line 3)
            self.stack_alphabet = set(file.readline().split())

            # reading initial state (line 4)
            self.initial_state = file.readline().strip()

            # reading initial stack value (line 5)
            self.stack = file.readline().strip()

            # reading final states (line 6)
            self.final_states = set(file.readline().split())

            # creating states
            for state in all_states:
                self.add_state(State(state,
                                     is_initial=state == self.initial_state,
                                     is_final=state in self.final_states))

            # reading transitions and creating states (line 6+)
            while True:
                current_transition = file.readline().split()
                # if the end of the file is reached
                if not current_transition:
                    break
                # creates a transition
                # adds transition to the current state

                self.get_state(current_transition[0]).add_transition(  # current state
                    StackTransition(current_transition[1],  # letter
                                    current_transition[2],  # stack_out
                                    current_transition[3],  # stack_in
                                    self.get_state(current_transition[4]))  # target_state
                )

