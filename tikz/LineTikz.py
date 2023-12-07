from tikz.Tikz import Tikz


class LineTikz(Tikz):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def draw_states(self):
        with open("output_automata/" + self.output_file, 'w') as fout:
            # Initialization
            fout.write(
                "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2.6cm, scale = 1,transform "
                "shape]\n\n\n")

            # Initializes states
            previous_state = None
            for state in self.automaton.states:
                line = "\\node[state"

                # first it checks if states are initial or final and adds tags acordingly
                # creates first state
                if state == self.automaton.states[0]:
                    if state.is_initial:
                        line += ",initial"
                    if state.is_final:
                        line += ",accepting"
                    line += "] (" + state.state_name + ") {$" + state.state_name + "$};\n\n\n"
                    previous_state = state
                    fout.write(line)
                    continue
                if state.is_initial:
                    line += ",initial"
                if state.is_final:
                    line += ",accepting"
                line += "] (" + state.state_name + ")"

                # end of line if normal states always adds them to the right of the previous state
                line += "[right of=" + previous_state.state_name + "] {$" + state.state_name + "$};\n\n"
                fout.write(line)
                previous_state = state

    def draw_transitions(self):
        with open("output_automata/" + self.output_file, 'a+') as fout:
            fout.write("\t\\path[->]\n")

            # loop through all states and write them in chunks
            for i, state in enumerate(self.automaton.states):
                # first write state's name
                fout.write("\t(" + state.state_name + ")")

                # puts together letters that use the same edge (used later)
                super().blend_transition(state)

                for transition in state.transitions:
                    # checks for loops
                    if transition.target_state == state:
                        # checks to write the loop above or below, depending on whether its in the top or bottom row
                        if i < len(self.automaton.states) / 2:
                            fout.write(
                                "\t edge[loop above] node "
                                "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                                "(" + transition.target_state.state_name + ")\n")
                            continue
                        else:
                            fout.write(
                                "\t edge[loop below] node "
                                "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                                "(" + transition.target_state.state_name + ")\n")
                            continue

                    # check for bends
                    if super().in_transition(state, transition.target_state):
                        fout.write(
                            "\t edge[bend right] node "
                            "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                            "(" + transition.target_state.state_name + ")\n")
                        continue
                    # check for neighbours
                    if self.automaton.states.index(state) == self.automaton.states.index(transition.target_state) - 1 \
                            or self.automaton.states.index(state) == self.automaton.states.index(
                        transition.target_state) + 1:
                        fout.write("\t edge node " +
                                   "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                                   "(" + transition.target_state.state_name + ")\n")
                        continue

                    # normal transitions
                    fout.write("\t edge[bend right] node "
                               "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                               "(" + transition.target_state.state_name + ")\n")

            fout.write(";\n\n\n\n")
            # end of tikz
            fout.write("\\end{tikzpicture}")
