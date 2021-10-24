# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Recall that the minimum spanning tree is the subset of edges of a tree that
# connect all its vertices with the smallest possible total edge weight. Given an
# undirected graph with weighted edges, compute the maximum weight spanning tree.
#
#
# --------------------------------------------------------------------------------
#
#
from collections import defaultdict


class Node:
    def __init__(self, arg: str):
        self.arg = arg

    def __repr__(self):
        return self.arg


class Graph:
    def __init__(self):
        self.edges_weight = {}
        self.edges = defaultdict(list)
        self.nodes = set()

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_edge(self, node1: Node, node2: Node, weight: float | int):
        self.edges_weight[node1, node2] = weight
        self.edges_weight[node2, node1] = weight
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)


def get_max_weight_span_tree(graph: Graph) -> int | float:
    def find_max_weight_span_tree(node: Node, visited: set, total_weight: int | float = 0):
        if visited == graph.nodes:
            yield total_weight

        for value in graph.edges[node]:
            if value not in visited:
                visited.add(value)
                new_weight = total_weight + graph.edges_weight[node, value]
                yield from find_max_weight_span_tree(value, visited, new_weight)
                visited.remove(value)

    nodes = list(graph.nodes)
    max_weight: float | int = 0
    for node in nodes:
        for weight in find_max_weight_span_tree(node, {node}):
            max_weight = max(max_weight, weight)
    return max_weight


g = Graph()
a = Node("a")
b = Node("b")
c = Node("c")
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_edge(a, b, 1)
g.add_edge(a, c, 2)
g.add_edge(b, c, 3)

assert get_max_weight_span_tree(g) == 5
