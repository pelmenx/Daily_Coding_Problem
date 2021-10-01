# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
# uniform probability, implement a function rand5() that returns an integer from 1
# to 5 (inclusive).
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def rand7():
    return randint(1, 7)


def rand5():
    result = rand7() * 7 + rand7() - 7
    if result < 45:
        result = result % 7 + 1
    else:
        return rand5()
    return result


rand5()
