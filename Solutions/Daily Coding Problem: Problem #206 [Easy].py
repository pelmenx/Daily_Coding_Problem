# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# A permutation can be specified by an array P, where P[i] represents the location
# of the element at i in the permutation. For example, [2, 1, 0] represents the
# permutation where elements at the index 0 and 2 are swapped.
#
# Given an array and a permutation, apply the permutation to the array. For
# example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return
# ["c", "b", "a"].
#
#
# --------------------------------------------------------------------------------
#
#
def permutation(array, array_p):
    permutation_list = [None] * len(array)
    for item, position in zip(array, array_p):
        permutation_list[position] = item
    return permutation_list


assert permutation(["a", "b", "c"], [2, 1, 0]) == ['c', 'b', 'a']
