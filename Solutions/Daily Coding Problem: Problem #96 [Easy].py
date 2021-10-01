# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a number in the form of a list of digits, return all possible
# permutations.
#
# For example, given [1,2,3], return
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
#
#
# --------------------------------------------------------------------------------
#
#
def permutation(array):
    def permutation_inside(array_1, array_2):
        if not array_2:
            yield array_1
        for j, letter_ in enumerate(array_2):
            yield from permutation_inside(array_1 + [letter_], array_2[:j] + array_2[j + 1:])
    permutation_list = []
    for i, letter in enumerate(array):
        for array_ in permutation_inside([letter], array[:i] + array[i + 1:]):
            permutation_list.append(array_)
    return permutation_list


assert permutation([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
