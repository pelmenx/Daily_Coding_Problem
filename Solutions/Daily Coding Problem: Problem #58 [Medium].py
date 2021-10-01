# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than
# linear time. If the element doesn't exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4
# (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.
#
#
# --------------------------------------------------------------------------------
#
#
def find_position_of_element(array, number, start=None, end=None):
    if end is None:
        end = len(array) - 1
        start = 0
    mid = (end + start) // 2

    if array[mid] == number:
        return mid
    elif array[mid] < number:
        if array[start] >= number:
            return find_position_of_element(array, number, mid + 1, end)
        else:
            return find_position_of_element(array, number, start, mid)
    else:
        if array[start] <= number:
            return find_position_of_element(array, number, start, mid)
        else:
            return find_position_of_element(array, number, mid + 1, end)


print(find_position_of_element([13, 18, 25, 2, 8, 10], 2))
print(find_position_of_element([13, 18, 25, 2, 8, 10], 8))
print(find_position_of_element([25, 2, 8, 10, 13, 18], 8))
print(find_position_of_element([8, 10, 13, 18, 25, 2], 8))
