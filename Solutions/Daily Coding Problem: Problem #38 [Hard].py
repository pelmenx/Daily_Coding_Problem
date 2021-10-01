# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# You have an N by N board. Write a function that, given N, returns the number of
# possible arrangements of the board where N queens can be placed on the board
# without threatening each other, i.e. no two queens share the same row, column,
# or diagonal.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def queens_position(n, matrix=None, counter=0, pointer=0):
    if matrix is None:
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(5)
        return queens_position(n, matrix)
    if counter == n:
        return 1
    result = 0
    for j in range(len(matrix[pointer])):
        tmp_matrix = copy.deepcopy(matrix)
        if tmp_matrix[pointer][j] == 5:
            counter += 1
            for k in range(len(tmp_matrix[pointer])):
                tmp_matrix[pointer][k] = 0
                tmp_matrix[k][j] = 0
            start = [pointer - min(pointer, j), j - min(pointer, j)]
            for m in range(n - max(start)):
                tmp_matrix[start[0] + m][start[1] + m] = 0
            for q in range(len(tmp_matrix)):
                for w in range(len(tmp_matrix[pointer])):
                    if q + w == pointer + j:
                        tmp_matrix[q][w] = 0
            tmp_matrix[pointer][j] = 1
            pointer += 1
            result += queens_position(n, tmp_matrix, counter, pointer)
            counter -= 1
            pointer -= 1
    return result


print(queens_position(8))
