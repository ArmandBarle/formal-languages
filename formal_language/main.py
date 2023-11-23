import numpy as np








def check_determinized(automaton):
    for state in automaton.states:
        if len(state.transitions) != len(automaton.alphabet):
            print("not determinized")
            return False

        for letter in automaton.alphabet:
            if len(state.transitions[letter]) != 1:
                print("not determinized")
                return False

    print("determinized")
    return True


# def determinization(automaton):
#     determinized_automaton = []
#     checked = [[automaton.initial_state]]
#     state_stack = [automaton.initial_state]
#
#     new_letter = chr(ord(automaton.states[0].state_name[0]) + 1)
#
#     while state_stack:
#         state = state_stack.pop()
#         new_state = State(new_letter + str(len(checked)), is_initial=state.is_initial, is_final=state.is_final)
#
#         if new_state.state_name not in checked:
#             checked.append(new_state.state_name)
#
#         for letter in automaton.alphabet:
#
#     return determinized_automaton


def check_complete(automaton):
    """
    checks if an automaton is complete
    one is complete if each node has an edge with every letter
    :return: true or false
    """
    for state in automaton.states:
        if len(state.transitions) != len(automaton.alphabet):
            print("not complete")
            return False

    print("complete")
    return True


def completion(automaton):
    """
    completes an automaton
    creates a new state for each state in the automaton that has no outgoing edges
    :param automaton: input automaton
    :return: completed automaton
    """
    if check_complete(automaton):
        return automaton
    else:
        trap_state_name = automaton.states[0].state_name[0] + str(len(automaton.states))
        automaton.add_state(State(trap_state_name, is_initial=False, is_final=False))
        for state in automaton.states:
            if len(state.transitions) != len(automaton.alphabet):
                for letter in automaton.alphabet:
                    if letter not in state.transitions:
                        state.add_transition(letter, automaton.states[-1])

    return automaton


def check_equivalent(automaton1, automaton2):
    state_stack = [(automaton1.initial_state, automaton2.initial_state)]
    checked = []
    while state_stack:

        state1, state2 = state_stack.pop()
        checked.append((state1, state2))

        for letter in automaton1.alphabet:
            next_state1 = state1.transitions[letter][0]
            next_state2 = state2.transitions[letter][0]

            if next_state1.is_final != next_state2.is_final:
                return False

            if (next_state1, next_state2) not in state_stack and (next_state1, next_state2) not in checked:
                state_stack.append((next_state1, next_state2))
    return True


def minimaization(automaton):
    """
    minimaizes an automaton
    steps:
    1. check if the automaton is complete
    2. turn automata into matrix
    3. add star to different state combinations

    :return:
    """
    # check if the automaton is complete
    if not check_complete(automaton):
        completion(automaton)

    # if not check_determinized(automaton):
    #     determinization(automaton)

    # create and n*n zeroes matrix where n is the number of states
    star_matrix = np.zeros((len(automaton.states), len(automaton.states)))

    good_states = []
    bad_states = []
    # create the star matrix where there is a 2 if the states are equivalent and 1 if they are not
    for i in range(len(automaton.states)):
        for j in range(len(automaton.states)):
            if i > j:
                state1 = automaton.states[i]
                state2 = automaton.states[j]
                if state1.is_final != state2.is_final:
                    star_matrix[i][j] = 1
                    bad_states.append([state1, state2])
                    bad_states.append([state2, state1])
                else:
                    star_matrix[i][j] = 2
                    good_states.append([state1, state2])

    # checks until there are no changes
    length_of_good_states = len(good_states)
    old_length = 0

    while old_length != length_of_good_states:

        # check every state combination whether they are not equivalent
        for states in good_states:
            for letter in automaton.alphabet:
                current_states1 = [states[0].transitions[letter][0], states[1].transitions[letter][0]]
                current_states2 = [states[1].transitions[letter][0], states[0].transitions[letter][0]]

                if current_states1 in bad_states or current_states2 in bad_states:
                    if [states[0], states[1]] not in bad_states:
                        bad_states.append([states[0], states[1]])
                    if [states[1], states[0]] not in bad_states:
                        bad_states.append([states[1], states[0]])

        # remove bad states
        for states in good_states:
            if states in bad_states:
                good_states.remove(states)

        # for states in bad_states:
        #     print(states[0].state_name, states[1].state_name)
        # print("-----------------------------------------------")

        old_length = length_of_good_states
        length_of_good_states = len(good_states)

    # add new combined states
    for states in good_states:
        new_state_name = states[0].state_name + states[1].state_name
        new_initial = states[0].is_initial or states[1].is_initial
        new_state = State(new_state_name, is_initial=new_initial, is_final=states[0].is_final)
        new_state.transitions = states[0].transitions
        automaton.add_state(new_state)

        # change the transitions from the old states to the new states
        for other_state in automaton.states:
            if other_state.state_name != states[0].state_name or other_state.state_name != states[1].state_name:
                for letter in automaton.alphabet:
                    if other_state.transitions[letter][0] == states[0] or other_state.transitions[letter][0] == states[
                        1]:
                        other_state.transitions[letter] = [new_state]

    # remove old states
    for states in good_states:
        if states[0] in automaton.states:
            automaton.states.remove(states[0])
        if states[1] in automaton.states:
            automaton.states.remove(states[1])

    return automaton


