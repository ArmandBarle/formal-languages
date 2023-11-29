from classes.Color import Color


class State:
    """
    A State
    :state_name = state name
    :is_initial = if the state of the state is initial
    :is_final = if the state of the state is final
    :transitions = nodes to which this node has transitions to
    """

    def __init__(self, state_name, is_initial=False, is_final=False):
        self.state_name = state_name
        self.is_initial = is_initial
        self.is_final = is_final
        self.transitions = []

    def __repr__(self):
        # Provide a string representation that, when passed to eval(), would recreate the object
        return f"State(state_name={repr(self.state_name)}, is_initial={self.is_initial}, is_final={self.is_final})"

    def __str__(self):
        # state name and their statuses
        if self.is_final and self.is_initial:
            output = Color.RED + Color.UNDERLINE + self.state_name + Color.END + ": "
        elif self.is_final:
            output = Color.RED + self.state_name + Color.END + ": "
        elif self.is_initial:
            output = Color.UNDERLINE + self.state_name + Color.END + ": "
        else:
            output = self.state_name + ": "
        if not self.transitions:
            return output

        # state transitions
        if len(self.transitions) == 0:
            return output

        for i, transition in enumerate(self.transitions):
            if i == len(self.transitions) - 1:
                output += str(transition)
            else:
                output += str(transition) + ", "

        return output

    def add_transition(self, other):
        self.transitions.append(other)

    def get_transition(self, transition):
        for t in self.transitions:
            if transition.letter == t.letter and transition.target_state == t.target_state:
                return t

    def remove_transition(self, transition):
        self.transitions.remove(transition)
