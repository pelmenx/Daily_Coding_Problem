# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with
# digits. The objective is to fill the grid with the constraint that every row,
# column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
#
# Implement an efficient sudoku solver.
#
#
# --------------------------------------------------------------------------------
#
#
def get_square(x, y):
    if x <= 2:
        row = 0
    elif x >= 3 and x <= 5:
        row = 3
    else:
        row = 6
    if y <= 2:
        column = 0
    elif y >= 3 and y <= 5:
        column = 3
    else:
        column = 6
    return row, column


def all_possible_values(board):
    values_dict = {}
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == ".":
                tmp = []
                for number in row:
                    if number.isdigit():
                        tmp.append(number)
                for k in range(0, 9):
                    if board[k][j].isdigit():
                        if board[k][j] not in tmp:
                            tmp.append(board[k][j])
                square_i, square_j = get_square(i, j)
                for k in range(square_i, square_i + 3):
                    for x in range(square_j, square_j + 3):
                        if board[k][x].isdigit():
                            if board[k][x] not in tmp:
                                tmp.append(board[k][x])
                tmp_new = []
                for k in range(1, 10):
                    if str(k) not in tmp:
                        tmp_new.append(str(k))
                values_dict[i, j] = tmp_new
    return values_dict


def alone(board, values_dict):
    while values_dict:
        check = False
        for item in values_dict:
            if len(values_dict.get(item)) == 1:
                board[item[0]][item[1]] = values_dict.get(item)[0]
                check = True
        if check is False:
            break
        values_dict = all_possible_values(board)
        if not values_dict:
            return True
    return values_dict


def hidden_alone(board, values_dict):
    for i in range(9):
        unique_value = {}
        for j in range(9):
            if (i, j) in values_dict:
                for item in values_dict.get((i, j)):
                    if item not in unique_value:
                        unique_value[item] = 1
                    else:
                        unique_value[item] += 1
        for pair in unique_value.items():
            if pair[1] == 1:
                for k in range(9):
                    if (i, k) in values_dict:
                        if pair[0] in values_dict.get((i, k)):
                            board[i][k] = pair[0]
                            values_dict.pop((i, k))
    for i in range(9):
        unique_value = {}
        for j in range(9):
            if (j, i) in values_dict:
                print((i, j), values_dict.get((j, i)))
                for item in values_dict.get((j, i)):
                    if item not in unique_value:
                        unique_value[item] = 1
                    else:
                        unique_value[item] += 1
        for pair in unique_value.items():
            if pair[1] == 1:
                for k in range(9):
                    if (k, i) in values_dict:
                        if pair[0] in values_dict.get((k, i)):
                            board[k][i] = pair[0]
                            values_dict.pop((k, i))
    for i in range(0, 3):
        for j in range(0, 3):
            unique_value = {}
            for k in range(i * 3, i * 3 + 3):
                for x in range(j * 3, j * 3 + 3):
                    if (k, x) in values_dict:
                        for item in values_dict.get((k, x)):
                            if item not in unique_value:
                                unique_value[item] = 1
                            else:
                                unique_value[item] += 1
            for pair in unique_value.items():
                if pair[1] == 1:
                    for k in range(i * 3, i * 3 + 3):
                        for x in range(j * 3, j * 3 + 3):
                            if (k, x) in values_dict:
                                if pair[0] in values_dict.get((k, x)):
                                    board[k][x] = pair[0]
                                    values_dict.pop((k, x))
    if not values_dict:
        return True


def solve_sudoku(board):
    values_dict = all_possible_values(board)
    values_dict = alone(board, values_dict)
    if values_dict is not True:
        values_dict = hidden_alone(board, values_dict)
        if values_dict is not True:
            return solve_sudoku(board)
        else:
            for row in board:
                print(row)
            return
    else:
        for row in board:
            print(row)
        return


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solve_sudoku(board)
