# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def GCD(array):
    denominators_dics = {}
    for item in array:
        tmp_item = abs(item)
        tmp_list = []
        while tmp_item > 1:
            i = 2
            while i <= tmp_item:
                if tmp_item % i == 0:
                    tmp_item /= i
                    tmp_list.append(i)
                    break
                i += 1
        denominators_dics[item] = tmp_list
    min_lenght = maxsize
    min_value = None
    values = denominators_dics.items()
    for item in values:
        if len(item[1]) < min_lenght:
            min_lenght = len(item[1])
            min_value = item
    result = 1
    for value in min_value[1]:
        check = True
        for key in denominators_dics.keys():
            if key != min_value[0]:
                if value not in denominators_dics[key]:
                    check = False
                    break
        if check:
            result *= value
            for key in denominators_dics.keys():
                if key != min_value[0]:
                    tmp = denominators_dics[key]
                    tmp.remove(value)
                    denominators_dics[key] = tmp
    return result


assert GCD([42, 56, 14]) == 14
assert GCD([5, 15, 20]) == 5
assert GCD([1, 2, 3]) == 1
assert GCD([-42, -56, -14]) == 14
