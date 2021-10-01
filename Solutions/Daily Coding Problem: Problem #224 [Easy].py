# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a sorted array, find the smallest positive integer that is not the sum of
# a subset of the array.
#
# For example, for the input [1, 2, 3, 10], you should return 7.
#
# Do this in O(N) time.
#
#
# --------------------------------------------------------------------------------
#
#
def find_the_smallest(array):
    min_positive_integer = 1
    for item in array:
        if item > min_positive_integer:
            break
        else:
            min_positive_integer += item
    return min_positive_integer


assert find_the_smallest([1, 2, 3, 10]) == 7
