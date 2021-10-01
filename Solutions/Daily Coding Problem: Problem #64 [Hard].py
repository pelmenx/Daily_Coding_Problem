# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A knight's tour is a sequence of moves by a knight on a chessboard such that all
# squares are visited once.
#
# Given N, write a function to return the number of knight's tours on an N by N
# chessboard.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def knight_tour(n):
    def knight_tour_inside(tmp_board1, start):
        if tmp_board1 == check_board:
            return 1
        sum = 0
        list_of_move = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        for move in list_of_move:
            if 0 <= start[0] + move[0] < n and 0 <= start[1] + move[1] < n and tmp_board1[start[0] + move[0]][start[1] + move[1]] == 0:
                tmp_tmp_board = copy.deepcopy(tmp_board1)
                tmp_tmp_board[start[0] + move[0]][start[1] + move[1]] = 1
                sum += knight_tour_inside(tmp_tmp_board, (start[0] + move[0], start[1] + move[1]))
        return sum

    check_board = [[1] * n] * n
    board = []
    count = 0
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            tmp_board = copy.deepcopy(board)
            tmp_board[i][j] = 1
            count += knight_tour_inside(tmp_board, (i, j))
    return count


print(knight_tour(5))
