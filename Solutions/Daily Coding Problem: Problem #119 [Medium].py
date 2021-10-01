# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a set of closed intervals, find the smallest set of numbers that covers
# all the intervals. If there are multiple smallest sets, return any of them.
#
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
# numbers that covers all these intervals is {3, 6}.
#
#
# --------------------------------------------------------------------------------
#
#
def find_interval(array_):
    def check_next_interval(array):
        if len(array) <= 1:
            return array[0]
        else:
            if array[1][1] >= array[0][1] >= array[1][0]:
                tmp = [array[0][1], array[0][1]]
            elif array[0][1] < array[1][0]:
                tmp = [array[0][0], array[1][0]]
            elif array_[0][0] <= array_[1][0] <= array_[1][1] <= array_[0][1]:
                tmp = [array_[1][0], array_[1][1]]
        return check_next_interval([tmp] + array[2:])
    array_.sort()
    if len(array_) == 1:
        return array_
    else:
        if array_[1][1] >= array_[0][1] >= array_[1][0]:
            tmp = [array_[0][1], array_[0][1]]
        elif array_[0][1] < array_[1][0]:
            tmp = [array_[0][1], array_[1][0]]
        elif array_[0][0] <= array_[1][0] <= array_[1][1] <= array_[0][1]:
            tmp = [array_[1][0], array_[1][1]]
        return check_next_interval([tmp] + array_[2:])


assert find_interval([[0, 3], [2, 6], [3, 4], [6, 9]]) == [3, 6]
assert find_interval([[-3, -2], [0, 3], [2, 6], [3, 4], [6, 9]]) == [-2, 6]
assert find_interval([[1, 10], [2, 9]]) == [2, 9]
