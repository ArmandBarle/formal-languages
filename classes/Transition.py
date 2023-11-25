class Transition:
    def __init__(self, letter, to_state):
        self.letter = [letter]
        self.to_state = to_state

    def __str__(self):
        return f"{self.letter} -> {self.to_state.state_name}"

    def add_letter(self, letter):
        self.letter.append(letter)
