# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an N by M 2D matrix of lowercase letters. Determine the minimum
# number of columns that can be removed to ensure that each row is ordered from
# top to bottom lexicographically. That is, the letter at each column is
# lexicographically later as you go down each row. It does not matter whether each
# row itself is ordered lexicographically.
#
# For example, given the following table:
#
# cba
# daf
# ghi
#
#
# This is not ordered because of the a in the center. We can remove the second
# column to make it ordered:
#
# ca
# df
# gi
#
#
# So your function should return 1, since we only needed to remove 1 column.
#
# As another example, given the following table:
#
# abcdef
#
#
# Your function should return 0, since the rows are already ordered (there's only
# one row).
#
# As another example, given the following table:
#
# zyx
# wvu
# tsr
#
#
# Your function should return 3, since we would need to remove all the columns to
# order it.
#
#
# --------------------------------------------------------------------------------
#
#
def number_of_removed_columns(matrix):
    if len(matrix) <= 1:
        return 0
    count = 0
    N = len(matrix)
    M = len(matrix[0])
    for i in range(M):
        for j in range(1, N):
            if matrix[j][i] < matrix[j - 1][i]:
                count += 1
                break
    return count


assert number_of_removed_columns([['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']]) == 1
assert number_of_removed_columns(['a', 'b', 'c', 'd', 'e', 'f']) == 0
assert number_of_removed_columns([['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']]) == 3
