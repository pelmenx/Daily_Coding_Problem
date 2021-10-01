# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Gray code [https://en.wikipedia.org/wiki/Gray_code] is a binary code where each
# successive value differ in only one bit, as well as when wrapping around. Gray
# code is common in hardware so that we don't see temporary spurious values during
# transitions.
#
# Given a number of bits n, generate a possible gray code for it.
#
# For example, for n = 2, one gray code would be [00, 01, 11, 10].
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product


def gray_code_with_product(n):
    result_list = []
    for p_ in product(('0', '1'), repeat=n):
        result_list.append(''.join(p_))
    return result_list


def gray_code_without_product(n):
    def gray_code(str):
        if len(str) == n:
            yield str
            return
        yield from gray_code(str + '0')
        yield from gray_code(str + '1')

    result_list = []
    for p_ in gray_code(''):
        result_list.append(p_)
    return result_list


assert gray_code_with_product(2) == ['00', '01', '10', '11']
assert gray_code_without_product(2) == ['00', '01', '10', '11']
