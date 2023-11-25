from classes.Automaton import Automaton
from classes.StackAutomaton import StackAutomaton
from algorithms import check_equivalent, minimaization, possible_word


def main():
    test_stack_automaton()


def test_stack_automaton():
    stack_automaton = StackAutomaton("input_automata/stack_automaton.txt")
    print(stack_automaton)
    print(possible_word(stack_automaton, "aabb"))


def main_test():
    automaton = Automaton("input_automata/hazi1")
    print((automaton))


def test_hazi1():
    test_automata = Automaton("input_automata/hazi1")
    print(test_automata)
    test_automata = minimaization(test_automata)
    print(test_automata)


def test_equivalency():
    automata1 = Automaton("input_automata/equivalency1")
    automata2 = Automaton("input_automata/equivalency2")
    automata3 = Automaton("input_automata/equivalency3")

    print(automata1)
    print(automata2)
    print(check_equivalent(automata1, automata1))
    # print(automata3)


if __name__ == '__main__':
    main()
