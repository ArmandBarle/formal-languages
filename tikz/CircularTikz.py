import math

from tikz.Tikz import Tikz


class CircularTikz(Tikz):
    def __init__(self, filename):
        super().__init__(filename)

    def draw_states_circular(self, rho=10):
        """
        draws states of the automaton in a circular shape
        rho = radius
        alpha = angle is in range [0, 2pi] and divided into as many points there are
        x = rho * cos(alpha)
        y = rho * sin(alpha)
        :param automaton:
        :return:
        """
        with open("tikz_out.txt", 'w') as fout:
            # Initialization
            fout.write(
                "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3.5cm, scale = 1,transform "
                "shape]\n\n\n")

            # create coordinates for the nodes
            coords = []
            for i, state in enumerate(self.automaton.states):
                alpha = 2 * math.pi * i / len(self.automaton.states)
                state_x = rho * math.cos(alpha)
                state_y = rho * math.sin(alpha)
                coords.append((-state_x, -state_y))

            # Initializes states
            for i, state in enumerate(self.automaton.states):
                line = "\\node[state"

                # first it checks if states are initial or final and adds tags acordingly
                if state.is_initial:
                    line += ",initial"
                if state.is_final:
                    line += ",accepting"
                # adds the name of the sate then the its coordinates and the state name which is displayed
                line += "] (" + state.state_name + ") at " + str(coords[i]) + " {$" + state.state_name + "$};\n\n\n"
                fout.write(line)

    def draw_transitions_circular(self):
        with open("tikz_out.txt", 'a+') as fout:
            # initialize path
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
                    # normal transitions
                    fout.write("\t edge node "
                               "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                               "(" + transition.target_state.state_name + ")\n")

            fout.write(";\n\n\n\n")
            # end of tikz
            fout.write("\\end{tikzpicture}")
