# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of integers where every integer occurs three times except for one
# integer, which only occurs once, find and return the non-duplicated integer.
#
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
# return 19.
#
# Do this in O(N) time and O(1) space.
#
#
# --------------------------------------------------------------------------------
#
#
def find_uniqe_integer(arr):
    a = base_2(0)
    for integer in arr:
        ineger_base_2 = base_2(integer)
        if len(a) < len(ineger_base_2):
            for i in range(len(ineger_base_2) - len(a)):
                a.append(0)
        if len(a) > len(ineger_base_2):
            for i in range(len(a) - len(ineger_base_2)):
                ineger_base_2.append(0)
        tmp = []
        for i in range(len(a)):
            tmp.append((a[i] + ineger_base_2[i]) % 3)
        a = tmp.copy()
        tmp.clear()
    result = 0
    for i in range(len(a) - 1, -1, -1):
        result += a[i] * 2 ** i
    return result


def base_2(number, base_2_integer=[]):
    if number < 2:
        base_2_integer.append(number)
        tmp = base_2_integer.copy()
        base_2_integer.clear()
        return tmp
    dev = int(number / 2)
    modulo = number % 2
    base_2_integer.append(modulo)
    return base_2(dev)


print(find_uniqe_integer([6, 1, 3, 3, 3, 6, 6]))
print(find_uniqe_integer([13, 19, 13, 13]))
