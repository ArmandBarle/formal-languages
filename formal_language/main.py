import formal_language.algorithms as falgs
from classes.Automaton import Automaton
from classes.State import State
from classes.Transition import Transition


def main():
    main_test()


def main_test():
    automaton = Automaton("input_automata/hazi1")
    print((automaton))

    # def test_manual():
    #     test_automaton = Automaton(alphabet={"0", "1"})
    #     q0 = State("q0", is_initial=True, is_final=False)
    #     q1 = State("q1", is_initial=False, is_final=False)
    #     q2 = State("q2", is_initial=False, is_final=True)
    #     q3 = State("q3", is_initial=False, is_final=False)
    #     q4 = State("q4", is_initial=False, is_final=False)
    #     q5 = State("q5", is_initial=False, is_final=False)
    #
    #     q0.add_transition("0", q1)
    #     q0.add_transition("1", q4)
    #     test_automaton.add_state(q0)
    #
    #     q1.add_transition("0", q4)
    #     q1.add_transition("1", q2)
    #     test_automaton.add_state(q1)
    #
    #     q2.add_transition("0", q0)
    #     q2.add_transition("1", q2)
    #     test_automaton.add_state(q2)
    #
    #     q3.add_transition("0", q5)
    #     q3.add_transition("1", q4)
    #     test_automaton.add_state(q3)
    #
    #     q4.add_transition("0", q4)
    #     q4.add_transition("1", q3)
    #     test_automaton.add_state(q4)
    #
    #     q5.add_transition("0", q4)
    #     q5.add_transition("1", q2)
    #     test_automaton.add_state(q5)
    #
    #     print(test_automaton)
    #     minimaization(test_automaton)
    #     print(test_automaton)
    #
    #
    # def test_non_deterministic_non_complete():
    #     test_automata = Automaton(alphabet={"0", "1"})
    #     s0 = State("s0", is_initial=True, is_final=True)
    #     s1 = State("s1", is_initial=False, is_final=False)
    #     s2 = State("s2", is_initial=False, is_final=False)
    #     s3 = State("s3", is_initial=False, is_final=True)
    #
    #     s0.add_transition("1", s1)
    #     test_automata.add_state(s0)
    #
    #     s1.add_transition("1", s3)
    #     s1.add_transition("1", s0)
    #     s1.add_transition("0", s2)
    #     test_automata.add_state(s1)
    #
    #     test_automata.add_state(s2)
    #
    #     s3.add_transition("1", s3)
    #     s3.add_transition("0", s2)
    #     test_automata.add_state(s3)
    #
    #     print(test_automata)
    #     check_determinized(test_automata)
    #     aut1 = completion(test_automata)
    #     print(test_automata)
    #     check_determinized(test_automata)
    #     aut2 = minimaization(aut1)
    #     print(test_automata)
    #
    #     print(check_equivalent(aut1, aut2))
    #
    #
    # def test_determinization():
    #     test_automata = read_automata("input_automata/hazi1")
    #     print(test_automata)
    #     test_automata = minimaization(test_automata)
    #     print(test_automata)
    #
    #
    # def test_hazi1():
    #     test_automata = read_automata("formal/hazi1")
    #     print(test_automata)
    #     test_automata = minimaization(test_automata)
    #     print(test_automata)
    #
    #
    # def test_equivalency():
    #     automata1 = read_automata("input_automata/equivalency1")
    #     automata2 = read_automata("input_automata/equivalency2")
    #     automata3 = read_automata("input_automata/equivalency3")
    #
    #     print(automata1)
    #     print(automata2)
    #     print(check_equivalent(automata1, automata1))
    #     # print(automata3)


if __name__ == '__main__':
    main()
