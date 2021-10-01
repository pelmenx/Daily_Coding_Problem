# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# You are given an array of non-negative integers that represents a
# two-dimensional elevation map where each element is unit-width wall and the
# integer is the height. Suppose it will rain and all spots between two walls get
# filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1)
# space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the
# middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
# the second, and 3 in the fourth index (we cannot hold 5 since it would run off
# to the left), so we can trap 8 units of water.
#
#
# --------------------------------------------------------------------------------
#
#
def capacity_trapped_water(input):
    water_capacity = 0
    left_point = 0
    right_point = len(input) - 1
    left_max_height = 0
    right_max_height = 0
    while left_point < right_point:
        if input[left_point] < input[right_point]:
            if input[left_point] > left_max_height:
                left_max_height = input[left_point]
            else:
                water_capacity += left_max_height - input[left_point]
            left_point += 1
        else:
            if input[right_point] > right_max_height:
                right_max_height = input[right_point]
            else:
                water_capacity += right_max_height - input[right_point]
            right_point -= 1
    return water_capacity


print(capacity_trapped_water([1, 3, 0, 1, 3, 10, 0, 10, 0, 5]))
print(capacity_trapped_water([3, 0, 1, 3, 0, 5]))
print(capacity_trapped_water([3, 0, 1, 3]))
print(capacity_trapped_water([3, 0, 1]))
print(capacity_trapped_water([1, 3, 0]))
print(capacity_trapped_water([1, 3]))
print(capacity_trapped_water([1]))
print(capacity_trapped_water([]))
