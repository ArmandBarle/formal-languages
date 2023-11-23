import formal.main


def in_transition(to_state, from_state):
    """
    checks if the to_state is in  from_state's transitions
    :param to_state: state where transition goes to
    :param from_state: state where transition goes from
    :return: boolean if to_state is in from_state transitions
    """
    for transition in from_state.transitions.keys():
        if to_state in from_state.transitions[transition]:
            return True
    return False


def blend_transition(automaton):
    """
    blends transitions that go to the same state with different letters
    :param automaton: automaton of which states are going to be blended
    :return: automaton with blended states
    """
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

    return automaton


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
        fout.write("\t\\path[->]\n")
        for i, state in enumerate(automaton.states):
            fout.write("\t(" + state.state_name + ")")
            for letter in automaton.alphabet:
                if letter not in state.transitions.keys():
                    continue
                for next_state in state.transitions[letter]:

                    # check for double letter edges
                    # TODO

                    # checks for loops
                    if next_state == state:
                        if i < len(automaton.states) / 2:
                            fout.write("\t edge[loop above] node {" + letter + "} (" + next_state.state_name + ")\n")
                            continue
                        else:
                            fout.write("\t edge[loop below] node {" + letter + "} (" + next_state.state_name + ")\n")
                            continue

                    # check for bends
                    if in_transition(state, next_state):
                        fout.write("\t edge[bend right] node {" + letter + "} (" + next_state.state_name + ")\n")
                        continue

                    # normal transitions
                    fout.write("\t edge node {" + letter + "} (" + next_state.state_name + ")\n")

        fout.write("\n\n\n\n")
        # end of tikz
        fout.write("\\end{tikzpicture}")


def draw_transitions_straight_line(automaton):
    with open("tikz_out.txt", 'a+') as fout:
        fout.write("\t\\path[->]\n")
        for i, state in enumerate(automaton.states):
            fout.write("\t(" + state.state_name + ")")
            for letter in automaton.alphabet:
                if letter not in state.transitions.keys():
                    continue
                for next_state in state.transitions[letter]:

                    # check for double letter edges
                    # TODO

                    # checks for loops
                    if next_state == state:
                        if i < len(automaton.states) / 2:
                            fout.write("\t edge[loop above] node {" + letter + "} (" + next_state.state_name + ")\n")
                            continue
                        else:
                            fout.write("\t edge[loop below] node {" + letter + "} (" + next_state.state_name + ")\n")
                            continue

                    # check for bends
                    if in_transition(state, next_state):
                        fout.write("\t edge[bend right] node {" + letter + "} (" + next_state.state_name + ")\n")
                        continue

                    # check for neighbour
                    if automaton.states.index(state) == automaton.states.index(next_state) - 1 \
                            or automaton.states.index(state) == automaton.states.index(next_state) + 1:
                        fout.write("\t edge node {" + letter + "} (" + next_state.state_name + ")\n")
                        continue

                    fout.write("\t edge[bend right] node {" + letter + "} (" + next_state.state_name + ")\n")

        fout.write("\n\n\n\n")
        # end of tikz
        fout.write("\\end{tikzpicture}")


def set_up_transitions(file_name):
    with open(file_name, 'r') as fin:
        for i in range(4):
            fin.readline()
        line = fin.readline()

        transitions = []
        while True:
            if line == "":
                break
            line = fin.readline()


if __name__ == '__main__':
    automaton = formal.main.read_automata("tikz_hazi3")
    automaton = blend_transition(automaton)
    print(automaton)
