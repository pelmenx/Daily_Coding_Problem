# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an array of numbers, find the maximum sum of any contiguous subarray of
# the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be
# 137, since we would take elements 42, 14, -5, and 86.
#
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not
# take any elements.
#
# Do this in O(N) time.
#
#
# --------------------------------------------------------------------------------
#
#
def max_subset(set):
    if not set:
        return 0
    current_max = 0
    final_max = 0
    for item in set:
        current_max = max(item, current_max + item)
        final_max = max(final_max, current_max)
    return final_max


print(max_subset([34, -50, 42, 14, -5, 86]))
print(max_subset([-5, -1, -8, -9]))
