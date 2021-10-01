# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a list of integers S and a target number k, write a function that returns
# a subset of S that adds up to k. If such a subset cannot be made, then return
# null.
#
# Integers can appear more than once in the list. You may assume all numbers in
# the list are positive.
#
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
# since it sums up to 24.
#
#
# --------------------------------------------------------------------------------
#
#
def find_subset_up_to_k(set, k, path=[]):
    if not k:
        return path
    for i, item in enumerate(set):
        subset = find_subset_up_to_k(set[:i] + set[i + 1:], k - item, path + [item])
        if subset:
            return subset
    return None


print(find_subset_up_to_k([12, 1, 61, 5, 9, 2], 24))
