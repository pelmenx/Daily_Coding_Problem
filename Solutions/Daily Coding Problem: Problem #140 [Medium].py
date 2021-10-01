# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an array of integers in which two elements appear exactly once and all
# other elements appear exactly twice, find the two elements that appear only
# once.
#
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The
# order does not matter.
#
# Follow-up: Can you do this in linear time and constant space?
#
#
# --------------------------------------------------------------------------------
#
#
def find_two_unique_number(array):
    xor = 0
    for number in array:
        xor ^= number

    xor = xor & -xor

    number_1 = 0
    number_2 = 0

    for number in array:
        if number & xor:
            number_1 ^= number
            print("Number1", number_1)
        else:
            number_2 ^= number
            print("Number2", number_2)


find_two_unique_number([2, 4, 6, 8, 10, 2, 6, 10])
