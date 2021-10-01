# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i
# = 0.
#
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20].
# Given [1, 3, 6, 24], return [1, 3, 6, 24].
#
#
# --------------------------------------------------------------------------------
#
#


def longest_subset(array):
    def find_all_subsets(array_=[], position=0):
        if position == len(array):
            yield array_
        else:
            yield from find_all_subsets(array_ + [array[position]], position + 1)
            yield from find_all_subsets(array_, position + 1)
    subset = None
    subset_length = 0
    for product in find_all_subsets():
        flag = True
        for i in range(len(product)):
            for item in product[i + 1:]:
                if max(abs(product[i]), abs(item)) % min(abs(product[i]), abs(item)) != 0:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            if len(product) > subset_length:
                subset = product
                subset_length = len(product)
    return subset


assert longest_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
assert longest_subset([1, 3, 6, 24]) == [1, 3, 6, 24]
