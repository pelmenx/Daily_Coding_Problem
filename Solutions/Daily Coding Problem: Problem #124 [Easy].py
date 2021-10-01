# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# You have n fair coins and you flip them all at the same time. Any that come up
# tails you set aside. The ones that come up heads you flip again. How many rounds
# do you expect to play before only one coin remains?
#
# Write a function that, given n, returns the number of rounds you'd expect to
# play until one coin remains.
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def number_of_rounds(n):
    round = 0
    while n > 1:
        tail = randint(0, 1)
        if tail == 0:
            n -= 1
        round += 1
    return round


print(number_of_rounds(5))