def epsilon_closure(automaton):
    pass


def read_automata(filename):
    # open a file using with
    with open(filename, "r") as file:

        states_names = file.readline()
        states_names = states_names.split()

        # Creating automaton
        alphabet = file.readline()
        alphabet = alphabet.split()
        automaton = Automaton(alphabet=set(alphabet))

        initial_state = file.readline().strip()
        final_states = file.readline()
        final_states = final_states.split()

        # Creating states
        states = []
        for state_name in states_names:
            state = State(state_name, is_initial=initial_state == state_name, is_final=state_name in final_states)
            states.append(state)

        # Adding transitions
        while True:
            line = file.readline()
            if line == "":
                break
            line = line.split()
            for state in states:
                if state.state_name == line[0]:
                    state.add_transition(line[1], states[int(line[2][-1])])

        for state in states:
            automaton.add_state(state)

        return automaton


def test_easy():
    test_automaton = read_automata("input_automata/minimization_test1")
    minimaization(test_automaton)
    print(test_automaton)

    check_determinized(test_automaton)


def test_manual():
    test_automaton = Automaton(alphabet={"0", "1"})
    q0 = State("q0", is_initial=True, is_final=False)
    q1 = State("q1", is_initial=False, is_final=False)
    q2 = State("q2", is_initial=False, is_final=True)
    q3 = State("q3", is_initial=False, is_final=False)
    q4 = State("q4", is_initial=False, is_final=False)
    q5 = State("q5", is_initial=False, is_final=False)

    q0.add_transition("0", q1)
    q0.add_transition("1", q4)
    test_automaton.add_state(q0)

    q1.add_transition("0", q4)
    q1.add_transition("1", q2)
    test_automaton.add_state(q1)

    q2.add_transition("0", q0)
    q2.add_transition("1", q2)
    test_automaton.add_state(q2)

    q3.add_transition("0", q5)
    q3.add_transition("1", q4)
    test_automaton.add_state(q3)

    q4.add_transition("0", q4)
    q4.add_transition("1", q3)
    test_automaton.add_state(q4)

    q5.add_transition("0", q4)
    q5.add_transition("1", q2)
    test_automaton.add_state(q5)

    print(test_automaton)
    minimaization(test_automaton)
    print(test_automaton)


def test_non_deterministic_non_complete():
    test_automata = Automaton(alphabet={"0", "1"})
    s0 = State("s0", is_initial=True, is_final=True)
    s1 = State("s1", is_initial=False, is_final=False)
    s2 = State("s2", is_initial=False, is_final=False)
    s3 = State("s3", is_initial=False, is_final=True)

    s0.add_transition("1", s1)
    test_automata.add_state(s0)

    s1.add_transition("1", s3)
    s1.add_transition("1", s0)
    s1.add_transition("0", s2)
    test_automata.add_state(s1)

    test_automata.add_state(s2)

    s3.add_transition("1", s3)
    s3.add_transition("0", s2)
    test_automata.add_state(s3)

    print(test_automata)
    check_determinized(test_automata)
    aut1 = completion(test_automata)
    print(test_automata)
    check_determinized(test_automata)
    aut2 = minimaization(aut1)
    print(test_automata)

    print(check_equivalent(aut1, aut2))


def test_determinization():
    test_automata = read_automata("input_automata/hazi1")
    print(test_automata)
    test_automata = minimaization(test_automata)
    print(test_automata)


def test_hazi1():
    test_automata = read_automata("formal/hazi1")
    print(test_automata)
    test_automata = minimaization(test_automata)
    print(test_automata)


def test_equivalency():
    automata1 = read_automata("input_automata/equivalency1")
    automata2 = read_automata("input_automata/equivalency2")
    automata3 = read_automata("input_automata/equivalency3")

    print(automata1)
    print(automata2)
    print(check_equivalent(automata1, automata1))
    # print(automata3)


if __name__ == '__main__':
    test_hazi1()
