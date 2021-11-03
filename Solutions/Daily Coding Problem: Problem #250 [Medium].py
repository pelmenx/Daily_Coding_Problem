# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A cryptarithmetic puzzle is a mathematical game where the digits of some numbers
# are represented by letters. Each letter represents a unique digit.
#
# For example, a puzzle of the form:
#
#   SEND
# + MORE
# --------
#  MONEY
#
#
# may have the solution:
#
# {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
#
#
# Given a three-word puzzle like the one above, create an algorithm that finds a
# solution.
#
#
# --------------------------------------------------------------------------------
#
#
class CryptarithmeticPuzzle(object):
    def __init__(self, string: str):
        self.first_statment = None
        self.second_statment = None
        self.result = None
        self.symbol = None
        self.initialize_puzzle(string)

    def initialize_puzzle(self, string: str) -> None:
        self.result = string.split("=")[1].strip()
        first_part_of_string = string.split("=")[0]
        for i, letter in enumerate(first_part_of_string):
            if not letter.isalpha():
                self.first_statment = first_part_of_string[:i]
                self.second_statment = first_part_of_string[i + 1:]
                self.symbol = first_part_of_string[i]
                break

    def solve_puzzle(self) -> dict | None:
        def make_possible_dict(pointer=0) -> dict:
            if pointer == len(letter_list):
                yield letters_dict
            else:
                for i in possible_digits:
                    if i not in letters_dict.values():
                        if (letter_list[pointer] == self.first_statment[0] or letter_list[pointer] == self.second_statment[0] or letter_list[pointer] == self.result[0]) and i == 0:
                            continue
                        else:
                            letters_dict[letter_list[pointer]] = i
                            yield from make_possible_dict(pointer + 1)
                            letters_dict.pop(letter_list[pointer])

        possible_digits = [x for x in range(0, 10)]
        letter_list = list(set(self.first_statment + self.second_statment + self.result))
        letters_dict = {}
        for dictionary in make_possible_dict():
            first = ""
            second = ""
            result = 0
            for letter in self.first_statment:
                first += str(dictionary[letter])
            for letter in self.second_statment:
                second += str(dictionary[letter])
            for letter in self.result:
                result = result * 10 + dictionary[letter]
            if eval(first + self.symbol + second) == result:
                return dictionary


puzzle = CryptarithmeticPuzzle("SEND+MORE=MONEY")
assert puzzle.solve_puzzle() == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
