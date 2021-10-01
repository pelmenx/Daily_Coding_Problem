# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a positive integer n, find the smallest number of squared integers which
# sum to n.
#
# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
#
# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def number_of_squared_integers(n, counter=0):
    def counting(sum=0, counter=0):
        if sum == n:
            yield counter
        elif sum > n:
            return
        elif counter > min:
            return
        else:
            for i in range(int((n - sum) ** 0.5), 0, -1):
                yield from counting(sum + i ** 2, counter + 1)
    min = maxsize
    for counter_ in counting():
        if counter_ < min:
            min = counter_
    print(min)
    return min


assert number_of_squared_integers(13) == 2
assert number_of_squared_integers(27) == 3
assert number_of_squared_integers(1231) == 4
