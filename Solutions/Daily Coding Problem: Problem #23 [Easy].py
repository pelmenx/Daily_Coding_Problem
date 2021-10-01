# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the minimum
# number of steps required to reach the end coordinate from the start. If there is
# no possible path, then return null. You can move up, left, down, and right. You
# cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
#
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1,
# 2) because there is a wall everywhere else on the second row.
#
#
# --------------------------------------------------------------------------------
#
#
import sys


def find_min_number_of_steps(matrix, start, end):
    global distance_from_start_dict, neighbour_points_dict
    if start not in neighbour_points_dict:
        return "start inside a wall"
    for neighbour_points in neighbour_points_dict[start]:
        if distance_from_start_dict[start] + 1 <= distance_from_start_dict[neighbour_points]:
            distance_from_start_dict[neighbour_points] = distance_from_start_dict[start] + 1
    tmp = neighbour_points_dict[start]
    neighbour_points_dict.pop(start)
    for point in tmp:
        try:
            find_min_number_of_steps(matrix, point, end)
        except KeyError:
            pass
    return distance_from_start_dict[end]


def find_path(start, end, path):
    global neighbour_points_dict_copy, distance_from_start_dict
    if start == end:
        path.reverse()
    for neighbour_points in neighbour_points_dict_copy[end]:
        if distance_from_start_dict[neighbour_points] == distance_from_start_dict[end] - 1:
            path.append(neighbour_points)
            return find_path(start, neighbour_points, path)
    return path


def make_graphs(matrix, start):
    neighbour_points_dict = {}
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            tmp = []
            if matrix[i][j] == 0:
                if 0 <= j + 1 < len(matrix[0]) and matrix[i][j + 1] == 0:
                    tmp.append((i, j + 1))
                if 0 <= j - 1 < len(matrix[0]) and matrix[i][j - 1] == 0:
                    tmp.append((i, j - 1))
                if 0 <= i + 1 < len(matrix[0]) and matrix[i + 1][j] == 0:
                    tmp.append((i + 1, j))
                if 0 <= i - 1 < len(matrix[0]) and matrix[i - 1][j] == 0:
                    tmp.append((i - 1, j))
                neighbour_points_dict[(i, j)] = tmp
    distance_from_start_dict = {}
    for point in neighbour_points_dict:
        if point == start:
            distance_from_start_dict[point] = 0
        else:
            distance_from_start_dict[point] = sys.maxsize
    return neighbour_points_dict, distance_from_start_dict


matrix = [[0, 0, 0, 0],
          [1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


start = (3, 0)
end = (0, 0)

neighbour_points_dict, distance_from_start_dict = make_graphs(matrix, start)
neighbour_points_dict_copy = neighbour_points_dict.copy()

min_distance = find_min_number_of_steps(matrix, start, end)
if min_distance == "start inside a wall":
    print(min_distance)
elif min_distance == sys.maxsize:
    print("there is no way")
else:
    print(min_distance)
    print(find_path(start, end, path=[end]))
