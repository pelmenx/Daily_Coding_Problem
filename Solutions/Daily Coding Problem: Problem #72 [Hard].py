# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# In a directed graph, each node is assigned an uppercase letter. We define a
# path's value as the number of most frequently-occurring letter along that path.
# For example, if a path in the graph goes through "ABACA", the value of the path
# is 3, since there are 3 occurrences of 'A' on the path.
#
# Given a graph with n nodes and m directed edges, return the largest value path
# of the graph. If the largest value is infinite, then return null.
#
# The graph is represented with a string and an edge list. The i-th character
# represents the uppercase letter of the i-th node. Each tuple in the edge list
# (i, j) means there is a directed edge from the i-th node to the j-th node.
# Self-edges are possible, as well as multi-edges.
#
# For example, the following input graph:
#
# ABACA
#
#
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
#
#
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A)
# .
#
# The following input graph:
#
# A
#
#
# [(0, 0)]
#
#
# Should return null, since we have an infinite loop.
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product


def find_largest_value_path(nodes, list_of_edges):
    max_edges = 0
    for product_ in product((0, 1), repeat=len(list_of_edges)):
        path = []
        if sum(product_) >= 1:
            for rank, edge in zip(product_, list_of_edges):
                if edge[0] == edge[1]:
                    return None
                if rank == 1:
                    path.append(edge)
            if len(path) == 1:
                count = 1
                if count > max_edges:
                    max_edges = count
            else:
                counter_dict = {}
                check = True
                for current_path, next_path in zip(path[:-1], path[1:]):
                    if current_path[1] != next_path[0]:
                        check = False
                        break
                    if nodes[next_path[0]] in counter_dict:
                        counter_dict[nodes[next_path[0]]] += 1
                    else:
                        counter_dict[nodes[next_path[0]]] = 1

                if check is True:
                    if nodes[path[0][0]] in counter_dict:
                        counter_dict[nodes[path[0][0]]] += 1
                    else:
                        counter_dict[nodes[path[0][0]]] = 1
                    if nodes[path[-1][1]] in counter_dict:
                        counter_dict[nodes[path[-1][1]]] += 1
                    else:
                        counter_dict[nodes[path[-1][1]]] = 1
                    for item in counter_dict:
                        if counter_dict.get(item) > max_edges:
                            max_edges = counter_dict.get(item)
    return max_edges


assert find_largest_value_path("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]) == 3
assert find_largest_value_path("A", [(0, 0)]) is None
