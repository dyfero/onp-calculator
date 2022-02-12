def __increment_bracket__():
    Bracket.brackets_counter = Bracket.brackets_counter + 1


def __decrement_bracket__():
    Bracket.brackets_counter = Bracket.brackets_counter - 1


def __clear_bracket_counter__():
    Bracket.brackets_counter = 0


class Bracket:
    brackets_counter = 0
