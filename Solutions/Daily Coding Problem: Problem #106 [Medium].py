# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Pinterest.
#
# Given an integer list where each number represents the number of hops you can
# make, determine whether you can reach to the last index starting at index 0.
#
# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
#
#
# --------------------------------------------------------------------------------
#
#
def is_road(array):
    def check(i):
        if i == len(array) - 1:
            return True
        elif i > len(array):
            return False
        elif array[i] == 0:
            return False
        else:
            return check(i + array[i])
    return check(0)


assert is_road([2, 0, 1, 0]) is True
assert is_road([1, 1, 0, 1]) is False
