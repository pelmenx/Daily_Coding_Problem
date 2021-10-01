# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Let A be an N by M matrix in which every row and every column is sorted.
#
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1,
# j1] and larger than M[i2, j2].
#
# For example, given the following matrix:
#
# [[1, 3, 7, 10, 15, 20],
#  [2, 6, 9, 14, 22, 25],
#  [3, 8, 10, 15, 25, 30],
#  [10, 11, 12, 23, 30, 35],
#  [20, 25, 30, 35, 40, 45]]
#
#
# And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the
# matrix smaller than 6 or greater than 23.
#
#
# --------------------------------------------------------------------------------
#
#
def find_number_of_elements(matrix, i1, j1, i2, j2):
    def find_smaller_elemets():
        counter = 0
        for row in matrix:
            if row[0] >= matrix[i1][j1]:
                break
            for item in row:
                if item >= matrix[i1][j1]:
                    break
                counter += 1
        return counter

    def find_greater_elements():
        counter = 0
        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][-1] <= matrix[i2][j2]:
                break
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] <= matrix[i2][j2]:
                    break
                counter += 1
        return counter

    return find_smaller_elemets() + find_greater_elements()


array = [[1, 3, 7, 10, 15, 20],
         [2, 6, 9, 14, 22, 25],
         [3, 8, 10, 15, 25, 30],
         [10, 11, 12, 23, 30, 35],
         [20, 25, 30, 35, 40, 45]]

assert find_number_of_elements(array, 1, 1, 3, 3) == 14
