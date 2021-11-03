# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# The ancient Egyptians used to express fractions as a sum of several terms where
# each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18
# + 1 / 468.
#
# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an
# Egyptian fraction.
#
#
# --------------------------------------------------------------------------------
#
#
from fractions import Fraction
import fractions


def egyptian_algorithm(fraction, fractions_list=[], i=2):
    if fraction < 0.0000000000000001:
        return fractions_list
    while True:
        if 1/i <= fraction:
            break
        i += 1
    return egyptian_algorithm(fraction - 1/i, fractions_list+[i], i)


def egyptian_algorithm_fraction(fraction, fractions_list=[], i=2):
    if not fraction:
        return fractions_list
    while True:
        if Fraction(1, i) <= fraction:
            break
        i += 1
    return egyptian_algorithm_fraction(fraction - Fraction(1, i), fractions_list+[Fraction(1, i)], i)


assert egyptian_algorithm(4/13) == [4, 18, 468]
assert egyptian_algorithm_fraction(Fraction(4, 13)) == [
    Fraction(1, 4), Fraction(1, 18), Fraction(1, 468)]
