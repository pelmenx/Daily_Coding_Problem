# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
#
# For example, given the following matrix:
#
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
#
#
# You should print out the following:
#
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12
#
#
#
# --------------------------------------------------------------------------------
#
#
def clockwise_spiral(matrix):
    if not matrix:
        return
    while matrix:
        # right
        for item in matrix[0]:
            print(item)
        matrix = matrix[1:]
        # down
        for row in matrix:
            print(row[-1])
            row.pop()
        # left
        if matrix:
            for item in matrix[-1][::-1]:
                print(item)
            matrix = matrix[:-1]
        # up
        for row in matrix[::-1]:
            print(row[0])
            row.pop(0)


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
clockwise_spiral(matrix)
