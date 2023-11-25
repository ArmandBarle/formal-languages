import numpy as np

from classes.Automaton import Automaton
from classes.State import State


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


def check_complete(automaton):
    """
    checks if an automaton is complete
    one is complete if each node has an edge with every letter
    :return: true or false
    """
    for state in automaton.states:
        count = 0
        for transition in state.transitions:
            count += len(transition.letter)
        if count != len(automaton.alphabet):
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


if __name__ == '__main__':
    pass
