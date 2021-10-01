# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Google.
#
# Given an integer n and a list of integers l, write a function that randomly
# generates a number from 0 to n-1 that isn't in l (uniform).
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def random_number(n, array):
    number = randint(0, n - 1)
    if number in array:
        return random_number(n, array)
    return number


print(random_number(5, [3]))
