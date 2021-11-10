# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# The transitive closure of a graph is a measure of which vertices are reachable
# from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if
# there is a path between vertices i and j, and otherwise 0.
#
# For example, suppose we are given the following graph in adjacency list form:
#
# graph = [
#     [0, 1, 3],
#     [1, 2],
#     [2],
#     [3]
# ]
#
#
# The transitive closure of this graph would be:
#
# [1, 1, 1, 1]
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
#
#
# Given a graph, find its transitive closure.
#
#
# --------------------------------------------------------------------------------
#
#
def get_matrix(array):
    def update_matrix(current_row, row):
        for col in array[current_row]:
            if col not in visited:
                matrix[row][col] = 1
                visited.add(col)
                update_matrix(col, row)

    matrix = [[0 for _ in range(len(array))] for _ in range(len(array))]
    visited = set()
    for i in range(len(array)):
        update_matrix(i, i)
        visited.clear()
    return matrix


assert get_matrix([[0, 1, 3], [1, 2], [2], [3]]) == [
    [1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
