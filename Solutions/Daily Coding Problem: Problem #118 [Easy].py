# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a sorted list of integers, square the elements and give the output in
# sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
#
#
# --------------------------------------------------------------------------------
#
#
def square_list(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        if abs(array[left]) >= array[right]:
            tmp = array[left] * array[left]
            array.pop(left)
            array.insert(right, tmp)
            right -= 1
        elif abs(array[left]) < array[right]:
            array[right] = array[right] * array[right]
            right -= 1
    return array


assert square_list([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]

assert square_list([0, 1, 2, 3, 4]) == [0, 1, 4, 9, 16]

assert square_list([-5, -4, -3, -2, -1]) == [1, 4, 9, 16, 25]
