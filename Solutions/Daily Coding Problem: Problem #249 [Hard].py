# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Salesforce.
#
# Given an array of integers, find the maximum XOR of any two elements.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def find_max_xor(array: list[int]) -> int:
    max_xor = -maxsize
    for i, item1 in enumerate(array):
        for item2 in array[i + 1:]:
            max_xor = max(max_xor, item1 ^ item2)
    return max_xor


assert find_max_xor([1, 2, 3, 4]) == 7
