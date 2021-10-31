# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# One way to unlock an Android phone is through a pattern of swipes across a 1-9
# keypad.
#
# For a pattern to be valid, it must satisfy the following:
#
#  * All of its keys must be distinct.
#  * It must not connect two keys by jumping over a third key, unless that key has
#    already been used.
#
# For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
#
# Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
#
#
# --------------------------------------------------------------------------------
#
#

from collections.abc import Iterable


class Android_Keypad:
    def __init__(self):
        self.password = []
        self.digits_used = set()
        self.invalid_pairs = {(1, 7): 4,
                              (1, 9): 5,
                              (1, 3): 2,
                              (2, 8): 5,
                              (3, 1): 2,
                              (3, 7): 5,
                              (3, 9): 6,
                              (4, 6): 5,
                              (6, 4): 5,
                              (7, 9): 8,
                              (7, 3): 5,
                              (7, 1): 4,
                              (8, 2): 5,
                              (9, 3): 6,
                              (9, 1): 5,
                              (9, 7): 8}

    def add_digit(self, digit: int):
        self.password.append(digit)
        self.digits_used.add(digit)

    def remove_digit(self, digit: int):
        self.password.pop()
        self.digits_used.remove(digit)


def generate_passwords(n: int, keypad: Android_Keypad) -> int | None:
    if n < 1 or n > 9:
        return None

    def generate_possible_passwords(start: int) -> Iterable:
        if len(keypad.password) == n:
            yield
        else:
            for end in range(1, 10):
                if end not in keypad.digits_used:
                    if (start, end) in keypad.invalid_pairs:
                        if keypad.invalid_pairs[(start, end)] in keypad.digits_used:
                            keypad.add_digit(end)
                            yield from generate_possible_passwords(end)
                            keypad.remove_digit(end)
                    else:
                        keypad.add_digit(end)
                        yield from generate_possible_passwords(end)
                        keypad.remove_digit(end)

    number_of_possible_passports = 0
    for i in range(1, 10):
        keypad.add_digit(i)
        for _ in generate_possible_passwords(start=i):
            number_of_possible_passports += 1
        keypad.remove_digit(i)
    return number_of_possible_passports


KEYPAD = Android_Keypad()
assert generate_passwords(0, KEYPAD) is None
assert generate_passwords(1, KEYPAD) == 9
assert generate_passwords(2, KEYPAD) == 56
assert generate_passwords(3, KEYPAD) == 320
assert generate_passwords(4, KEYPAD) == 1624
assert generate_passwords(5, KEYPAD) == 7152
assert generate_passwords(6, KEYPAD) == 26016
assert generate_passwords(7, KEYPAD) == 72912
assert generate_passwords(8, KEYPAD) == 140704
assert generate_passwords(9, KEYPAD) == 140704
assert generate_passwords(10, KEYPAD) is None
