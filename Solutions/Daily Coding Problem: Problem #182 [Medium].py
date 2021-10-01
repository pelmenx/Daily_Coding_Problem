# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# A graph is minimally-connected if it is connected and there is no edge that can
# be removed while still leaving the graph connected. For example, any binary tree
# is minimally-connected.
#
# Given an undirected graph, check if the graph is minimally-connected. You can
# choose to represent the graph as either an adjacency matrix or adjacency list.
#
#
# --------------------------------------------------------------------------------
#
#
def is_graph_minimally_connected(graph):
    def is_connected(graph_, vertex,):
        tmp = []
        for i, item in enumerate(graph_[vertex]):
            if item:
                graph_[vertex][i] = 0
                graph_[i][vertex] = 0
                tmp.append(i)
        visited_vertex.extend(tmp)
        for item in tmp:
            is_connected(graph_, item)
    visited_vertex = [0]
    is_connected(graph, 0)
    if len(visited_vertex) != len(graph):
        return False
    for i, item in enumerate(visited_vertex):
        for item_ in visited_vertex[i + 1:]:
            if item == item_:
                return False
    return True


adjacency_matrix1 = [[0, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0]]

adjacency_matrix2 = [[0, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [1, 0, 0, 1, 0]]

adjacency_matrix3 = [[0, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

adjacency_matrix4 = [[0, 1, 0, 0],
                     [1, 0, 0, 1],
                     [0, 0, 0, 1],
                     [0, 1, 1, 0]]

adjacency_matrix5 = [[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [0, 1, 1, 0]]

adjacency_matrix6 = [[0, 1, 0, 0],
                     [1, 0, 0, 1],
                     [0, 0, 0, 0],
                     [0, 1, 0, 0]]

assert is_graph_minimally_connected(adjacency_matrix1) is True
assert is_graph_minimally_connected(adjacency_matrix2) is False
assert is_graph_minimally_connected(adjacency_matrix3) is False
assert is_graph_minimally_connected(adjacency_matrix4) is True
assert is_graph_minimally_connected(adjacency_matrix5) is False
assert is_graph_minimally_connected(adjacency_matrix6) is False
