# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by LinkedIn.
#
# Given a string, return whether it represents a number. Here are the different
# kinds of numbers:
#
#  * "10", a positive integer
#  * "-10", a negative integer
#  * "10.1", a positive real number
#  * "-10.1", a negative real number
#  * "1e5", a number in scientific notation
#
# And here are examples of non-numbers:
#
#  * "a"
#  * "x 1"
#  * "a -2"
#  * "-"
#
#
# --------------------------------------------------------------------------------
#
#
from re import match


def is_match(string):
    result = match(r"^-?\d+\.?[A-Za-z]?\d*$", string)
    if result:
        return True
    return False


print(is_match("10"))
print(is_match("-10"))
print(is_match("10.1"))
print(is_match("-10.1"))
print(is_match("1e5"))
print(is_match("a"))
print(is_match("x 1"))
print(is_match("a -2"))
print(is_match("-"))
