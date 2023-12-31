import re
import numpy as np
from classes.State import State
import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

debug_console_handler = logging.StreamHandler()
debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d')
debug_console_handler.setFormatter(debug_formatter)

info_console_handler = logging.StreamHandler()
info_formatter = logging.Formatter('%(levelname)s: %(message)s')
info_console_handler.setFormatter(info_formatter)

# logger.addHandler(debug_console_handler)
logger.addHandler(info_console_handler)


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
            for i in range(len(automaton.alphabet)):
                current_states1 = [states[0].transitions[i].target_state, states[1].transitions[i].target_state]
                current_states2 = [states[1].transitions[i].target_state, states[0].transitions[i].target_state]

                if current_states1 in bad_states or current_states2 in bad_states:
                    if [states[0], states[1]] not in bad_states:
                        bad_states.append([states[0], states[1]])
                    if [states[1], states[0]] not in bad_states:
                        bad_states.append([states[1], states[0]])

        # remove bad states
        print(good_states)
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
                for i in range(len(automaton.alphabet)):
                    if other_state.transitions[i].target_state == states[0] or other_state.transitions[i].target_state == states[
                        1]:
                        other_state.transitions[i].target_state = new_state

    # remove old states
    for states in good_states:
        if states[0] in automaton.states:
            automaton.states.remove(states[0])
        if states[1] in automaton.states:
            automaton.states.remove(states[1])

    return automaton


def epsilon_closure(automaton):
    pass


def letter_available(state, letter):
    """
    checks if the transition with the letter is available in the state
    :param state: checked state
    :param letter: checked transition letter
    :return: True if the transition is available
    """
    for transition in state.transitions:
        if letter in transition.letter:
            return transition

    logger.debug("Letter {} not available from state {}".format(letter, state.state_name))
    return False


def stack_operation(automaton, transition):
    if transition.stack_out[0] != "E":
        stack_out = re.findall(r'[a-zA-Z]+\d+', transition.stack_out)
        try:
            for elem in stack_out:
                stack = automaton.stack
                removed = automaton.stack.pop()
                if elem != removed:
                    logger.debug(
                        "not able to remove {} from stack {} cause {} != {}".format(elem, stack, elem,
                                                                                    removed))
                    return False
        except IndexError as e:
            logging.error("Stack underflow", str(e))
            return False

    if transition.stack_in[0] == "E":
        return True
    else:
        stack_in = re.findall(r'[a-zA-Z]+\d+', transition.stack_in)

    for elem in stack_in:
        automaton.stack.append(elem)

    return True


# noinspection PyTypeChecker
def possible_word(stack_automaton, word):
    word = list(word)

    # start at the initial state
    current_state = stack_automaton.initial_state

    # check if the automata can go along letter by letter
    while word:
        logger.info("stack: {}".format(stack_automaton.stack))
        # go letter by letter
        letter = word.pop(0)
        transition = letter_available(current_state, letter)
        # check if a transition with that letter exists
        if not transition:
            logger.debug("transition: {}".format(transition))
            return False
        # check if the stack operation of the transition is doable
        if not stack_operation(stack_automaton, transition):
            logger.debug("operation: {}".format(transition))
            return False

        # go to the next state
        current_state = transition.target_state

    # this should be the end of the word
    # check if you are in a final state and the stack is empty
    if current_state.is_final and len(stack_automaton.stack) == 0:
        return True

    # or if you can reach it final state using epsilon transitions
    while True:
        logger.info("stack: {}".format(stack_automaton.stack))
        # same as above but only with epsilon transitions
        transition = letter_available(current_state, "E")
        if not transition:
            break
        if not stack_operation(stack_automaton, transition):
            break
        current_state = transition.target_state

    # final check if you are in a final state and stack is empty
    if current_state.is_final and len(stack_automaton.stack) == 0:
        return True
    return False


if __name__ == '__main__':
    pass
