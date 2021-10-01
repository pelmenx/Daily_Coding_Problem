# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an array of nonnegative integers. Let's say you start at the
# beginning of the array and are trying to advance to the end. You can advance at
# most, the number of steps that you're currently on. Determine whether you can
# get to the end of the array.
#
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1
# -> 3 -> 5, so return true.
#
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
#
#
# --------------------------------------------------------------------------------
#
#
def is_advanceable(array):
    def is_advanceable_inside(array_, position, step):
        if position + 1 == len(array):
            yield
        elif step:
            for i in range(1, step + 1):
                yield from is_advanceable_inside(array_, position + i, array_[position + i])
    for _ in is_advanceable_inside(array, 0, array[0]):
        return True
    return False


assert is_advanceable([1, 3, 1, 2, 0, 1]) is True
assert is_advanceable([1, 2, 1, 0, 0]) is False
