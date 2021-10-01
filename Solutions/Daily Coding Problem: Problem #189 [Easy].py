# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of elements, return the length of the longest subarray where all
# its elements are distinct.
#
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
# subarray of distinct elements is [5, 2, 3, 4, 1].
#
#
# --------------------------------------------------------------------------------
#
#
def distinct_elements(array):
    tmp_dict = {}
    for item in array:
        if item not in tmp_dict:
            tmp_dict[item] = None
    return len(tmp_dict)


assert distinct_elements([5, 1, 3, 5, 2, 3, 4, 1]) == 5
