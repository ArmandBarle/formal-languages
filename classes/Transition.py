class Transition:
    def __init__(self, letter, target_state):
        self.letter = [letter]
        self.target_state = target_state

    def __str__(self):
        return f"{self.letter} -> {self.target_state.state_name}"

    def add_letter(self, letter):
        self.letter.append(letter)
