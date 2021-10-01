# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to
# you beforehand. Find the minimum element in O(log N) time. You may assume the
# array does not contain duplicates.
#
# For example, given [5, 7, 10, 3, 4], return 3.
#
#
# --------------------------------------------------------------------------------
#
#
def find_mininimum_element(array):
    if len(array) == 1:
        return array[0]
    start = 0
    end = len(array) - 1
    mid = int((start + end) / 2)
    if array[start] < array[end]:
        if array[start] < array[mid]:
            return array[start]
        else:
            return find_mininimum_element(array[start:mid + 1])
    else:
        if array[mid] < array[end]:
            return array[mid]
        else:
            return find_mininimum_element(array[mid + 1:end + 1])


assert find_mininimum_element([5, 7, 10, 3, 4]) == 3
assert find_mininimum_element([4, 5, 7, 10, 3]) == 3
assert find_mininimum_element([3, 4, 5, 7, 10]) == 3
