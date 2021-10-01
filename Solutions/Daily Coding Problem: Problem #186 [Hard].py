# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an array of positive integers, divide the array into two subsets such that
# the difference between the sum of the subsets is as small as possible.
#
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}
# , which has a difference of 5, which is the smallest possible difference.
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product
from sys import maxsize


def div_into_two_subsets_with_product(set):
    min_difference = maxsize
    two_subsets = None
    for p_ in product((0, 1), repeat=len(set)):
        first_subset = []
        second_subset = []
        for i, item in enumerate(p_):
            if item:
                first_subset.append(set[i])
            else:
                second_subset.append(set[i])
        first_sum = sum(first_subset)
        second_sum = sum(second_subset)
        if abs(first_sum - second_sum) < min_difference:
            min_difference = abs(first_sum - second_sum)
            two_subsets = (first_subset, second_subset)
    return two_subsets


def div_into_two_subsets_without_product(set):
    def div_into_two_subsets(set1, set2=[]):
        yield (set1, set2)
        for i, item in enumerate(set1):
            yield from div_into_two_subsets(set1[:i] + set1[i + 1:], set2 + [item])
    min_difference = maxsize
    two_subsets = None
    for subsets in div_into_two_subsets(set):
        first_sum = sum(subsets[0])
        second_sum = sum(subsets[1])
        if abs(first_sum - second_sum) < min_difference:
            min_difference = abs(first_sum - second_sum)
            two_subsets = subsets
    return two_subsets


assert div_into_two_subsets_with_product([5, 10, 15, 20, 25]) == ([15, 25], [5, 10, 20])
assert div_into_two_subsets_without_product([5, 10, 15, 20, 25]) == ([15, 25], [5, 10, 20])
