# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an array of length n + 1 whose elements belong to the set {1, 2,
# ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in
# linear time and space.
#
#
# --------------------------------------------------------------------------------
#
#
def find_duplicate(array, n):
    if len(array) - 1 == n:
        expected_sum = ((1 + n) * n / 2)
        real_sum = sum(array)
        return real_sum - expected_sum


assert find_duplicate([1, 1, 2], 2) == 1
assert find_duplicate([1, 2, 3, 3], 3) == 3
assert find_duplicate([1, 2, 3, 4, 3], 4) == 3
