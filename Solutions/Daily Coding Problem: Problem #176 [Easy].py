# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Bloomberg.
#
# Determine whether there exists a one-to-one character mapping from one string s1
# to another s2.
#
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b
# to c, and c to d.
#
# Given s1 = foo and s2 = bar, return false since the o cannot map to two
# characters.
#
#
# --------------------------------------------------------------------------------
#
#
def is_mapping(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for item in s1:
        if item not in s1_dict:
            s1_dict[item] = None
    for item in s2:
        if item not in s2_dict:
            s2_dict[item] = None
    if len(s1_dict) == len(s2_dict):
        return True
    else:
        return False


assert is_mapping("abc", "bcd") is True
assert is_mapping("foo", "bar") is False
