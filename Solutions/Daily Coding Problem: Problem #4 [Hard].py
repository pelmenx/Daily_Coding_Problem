# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
# give 3.
#
# You can modify the input array in-place.
#
#
# --------------------------------------------------------------------------------
#
#
def skiped_integer(integer_list):
    integer_list.sort()
    max = 0
    for i in integer_list:
        if i - max > 1:
            return max + 1
        if i > max:
            max = int(i)
    return max + 1


# tests
print(skiped_integer([3, 4, -1, 1]))  # 2
print(skiped_integer([1, 2, 0]))  # 3
print(skiped_integer([-1, -2]))  # 1
print(skiped_integer([3, 4, -1, 1, 1.2, 2.1]))  # 2
print(skiped_integer([]))  # 1
print(skiped_integer([2, 3]))  # 1
