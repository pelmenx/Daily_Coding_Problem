# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Etsy.
#
# Given an array of numbers N and an integer k, your task is to split N into k
# partitions such that the maximum sum of any partition is minimized. Return this
# sum.
#
# For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since
# the optimal partition is [5, 1, 2], [7], [3, 4].
#
#
# --------------------------------------------------------------------------------
#
#
from copy import deepcopy


def split_array(array: list[int], k: 3) -> int | None:
    if len(array) < k or k < 1:
        return None

    def split(array_: list) -> list:
        yield array_
        for i, (block1, block2) in enumerate(zip(array_[:-1], array_[1:])):
            if len(block2) > 1:
                array_[i].append(array_[i + 1].pop(0))
                tmp = tuple(tuple(item) for item in array_)
                if tmp not in visited_arrays_set:
                    visited_arrays_set.add(tmp)
                    yield from split(array_)
                array_[i + 1].insert(0, array_[i].pop())
            if len(block1) > 1:
                array_[i + 1].insert(0, array_[i].pop())
                tmp = tuple(tuple(item) for item in array_)
                if tmp not in visited_arrays_set:
                    visited_arrays_set.add(tmp)
                    yield from split(array_)
                array_[i].append(array_[i + 1].pop(0))

    splitter = len(array) // k
    tmp_array = []
    for i in range(k):
        if i != k - 1:
            tmp_array.append(array[splitter * i:splitter * (i + 1)])
        else:
            tmp_array.append(array[splitter * i:])
    visited_arrays_set = set()
    min_max_block_sum = sum(array)
    for arr in split(tmp_array):
        if max([sum(block) for block in arr]) < min_max_block_sum:
            min_max_block_sum = max([sum(block) for block in arr])
            min_array = deepcopy(arr)
    return min_max_block_sum


assert split_array([5, 1, 2, 7, 3, 4], 3) == 8
assert split_array([5, 1, 2, 7, 3, 4], 6) == 7
assert split_array([5, 1, 2, 7, 3, 4], 7) is None
assert split_array([5, 1, 2, 7, 3, 4], 0) is None
