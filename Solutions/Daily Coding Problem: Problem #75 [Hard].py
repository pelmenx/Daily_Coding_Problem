# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an array of numbers, find the length of the longest increasing subsequence
# in the array. The subsequence does not necessarily have to be contiguous.
#
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7,
# 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product


def longest_increasing_subsequence(array):
    largest_subsequence = 0
    for product_ in product((0, 1), repeat=len(array)):
        tmp_array = []
        check = True
        for p, item in zip(product_, array):
            if p == 1:
                if len(tmp_array) > 0:
                    if item > tmp_array[-1]:
                        tmp_array.append(item)
                    else:
                        check = False
                        break
                else:
                    tmp_array.append(item)
        if check:
            if len(tmp_array) > largest_subsequence:
                largest_subsequence = len(tmp_array)

    return largest_subsequence


assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
