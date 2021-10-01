# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an undirected graph represented as an adjacency matrix and an integer k,
# write a function to determine whether each vertex in the graph can be colored
# such that no two adjacent vertices share the same color using at most k colors.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def connected_nodes(adjacency_matrix):
    connected_nodes_dict = {}
    for i, row in enumerate(adjacency_matrix):
        connected_nodes_list = []
        for j, node in enumerate(row):
            if node == 1:
                connected_nodes_list.append(j)
        connected_nodes_dict[i] = connected_nodes_list
    return connected_nodes_dict


def sort_nodes(adjacency_matrix):
    tmp_matrix = copy.deepcopy(adjacency_matrix)
    sorted_nodes = []
    colored_dict = {}
    rang = 0
    while rang <= len(adjacency_matrix):
        for i, row in reversed(list(enumerate(tmp_matrix))):
            if sum(row) == rang:
                sorted_nodes.append(i)
                colored_dict[i] = None
        rang += 1
    return sorted_nodes, colored_dict


def coloring(adjacency_matrix):
    connected_nodes_dict = connected_nodes(adjacency_matrix)
    not_colored_list, colored_dict = sort_nodes(adjacency_matrix)
    color_list = [1]
    colored_dict[not_colored_list[-1]] = color_list[-1]
    not_colored_list = not_colored_list[:-1]
    while True:
        for i in range(len(not_colored_list) - 1, -1, -1):
            check = True
            for item in connected_nodes_dict.get(not_colored_list[i]):
                if colored_dict[item] == color_list[-1]:
                    check = False
            if check:
                colored_dict[not_colored_list[i]] = color_list[-1]
                not_colored_list.pop(i)
        if not not_colored_list:
            return len(color_list)
        color_list.append(color_list[-1] + 1)
    print(color_list)


def can_color_graph(adjacency_matrix, k):
    if not adjacency_matrix:
        return k >= 1
    min_number_of_color = coloring(adjacency_matrix)
    return k >= min_number_of_color


adjacency_matrix = [[0, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0],
                    [0, 1, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0, 1],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0]]
print(can_color_graph(adjacency_matrix, 3))


adjacency_matrix = [[0, 1, 1, 1, 0],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [0, 1, 1, 1, 0]]
print(can_color_graph(adjacency_matrix, 1))


adjacency_matrix = [[1]]
print(can_color_graph(adjacency_matrix, 1))


adjacency_matrix = []
print(can_color_graph(adjacency_matrix, 1))
