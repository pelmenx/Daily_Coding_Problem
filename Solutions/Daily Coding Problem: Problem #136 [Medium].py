# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Google.
#
# Given an N by M matrix consisting only of 1's and 0's, find the largest
# rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
#
#
# Return 4.
#
#
# --------------------------------------------------------------------------------
#
#
def find_islands(array):
    def make_islands(x, y):
        count = 0
        for i in range(i_, x + 1):
            for j in range(j_, y + 1):
                if not array[i][j]:
                    return
                else:
                    count += 1
        yield count
        if x + 1 < len(array[0]):
            if array[x + 1][y]:
                yield from make_islands(x + 1, y)
        if y + 1 < len(array):
            if array[x][y + 1]:
                yield from make_islands(x, y + 1)
    max_area = 0
    for i_, row in enumerate(array):
        for j_, item in enumerate(row):
            if item:
                for area in make_islands(i_, j_):
                    if area > max_area:
                        max_area = area
    return max_area


matrix = [[1, 1, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 0]]

assert find_islands(matrix) == 4
