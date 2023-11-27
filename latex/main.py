from classes.Automaton import Automaton


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


def draw_states_multiline(automaton):
    with open("tikz_out.txt", 'w') as fout:
        # Initialization
        fout.write(
            "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3.5cm, scale = 1,transform "
            "shape]\n\n\n")

        # Initializes states
        previous_state = None
        for state in automaton.states:
            line = "\\node[state"

            # first it checks if states are initial or final and adds tags acordingly
            # creates first state
            if state == automaton.states[0]:
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

            # after the automata wrote half of its states it starts in a new line
            if len(automaton.states) % 2 == 0 and state == automaton.states[int(len(automaton.states) / 2)]:
                line += "[below of=" + automaton.states[0].state_name + "] {$" + state.state_name + "$};\n\n\n"
                previous_state = state
                fout.write(line)
                continue

            if len(automaton.states) % 2 == 1 and state == automaton.states[int(len(automaton.states) // 2) + 1]:
                line += "[below of=" + automaton.states[0].state_name + "] {$" + state.state_name + "$};\n\n\n"
                previous_state = state
                fout.write(line)
                continue

            # end of line if normal states always adds them to the right of the previous state
            line += "[right of=" + previous_state.state_name + "] {$" + state.state_name + "$};\n\n\n"
            fout.write(line)
            previous_state = state


def draw_states_single_line(automaton):
    with open("tikz_out.txt", 'w') as fout:
        # Initialization
        fout.write(
            "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3.5cm, scale = 1,transform "
            "shape]\n\n\n")

        # Initializes states
        previous_state = None
        for state in automaton.states:
            line = "\\node[state"

            # first it checks if states are initial or final and adds tags acordingly
            # creates first state
            if state == automaton.states[0]:
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
            line += "[right of=" + previous_state.state_name + "] {$" + state.state_name + "$};\n\n\n"
            fout.write(line)
            previous_state = state


def draw_states_circular(automaton):
    with open("tikz_out.txt", 'w') as fout:
        # Initialization
        fout.write(
            "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3.5cm, scale = 1,transform "
            "shape]\n\n\n")

        # Initializes states
        previous_state = None
        for state in automaton.states:
            line = "\\node[state"

            # first it checks if states are initial or final and adds tags acordingly
            # creates first state
            if state == automaton.states[0]:
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

            # after the automata wrote half of its states it starts in a new line
            if len(automaton.states) % 2 == 0 and state == automaton.states[int(len(automaton.states) / 2)]:
                line += "[below of=" + automaton.states[0].state_name + "] {$" + state.state_name + "$};\n\n\n"
                previous_state = state
                fout.write(line)
                continue

            if len(automaton.states) % 2 == 1 and state == automaton.states[int(len(automaton.states) // 2) + 1]:
                line += "[below of=" + automaton.states[0].state_name + "] {$" + state.state_name + "$};\n\n\n"
                previous_state = state
                fout.write(line)
                continue

            # end of line if normal states always adds them to the right of the previous state
            line += "[right of=" + previous_state.state_name + "] {$" + state.state_name + "$};\n\n\n"
            fout.write(line)
            previous_state = state


def draw_transitions(automaton):
    with open("tikz_out.txt", 'a+') as fout:
        # initialize path
        fout.write("\t\\path[->]\n")

        # loop through all states and write them in chunks
        for i, state in enumerate(automaton.states):
            # first write state's name
            fout.write("\t(" + state.state_name + ")")

            # puts together letters that use the same edge (used later)
            blend_transition(state)

            for transition in state.transitions:
                # checks for loops
                if transition.target_state == state:
                    # checks to write the loop above or below, depending on whether its in the top or bottom row
                    if i < len(automaton.states) / 2:
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
                if in_transition(state, transition.target_state):
                    fout.write(
                        "\t edge[bend right] node "
                        "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                        "(" + transition.target_state.state_name + ")\n")
                    continue
                # normal transitions
                fout.write("\t edge node "
                           "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                           "(" + transition.target_state.state_name + ")\n")

        fout.write("\n\n\n\n")
        # end of tikz
        fout.write("\\end{tikzpicture}")


def draw_transitions_straight_line(automaton):
    with open("tikz_out.txt", 'a+') as fout:
        fout.write("\t\\path[->]\n")

        # loop through all states and write them in chunks
        for i, state in enumerate(automaton.states):
            # first write state's name
            fout.write("\t(" + state.state_name + ")")

            # puts together letters that use the same edge (used later)
            blend_transition(state)

            for transition in state.transitions:
                # checks for loops
                if transition.target_state == state:
                    # checks to write the loop above or below, depending on whether its in the top or bottom row
                    if i < len(automaton.states) / 2:
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
                if in_transition(state, transition.target_state):
                    fout.write(
                        "\t edge[bend right] node "
                        "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                        "(" + transition.target_state.state_name + ")\n")
                    continue
                # check for neighbours
                if automaton.states.index(state) == automaton.states.index(transition.target_state) - 1 \
                        or automaton.states.index(state) == automaton.states.index(transition.target_state) + 1:
                    fout.write("\t edge node " +
                               "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                               "(" + transition.target_state.state_name + ")\n")
                    continue

                # normal transitions
                fout.write("\t edge[bend right] node "
                           "{" + ", ".join(str(letter) for letter in transition.letter) + "} " +
                           "(" + transition.target_state.state_name + ")\n")

        fout.write("\n\n\n\n")
        # end of tikz
        fout.write("\\end{tikzpicture}")


if __name__ == '__main__':
    automaton = Automaton("tikz_hazi3")
    draw_states_single_line(automaton)
    draw_transitions_straight_line(automaton)
