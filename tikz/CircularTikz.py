import math

from tikz.Tikz import Tikz


def loop_orientation(angle):
    normalized_angle = angle % (2 * math.pi)
    if math.pi / 4 < normalized_angle < 3 * math.pi / 4:
        return "below"
    elif 3 * math.pi / 4 < normalized_angle < 5 * math.pi / 4:
        return "right"
    elif 5 * math.pi / 4 < normalized_angle < 7 * math.pi / 4:
        return "above"
    else:
        return "left"


class CircularTikz(Tikz):
    def __init__(self, filename):
        self.angles = []
        super().__init__(filename)

    def draw_states(self, rho=5):
        """
        draws states of the automaton in a circular shape
        alpha = angle is in range [0, 2pi] and divided into as many points there are
        x = rho * cos(alpha)
        y = rho * sin(alpha)
        :param rho: radius
        :return: a file called tikz_out.txt with the positioning of the states
        """
        if len(self.automaton.states) > 10:
            rho += (len(self.automaton.states) - 10) / 2

        with open("tikz_out.txt", 'w') as fout:
            # Initialization
            fout.write(
                "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3.5cm, scale = 1,transform "
                "shape]\n\n\n")

            # create coordinates for the nodes
            coords = []
            for i, state in enumerate(self.automaton.states):
                alpha = 2 * math.pi * i / len(self.automaton.states)
                self.angles.append(alpha)
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
                line += "] (" + state.state_name + ") at " + str(coords[i]) + " {$" + state.state_name + "$};\n\n"
                fout.write(line)

    def draw_transitions(self):
        """
        draws the transitions of the automaton

        :return: a file called tikz_out.txt with the transitions between existing states
        """
        with open("tikz_out.txt", 'a+') as fout:

            # initialize path
            fout.write("\t\\path[->]\n")

            # loop through all states and write them in chunks
            for i, state in enumerate(self.automaton.states):
                # first write state's name
                fout.write("\t(" + state.state_name + ")")

                # puts together letters that use the same edge (used later)
                # eg.from q0 a and b both go to q1
                super().blend_transition(state)

                for transition in state.transitions:
                    # checks for loops ex. q0 -> q0
                    if transition.target_state == state:
                        # checks where to write loop depending on the position of the state
                        # eg. above, below, right, left
                        fout.write(
                            "\t edge[loop " + loop_orientation(self.angles[i]) + "] node {" +
                            ", ".join(str(letter) for letter in transition.letter) + "} " +
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
