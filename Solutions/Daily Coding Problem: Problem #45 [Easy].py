# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
# uniform probability, implement a function rand7() that returns an integer from 1
# to 7 (inclusive).
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    result = rand5() * 5 + rand5() - 5
    if result < 22:
        result = result % 7 + 1
    else:
        return rand7()
    return result


print(rand7())
