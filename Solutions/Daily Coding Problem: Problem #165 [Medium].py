# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of integers, return a new array where each element in the new
# array is the number of smaller elements to the right of that element in the
# original input array.
#
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
#
#  * There is 1 smaller element to the right of 3
#  * There is 1 smaller element to the right of 4
#  * There are 2 smaller elements to the right of 9
#  * There is 1 smaller element to the right of 6
#  * There are no smaller elements to the right of 1
#
#
# --------------------------------------------------------------------------------
#
#
def number_of_smallest_elements(array):
    number_of_smallest_elements_list = []
    for i, item in enumerate(array):
        count = 0
        for item_ in array[i + 1:]:
            if item > item_:
                count += 1
        number_of_smallest_elements_list.append(count)
    return number_of_smallest_elements_list


assert number_of_smallest_elements([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
