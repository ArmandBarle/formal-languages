class Automaton:
    def __init__(self, alphabet=None):
        self.states = []
        self.alphabet = set(alphabet)
        self.initial_state = None
        self.final_states = set()

    def add_state(self, state):
        self.states.append(state)
        if state.is_initial:
            self.initial_state = state
        if state.is_final:
            self.final_states.add(state)

    def __str__(self):
        output = ""
        for state in self.states:
            output += str(state) + "\n"
        return output

    def __repr__(self):
        return str(self)
