# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a multiset of integers, return whether it can be partitioned into two
# subsets whose sums are the same.
#
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return
# true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both
# add up to 55.
#
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't
# split it up into two subsets that add up to the same sum.
#
#
# --------------------------------------------------------------------------------
#
#
def find_two_equal_subset(set):
    def find_two_equal_subset(subset1, subset2=[]):
        if sum(subset1) == sum(subset2):
            yield subset1, subset2
        for i, item in enumerate(subset1):
            yield from find_two_equal_subset(subset1[:i] + subset1[i + 1:], subset2 + [item])

    splited = []
    for a, b in find_two_equal_subset(set):
        splited.append((a, b))
    if splited:
        return True
    else:
        return False


print(find_two_equal_subset([15, 5, 20, 10, 35, 15, 10]))
print(find_two_equal_subset([15, 5, 20, 10, 35]))
