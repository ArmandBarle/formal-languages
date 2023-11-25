from classes.Transition import Transition


class StackTransition(Transition):
    def __init__(self, letter, stack_out, stack_in, target_state):
        super(StackTransition, self).__init__(letter, target_state)
        self.stack_out = stack_out
        self.stack_in = stack_in

    def __str__(self):
        return f"({self.letter[0]},{self.stack_out}/{self.stack_in}) -> {self.target_state.state_name} "
