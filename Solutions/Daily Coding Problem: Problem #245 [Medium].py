# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yelp.
#
# You are given an array of integers, where each element represents the maximum
# number of steps that can be jumped going forward from that element. Write a
# function to return the minimum number of jumps you must take in order to get
# from the start to the end of the array.
#
# For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the
# optimal solution involves jumping from 6 to 5, and then from 5 to 9.
#
#
# --------------------------------------------------------------------------------
#
#
def find_number_of_steps(array: list[int]) -> int:
    def find_min_number_of_steps_inside(position, number_of_steps=0):
        if number_of_steps >= min_number_of_steps:
            return
        if position == len(array) - 1:
            yield number_of_steps
        for i in range(1, array[position] + 1):
            if position + i < len(array):
                yield from find_min_number_of_steps_inside(position + i, number_of_steps + 1)
    min_number_of_steps = len(array) + 1
    for step_number in find_min_number_of_steps_inside(0):
        if step_number < min_number_of_steps:
            min_number_of_steps = step_number
    return min_number_of_steps if min_number_of_steps <= len(array) else None


assert find_number_of_steps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
assert find_number_of_steps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
assert find_number_of_steps([1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) is None
