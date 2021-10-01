# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and the
# Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
#
#
# --------------------------------------------------------------------------------
#
#
def segregation(array):
    pointer = 0
    right = len(array) - 1
    left = 0
    while pointer <= right:
        if array[pointer] == "R":
            if pointer == left:
                pointer += 1
            else:
                tmp_1 = array[pointer]
                tmp_2 = array[left]
                array[pointer] = tmp_2
                array[left] = tmp_1
                left += 1
        elif array[pointer] == "B":
            if pointer == right:
                pointer += 1
            else:
                tmp_1 = array[pointer]
                tmp_2 = array[right]
                array[pointer] = tmp_2
                array[right] = tmp_1
                right -= 1
        else:
            pointer += 1
    return array


print(segregation(['G', 'R']))
print(segregation(['G', 'B', 'R']))
print(segregation(['B', 'G', 'R']))
print(segregation(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
