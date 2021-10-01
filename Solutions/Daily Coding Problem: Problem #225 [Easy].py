# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Bloomberg.
#
# There are N prisoners standing in a circle, waiting to be executed. The
# executions are carried out starting with the kth person, and removing every
# successive kth person going clockwise until there is no one left.
#
# Given N and k, write an algorithm to determine where a prisoner should stand in
# order to be the last survivor.
#
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5,
# 3], so you should return 3.
#
# Bonus: Find an O(log N) solution if k = 2.
#
#
# --------------------------------------------------------------------------------
#
#
from math import ceil


def executed_game(N, k):
    prisoners_list = [*range(1, N + 1)]
    current_prisonner_list = prisoners_list[:]
    position = -1
    while len(prisoners_list) != 1:
        if position + k >= len(current_prisonner_list):
            multiplier = ceil(k / len(prisoners_list))
            current_prisonner_list += prisoners_list * multiplier
        position += k
        prisoners_list.remove(current_prisonner_list[position])
    return (prisoners_list[0])


def executed_game_O_log_n(N):
    def play(prisoners_list, case):
        if len(prisoners_list) == 1:
            return prisoners_list[0]
        if case:
            return play(prisoners_list[::2], False if prisoners_list[::2][-1] == prisoners_list[-1] else True)
        else:
            return play(prisoners_list[1::2], False if prisoners_list[1::2][-1] == prisoners_list[-1] else True)
    prisoners_list = [*range(1, N + 1)]
    return play(prisoners_list, True)


assert executed_game(5, 2) == 3
assert executed_game(5, 3) == 4

assert executed_game_O_log_n(5) == 3

for i in range(1, 15):
    assert executed_game(i, 2) == executed_game_O_log_n(i)
