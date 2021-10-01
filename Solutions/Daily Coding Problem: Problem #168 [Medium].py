# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an N by N matrix, rotate it by 90 degrees clockwise.
#
# For example, given the following matrix:
#
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
#
#
# you should return:
#
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
#
#
# Follow-up: What if you couldn't use any extra space?
#
#
# --------------------------------------------------------------------------------
#
#
def rotate_by_90_degrees(matrix):
    for i in range(len(matrix) // 2):
        for j in range(0, len(matrix[i]) - 1 - i * 2):
            r = len(matrix) - 1 - i
            matrix[i][i + j], matrix[i + j][r] = matrix[i + j][r], matrix[i][i + j]
            matrix[i][i + j], matrix[r][r - j] = matrix[r][r - j], matrix[i][i + j]
            matrix[i][i + j], matrix[r - j][i] = matrix[r - j][i], matrix[i][i + j]
    return matrix


array1 = [[11, 12, 13, 14, 15, 16],
          [21, 22, 23, 24, 25, 26],
          [31, 32, 33, 34, 35, 36],
          [41, 42, 43, 44, 45, 46],
          [51, 52, 53, 54, 55, 56],
          [61, 62, 63, 64, 65, 66]]

array2 = [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]

assert rotate_by_90_degrees(array1) == [[61, 51, 41, 31, 21, 11],
                                        [62, 52, 42, 32, 22, 12],
                                        [63, 53, 43, 33, 23, 13],
                                        [64, 54, 44, 34, 24, 14],
                                        [65, 55, 45, 35, 25, 15],
                                        [66, 56, 46, 36, 26, 16]]

assert rotate_by_90_degrees(array2) == [[9, 8, 7],
                                        [6, 5, 4],
                                        [3, 2, 1]]
