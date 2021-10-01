# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by
# multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's
# -10 * -10 * 5.
#
# You can assume the list has at least three integers.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize
from itertools import product


def find_the_largest_product(array):
    largest_product = -maxsize
    for product_ in product((0, 1), repeat=len(array)):
        if sum(product_) == 3:
            value = 1
            for item, rank in zip(array, product_):
                if rank != 0:
                    value *= item
            if value > largest_product:
                largest_product = value
    return largest_product


assert find_the_largest_product([-10, -10, 5, 2]) == 500
