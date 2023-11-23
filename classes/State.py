class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class State:
    """
    A State
    :state_name = state name
    :is_initial = if the state of the state is initial
    :is_final = if the state of the state is final
    :transitions = nodes to which this node has transitions to
    """

    def __init__(self, state_name, is_initial=False, is_final=False):
        self.is_final = is_final
        self.is_initial = is_initial
        self.state_name = state_name
        self.transitions = {}  # Dictionary of {input_symbol: target state}

    def __str__(self):
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

        for symbol, target_state in self.transitions.items():
            if isinstance(target_state, list):
                # For multiple transitions for the same input symbol
                targets = ", ".join(state.state_name for state in target_state)
                output += f"{symbol} -> [{targets}] "
            else:
                if isinstance(target_state, State):
                    output += f"{symbol} -> {target_state.state_name} "
                else:
                    output += f"{symbol} -> {target_state} "

        return output

    def add_transition(self, input_symbol, target_state):
        if input_symbol in self.transitions:
            self.transitions[input_symbol] += [target_state]
        else:
            self.transitions[input_symbol] = [target_state]

    def blend_transitions(automaton):
        for state in automaton.states:
            for transition_letter in state.transitions.keys():
                new_transtitions = []
                found_transitions = False
                for transition_letter2 in state.transitions.keys():
                    if transition_letter == transition_letter2:
                        continue
                    if state.transitions[transition_letter] == state.transitions[transition_letter2]:
                        found_transitions = True
                        state.transitions.pop(transition_letter2)
                        new_transtitions.append(transition_letter)
                if found_transitions:
                    state.add_transition(tuple(new_transtitions), state.state_name)