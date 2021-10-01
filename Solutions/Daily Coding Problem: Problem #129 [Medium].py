# Good morning! Here's your coding interview problem for today.
#
# Given a real number n, find the square root of n. For example, given n = 9,
# return 3.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize
from math import sqrt, exp, log


def square_root(n):
    x = 1
    while True:
        nx = (x + n / x) / 2
        if (abs(x - nx) < 1 / maxsize):
            break
        x = nx
    return x


print(square_root(4.4))
print(sqrt(4.4))
print(4.4 ** (1 / 2))
print(pow(4.4, (1 / 2)))
print(exp(log(4.4) / 2))
