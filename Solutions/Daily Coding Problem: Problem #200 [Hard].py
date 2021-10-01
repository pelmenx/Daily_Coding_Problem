# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Let X be a set of n intervals on the real line. We say that a set of points P
# "stabs" X if every interval in X contains at least one point in P. Compute the
# smallest set of points that stabs X.
#
# For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should
# return [4, 9].
#
#
# --------------------------------------------------------------------------------
#
#
def stabs_intervals(intervals):
    def find_all_points(intervals_):
        points_list_ = []
        for interlval_ in intervals_:
            tmp = []
            for i in range(interlval_[0], interlval_[1] + 1):
                tmp.append(i)
            points_list_.append(tmp)
        return points_list_
    all_points_list = find_all_points(intervals)
    result = []
    for i, group in enumerate(all_points_list):
        counter_dict = {}
        stab = group[0]
        number_of_performances = -1
        for number in group:
            counter_dict[number] = 0
            for subgroup in all_points_list[:i] + all_points_list[i + 1:]:
                for subnumber in subgroup:
                    if number == subnumber:
                        counter_dict[number] += 1
                        if counter_dict[number] > number_of_performances:
                            number_of_performances = counter_dict[number]
                            stab = number
        if stab not in result:
            result.append(stab)
    return result


assert stabs_intervals([(1, 4), (4, 5), (7, 9), (9, 12)]) == [4, 9]
