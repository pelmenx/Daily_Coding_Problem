# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Coursera.
#
# Given a 2D board of characters and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# For example, given the following board:
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
#
# exists(board, "ABCCED") returns true,exists(board, "SEE") returns true,
# exists(board, "ABCB") returns false.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def exists(array, string,):
    def check_next_letter(array_inside, string_inside, row, column):
        if not string_inside:
            yield True
        for position in position_list:
            new_row = row + position[0]
            new_col = column + position[1]
            if 0 <= new_row < len(array) and 0 <= new_col < len(array[0]):
                if array_inside[new_row][new_col] == string_inside[0]:
                    tmp_array_inside = copy.deepcopy(array_inside)
                    tmp_array_inside[new_row][new_col] = None
                    yield from check_next_letter(tmp_array_inside, string_inside[1:], new_row, new_col)

    position_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i, row_ in enumerate(array):
        for j, item in enumerate(row_):
            if item == string[0]:
                tmp_array = copy.deepcopy(array)
                tmp_array[i][j] = None
                for _ in check_next_letter(tmp_array, string[1:], i, j):
                    return True
    return False


matrix = [['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']]

assert exists(matrix, "ABCCED") is True
assert exists(matrix, "SEE") is True
assert exists(matrix, "ABCB") is False
