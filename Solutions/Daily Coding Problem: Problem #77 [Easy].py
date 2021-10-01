# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given a list of possibly overlapping intervals, return a new list of intervals
# where all overlapping intervals have been merged.
#
# The input list is not necessarily ordered in any way.
#
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1,
# 3), (4, 10), (20, 25)].
#
#
# --------------------------------------------------------------------------------
#
#
def merged_intervals(array, new_array=None):
    if array == new_array:
        return array
    merged_intervals_list = []
    for interval in array:
        if not merged_intervals_list:
            merged_intervals_list.append(interval)
        else:
            check = True
            for i in range(len(merged_intervals_list)):
                if interval[0] <= merged_intervals_list[i][0] <= merged_intervals_list[i][1] <= interval[1]:
                    merged_intervals_list[i] = interval
                    check = False
                elif merged_intervals_list[i][0] <= interval[0] <= merged_intervals_list[i][1] <= interval[1]:
                    merged_intervals_list[i] = (merged_intervals_list[i][0], interval[1])
                    check = False
                elif interval[0] <= merged_intervals_list[i][0] <= interval[1] <= merged_intervals_list[i][1]:
                    merged_intervals_list[i] = (interval[0], merged_intervals_list[i][1])
                    check = False
            if check:
                merged_intervals_list.append(interval)
    return merged_intervals(merged_intervals_list, array)


assert merged_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]

assert merged_intervals([(1, 3), (5, 8), (4, 10), (20, 25), (6, 12)]) == [(1, 3), (4, 12), (20, 25)]

assert merged_intervals([(1, 3), (5, 8), (0, 10)]) == [(0, 10)]

assert not merged_intervals([])
