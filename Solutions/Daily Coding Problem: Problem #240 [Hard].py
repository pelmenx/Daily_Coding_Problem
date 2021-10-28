# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Spotify.
#
# There are N couples sitting in a row of length 2 * N. They are currently ordered
# randomly, but would like to rearrange themselves so that each couple's partners
# can sit side by side.
#
# What is the minimum number of swaps necessary for this to happen?
#
#
# --------------------------------------------------------------------------------
#
#
from random import shuffle
from collections import defaultdict


def rearange_list(n: int) -> int:
    array = [*range(0, n)] * 2
    shuffle(array)
    i = 0
    counter = 0
    while i < len(array):
        for j in range(i + 2, len(array)):
            if array[i] == array[j]:
                array[i + 1], array[j] = array[j], array[i + 1]
                counter += 1
                break
        i += 2
    return counter


for n in range(1, 20):
    dd = defaultdict(int)
    for i in range(100):
        dd[rearange_list(n)] += 1

    assert max(dd) == n - 1
