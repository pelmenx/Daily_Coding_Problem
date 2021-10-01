# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Slack.
#
# You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
# how many ways are there to reach the bottom right corner?
#
# You can only move right and down. 0 represents an empty space while 1 represents
# a wall you cannot walk through.
#
# For example, given the following matrix:
#
# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]
#
#
# Return two, as there are only two ways to get to the bottom right:
#
#  * Right, down, down, right
#  * Down, right, down, right
#
# The top left corner and bottom right corner will always be 0.
#
#
# --------------------------------------------------------------------------------
#
#
def number_of_paths(matrix):
    def find_path(x=0, y=0, end=[len(matrix) - 1, len(matrix[0]) - 1]):
        if [x, y] == end:
            yield
        if x + 1 < len(matrix):
            if matrix[x + 1][y] == 0:
                yield from find_path(x + 1, y)
        if y + 1 < len(matrix[0]):
            if matrix[x][y + 1] == 0:
                yield from find_path(x, y + 1)
    count = 0
    for _ in find_path():
        count += 1
    return count


array = [[0, 0, 1],
         [0, 0, 1],
         [1, 0, 0]]

assert number_of_paths(array) == 2
