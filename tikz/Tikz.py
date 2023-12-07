from classes.Automaton import Automaton


class Tikz:
    def __init__(self, input_file, output_file):
        self.automaton = Automaton(input_file)
        self.output_file = output_file
        self.draw_states()
        self.draw_transitions()

    @staticmethod
    def in_transition(target_state, from_state):
        """
        checks if the target_state is in  from_state's transitions
        :param target_state: state where transition goes to
        :param from_state: state where transition goes from
        :return: boolean if target_state is in from_state transitions
        """
        for transition in from_state.transitions:
            if target_state.state_name == transition.target_state.state_name:
                return True
        return False

    @staticmethod
    def blend_transition(state):
        """
        blends transitions that go to the same state with different letters
        :param state: state of which states are going to be blended
        :return: state with blended states
        """
        same_transitions = []
        for i, transition1 in enumerate(state.transitions[:-1]):
            for transition2 in state.transitions[i + 1:]:
                if transition1.target_state.state_name == transition2.target_state.state_name:
                    same_transitions.append((transition1, transition2))

        for transition in same_transitions:
            state.remove_transition(transition[1])
            state.get_transition(transition[0]).add_letter(transition[1].letter[0])

    def draw_states(self):
        pass

    def draw_transitions(self):
        pass
