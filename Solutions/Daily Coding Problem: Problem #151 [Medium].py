# Good morning! Here's your coding interview problem for today.
#
# Given a 2-D matrix representing an image, a location of a pixel in the screen
# and a color C, replace the color of the given pixel and all adjacent same
# colored pixels with C.
#
# For example, given the following matrix, and location pixel of (2, 2), and 'G'
# for green:
#
# B B W
# W W W
# W W W
# B B B
#
#
# Becomes
#
# B B G
# G G G
# G G G
# B B B
#
#
#
# --------------------------------------------------------------------------------
#
#
def replace_color(matrix, position, color):
    def coloring(start):
        if 0 <= start[0] - 1 < len(matrix):
            if matrix[start[0] - 1][start[1]] == replaced_color:
                matrix[start[0] - 1][start[1]] = color
                coloring((start[0] - 1, start[1]))
        if 0 <= start[0] + 1 < len(matrix):
            if matrix[start[0] + 1][start[1]] == replaced_color:
                matrix[start[0] + 1][start[1]] = color
                coloring((start[0] + 1, start[1]))
        if 0 <= start[1] - 1 < len(matrix[0]):
            if matrix[start[0]][start[1] - 1] == replaced_color:
                matrix[start[0]][start[1] - 1] = color
                coloring((start[0], start[1] - 1))
        if 0 <= start[1] + 1 < len(matrix[0]):
            if matrix[start[0]][start[1] + 1] == replaced_color:
                matrix[start[0]][start[1] + 1] = color
                coloring((start[0], start[1] + 1))
    replaced_color = matrix[position[0]][position[1]]
    matrix[position[0]][position[1]] = color
    coloring(position)
    return matrix


array = [['B', 'B', 'W'],
         ['W', 'W', 'W'],
         ['W', 'W', 'W'],
         ['B', 'B', 'B']]

new_array = replace_color(array, (2, 2), "G")

for row in new_array:
    print(row)
