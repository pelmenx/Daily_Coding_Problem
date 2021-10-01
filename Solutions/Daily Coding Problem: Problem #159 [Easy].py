# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string, return the first recurring character in it, or null if there is
# no recurring character.
#
# For example, given the string "acbbac", return "b". Given the string "abcdef",
# return null.
#
#
# --------------------------------------------------------------------------------
#
#
def recurring_character(string):
    if len(string) > 1:
        for letter_1, letter_2 in zip(string[:-1], string[1:]):
            if letter_1 == letter_2:
                return letter_1


assert recurring_character("acbbac") == "b"
assert recurring_character("abcdef") is None
