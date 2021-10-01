# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Given a number represented by a list of digits, find the next greater
# permutation of a number, in terms of lexicographic ordering. If there is not
# greater permutation possible, return the permutation with the lowest
# value/ordering.
#
# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
# return [2,1,3]. The list [3,2,1] should return [1,2,3].
#
# Can you perform the operation without allocating extra memory (disregarding the
# input memory)?
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import permutations


def find_next_permutation(array):
    next_permutation = None
    lowest_value_permutation = None
    for p_ in permutations(array, len(array)):
        p_ = list(p_)
        if p_ > array:
            if not next_permutation:
                next_permutation = p_
            else:
                if array < p_ < next_permutation:
                    next_permutation = p_
        elif p_ < array:
            if not lowest_value_permutation:
                lowest_value_permutation = p_
            else:
                if p_ < lowest_value_permutation:
                    lowest_value_permutation = p_
    if next_permutation:
        return next_permutation
    else:
        return lowest_value_permutation


assert find_next_permutation([1, 2, 3]) == [1, 3, 2]
assert find_next_permutation([1, 3, 2]) == [2, 1, 3]
assert find_next_permutation([3, 2, 1]) == [1, 2, 3]
