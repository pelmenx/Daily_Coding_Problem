# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.
#
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1,
# 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
#
# You may also use a list or array to represent a set.
#
#
# --------------------------------------------------------------------------------
#
#
def generate_power_set(set, power_list=[], indicator_list=[], result_list=[]):
    if not set:
        return result_list
    elif not power_list:
        result_list.append([])
        tmp_power_list = set
        tmp_indicator_list = []
        for i in range(0, len(set)):
            tmp_indicator_list.append(i + 1)
        for item in tmp_power_list:
            result_list.append([item])
        return generate_power_set(set, tmp_power_list, tmp_indicator_list)
    elif len(power_list) == 1:
        return result_list
    else:
        tmp_power_list = []
        tmp_indicator_list = []
        for i in range(0, len(power_list)):
            for j in range(indicator_list[i], len(set)):
                if set == power_list:
                    tmp = [power_list[i]]
                else:
                    tmp = power_list[i][:]
                tmp.append(set[j])
                tmp_power_list.append(tmp)
                tmp_indicator_list.append(j + 1)
        result_list.extend(tmp_power_list)
    return generate_power_set(set, tmp_power_list, tmp_indicator_list)


print(generate_power_set([1, 2, 3, 4, 5, 6]))
