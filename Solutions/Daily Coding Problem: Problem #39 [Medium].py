# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Conway's Game of Life takes place on an infinite two-dimensional board of square
# cells. Each cell is either dead or alive, and at each tick, the following rules
# apply:
#
#  * Any live cell with less than two live neighbours dies.
#  * Any live cell with two or three live neighbours remains living.
#  * Any live cell with more than three live neighbours dies.
#  * Any dead cell with exactly three live neighbours becomes a live cell.
#
# A cell neighbours another cell if it is horizontally, vertically, or diagonally
# adjacent.
#
# Implement Conway's Game of Life. It should be able to be initialized with a
# starting list of live cell coordinates and the number of steps it should run
# for. Once initialized, it should print out the board state at each step. Since
# it's an infinite board, print out only the relevant coordinates, i.e. from the
# top-leftmost live cell to bottom-rightmost live cell.
#
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.
# ).
#
#
# --------------------------------------------------------------------------------
#
#
import copy
import sys


def Conways_Game_of_Life(life_cells_list, iteration, current_itteration=0):
    if iteration < 0:
        print("iteration parameter should be non-negative")
        return
    if not life_cells_list:
        for i in range(current_itteration, iteration + 1):
            print("current_itteration", i)
            print([])
            print()
        return
    bottom = 0
    right = 0
    top = sys.maxsize
    left = sys.maxsize
    for coordinates in life_cells_list:
        if coordinates[0] > bottom:
            bottom = coordinates[0]
        if coordinates[0] < top:
            top = coordinates[0]
        if coordinates[1] > right:
            right = coordinates[1]
        if coordinates[1] < left:
            left = coordinates[1]
    board = []
    tmp_life_cells_list = []
    for i in range(top, bottom + 2):
        board.append([])
        for j in range(left, right + 2):
            if [i, j] in life_cells_list:
                board[i - top].append("*")
                if top != 0 and left != 0:
                    tmp_life_cells_list.append([i - top + 1, j - left + 1])
                if top != 0 and left == 0:
                    tmp_life_cells_list.append([i - top + 1, j - left])
                if top == 0 and left != 0:
                    tmp_life_cells_list.append([i - top, j - left + 1])
                if top == 0 and left == 0:
                    tmp_life_cells_list.append([i - top, j - left])
            else:
                board[i - top].append(".")
    if top != 0:
        tmp_board = [["."] * len(board[0])]
        tmp_board.extend(board)
        board = copy.deepcopy(tmp_board)
        tmp_board.clear()
        if left != 0:
            for line in board:
                line.insert(0, ".")
            print("current_itteration", current_itteration)
            for line in board[1:-1]:
                print(line[1:-1])
            print()
        else:
            print("current_itteration", current_itteration)
            for line in board[1:-1]:
                print(line[-1])
            print()
    else:
        if left != 0:
            for line in board:
                line.insert(0, ".")
            print("current_itteration", current_itteration)
            for line in board[:-1]:
                print(line[1:-1])
            print()
        else:
            print("current_itteration", current_itteration)
            for line in board[:-1]:
                print(line[:-1])
            print()
    if iteration == current_itteration:
        return
    life_cells_list = copy.deepcopy(tmp_life_cells_list)
    tmp_life_cells_list.clear()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if [i, j] in life_cells_list:
                counter = 0
                for k in range(i - 1, i + 2):
                    if k >= 0 and k <= len(board):
                        for x in range(j - 1, j + 2):
                            if x >= 0 and x <= len(board[i]):
                                if [k, x] in life_cells_list and [k, x] != [i, j]:
                                    counter += 1
                if counter == 2 or counter == 3:
                    if top != 0 and left != 0:
                        tmp_life_cells_list.append([i + top - 1, j + left - 1])
                    if top != 0 and left == 0:
                        tmp_life_cells_list.append([i + top - 1, j + left])
                    if top == 0 and left != 0:
                        tmp_life_cells_list.append([i + top, j + left - 1])
                    if top == 0 and left == 0:
                        tmp_life_cells_list.append([i + top, j + left])
            else:
                counter = 0
                for k in range(i - 1, i + 2):
                    if k >= 0 and k <= len(board):
                        for x in range(j - 1, j + 2):
                            if x >= 0 and x <= len(board[i]):
                                if [k, x] in life_cells_list:
                                    counter += 1
                if counter == 3:
                    if top != 0 and left != 0:
                        tmp_life_cells_list.append([i + top - 1, j + left - 1])
                    if top != 0 and left == 0:
                        tmp_life_cells_list.append([i + top - 1, j + left])
                    if top == 0 and left != 0:
                        tmp_life_cells_list.append([i + top, j + left - 1])
                    if top == 0 and left == 0:
                        tmp_life_cells_list.append([i + top, j + left])

    return Conways_Game_of_Life(tmp_life_cells_list, iteration, current_itteration + 1)


Conways_Game_of_Life([[0, 0], [0, 4], [0, 6], [1, 0], [1, 1], [1, 5], [2, 5], [2, 6], [2, 7]], 8)
