# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a circular array, compute its maximum subarray sum in O(n) time. A
# subarray can be empty, and in this case the sum is 0.
#
# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8
# where the 8 is obtained from wrapping around.
#
# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
#
#
# --------------------------------------------------------------------------------
#
#
def max_sum(array):
    sub_array = array[:]
    max_sum = sum(sub_array)
    for i in range(len(array)):
        j = len(array) - 1
        while j > 0:
            sub = []
            for i in range(i, i + j):
                sub += [array[i % len(array)]]
            j -= 1
            if sum(sub) > max_sum:
                max_sum = sum(sub)
                sub_array = sub
    print(sub_array)
    return max_sum


assert max_sum([8, -1, 3, 4]) == 15
assert max_sum([-4, 5, 1, 0]) == 6
