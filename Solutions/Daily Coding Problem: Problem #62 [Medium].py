# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# There is an N by M matrix of zeroes. Given N and M, write a function to count
# the number of ways of starting at the top-left corner and getting to the
# bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there are two
# ways to get to the bottom-right:
#
#  * Right, then down
#  * Down, then right
#
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
#
#
# --------------------------------------------------------------------------------
#
#
def find_all_ways(n, m):
    def find_all_ways(x, y):
        if (x, y) == (n - 1, m - 1):
            yield 1
        if x + 1 < n:
            yield from find_all_ways(x + 1, y)
        if y + 1 < m:
            yield from find_all_ways(x, y + 1)
    number_of_ways = 0
    for i in find_all_ways(0, 0):
        number_of_ways += i
    return number_of_ways


print(find_all_ways(5, 5))
