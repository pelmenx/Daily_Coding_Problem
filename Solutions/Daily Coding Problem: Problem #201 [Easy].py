# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an array of arrays of integers, where each array corresponds to a
# row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents
# the triangle:
#
#   1
#  2 3
# 1 5 1
#
#
# We define a path in the triangle to start at the top and go down one row at a
# time to an adjacent value, eventually ending with an entry on the bottom row.
# For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
#
# Write a program that returns the weight of the maximum weight path.
#
#
# --------------------------------------------------------------------------------
#
#
def maximum_weight_path(array):
    def max_weight_path(array_, position=0, sum=0):
        # print(array_)
        if len(array_) == 1:
            yield sum + array_[0][position]
        if len(array_) > 1:
            yield from max_weight_path(array_[1:], position, sum + array_[0][position])
            if len(array_) > 1:
                if position + 1 < len(array_[1]):
                    yield from max_weight_path(array_[1:], position + 1, sum + array_[0][position])

    max_weight = None
    for weight in max_weight_path(array):
        if max_weight is None:
            max_weight = weight
        else:
            if weight > max_weight:
                max_weight = weight
    return max_weight


assert maximum_weight_path([[1], [2, 3], [1, 5, 1]]) == 9
