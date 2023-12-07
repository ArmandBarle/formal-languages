from tikz.MultilineTikz import MultilineTikz
from tikz.CircularTikz import CircularTikz
from tikz.LineTikz import LineTikz


def choose_drawing_destinations(draw_type):
    print("choose input file from input_automata directory")
    input_file = input("input_automata/").strip()
    print(input_file)
    print("choose output file (default tikz_out.txt)")
    output_file = input("output_automata/").strip()
    if output_file == "":
        output_file = "tikz_out.txt"
    draw_type(input_file, output_file)


def menu():
    print("Hello World!")

    command = None

    try:

        while command != "q":
            print("========================================================")
            print("(f) Formal language algorithms (out of order)\n"
                  "(l) Latex automata generation\n"
                  "(q) Quit")
            print("========================================================")
            command = input("Command: ").strip().lower()

            if command == "f":
                print("algorithm 1")
                print("algorithm 2")
                print("algorithm 3")

            elif command == "l":
                print("(s) Draw automaton in single line (max 6 states)")
                print("(m) Draw automaton in multiline line (max 10 states)")
                print("(c) Draw automaton in circular line (max 14 states)")
                command = input("Command: ").strip().lower()
                if command == "s":
                    choose_drawing_destinations(LineTikz)
                elif command == "m":
                    choose_drawing_destinations(MultilineTikz)
                elif command == "c":
                    choose_drawing_destinations(CircularTikz)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    menu()
