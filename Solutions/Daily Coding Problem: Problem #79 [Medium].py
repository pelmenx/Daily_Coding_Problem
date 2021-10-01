# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an array of integers, write a function to determine whether the array
# could become non-decreasing by modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true, since we can
# modify the 10 into a 1 to make the array non-decreasing.
#
# Given the array [10, 5, 1], you should return false, since we can't modify any
# one element to get a non-decreasing array.
#
#
# --------------------------------------------------------------------------------
#
#
def decreasing_array(array):
    count = 0
    i = 0
    j = 1
    while i < len(array) and j < len(array):
        if array[i] >= array[j]:
            i += 1
            j += 1
        else:
            count += 1
            if count > 1:
                return False
            j += 1
    if count == 1:
        return True
    else:
        return False


assert decreasing_array([10, 5, 7]) is True
assert decreasing_array([10, 5, 1]) is False
assert decreasing_array([10, 50, 30]) is False
