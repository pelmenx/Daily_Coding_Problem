# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# A tree is symmetric if its data and shape remain unchanged when it is reflected
# about the root node. The following tree is an example:
#
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
#
#
# Given a k-ary tree, determine whether it is symmetric.
#
#
# --------------------------------------------------------------------------------
#
#
from copy import deepcopy


class Node(object):
    def __init__(self, arg: int):
        self.arg = arg

    def __repr__(self):
        return repr(self.arg)


class Tree_node(object):
    def __init__(self):
        self.children: dict = {}
        self.root: Node | None = None
        self.edge_angle: dict = {}
        self.max_angle: int = 180

    def add_node(self, root: Node, new_nodes: list):
        self.children[root] = new_nodes

    def add_edge_angle(self, root: Node, nodes: list, anges: list):
        for node, angle in zip(nodes, anges):
            self.edge_angle[root, node] = angle


def is_symetric_tree(graph1: Tree_node, graph2: Tree_node) -> bool:
    def is_symetric_tree_hepler(root1: Node, root2: Node) -> None:
        if root1 in graph1.children and root2 in graph2.children:
            if len(graph1.children[root1]) == len(graph2.children[root2]):
                for node1, node2 in zip(graph1.children[root1], graph2.children[root2]):
                    if node1.arg == node2.arg:
                        if graph1.edge_angle[root1, node1] == graph2.edge_angle[root2, node2]:
                            yield from is_symetric_tree_hepler(node1, node2)
                        else:
                            yield False
                    else:
                        yield False
            else:
                yield False
        elif root1 in graph1.children and root2 not in graph2.children:
            yield False
        elif root1 not in graph1.children and root2 in graph2.children:
            yield False

    for is_symetric in is_symetric_tree_hepler(graph1.root, graph2.root):
        if not is_symetric:
            return False
    return True


def reflect_graph(graph: Tree_node, root: Node) -> None:
    if root in graph.children:
        tmp = graph.children[root]
        tmp.reverse()
        graph.children[root] = tmp
        for node in graph.children[root]:
            graph.edge_angle[root, node] = graph.max_angle - graph.edge_angle[root, node]
        for node in graph.children[root]:
            reflect_graph(graph, node)


a = Node(4)
b = Node(3)
c = Node(5)
d = Node(3)
e = Node(9)
f = Node(9)

Graph = Tree_node()
Graph.root = a
Graph.add_node(a, [b, c, d])
Graph.add_edge_angle(a, [b, c, d], [45, 90, 135])
Graph.add_node(b, [e])
Graph.add_edge_angle(b, [e], [45])
Graph.add_node(d, [f])
Graph.add_edge_angle(d, [f], [135])

New_Graph = deepcopy(Graph)

reflect_graph(New_Graph, New_Graph.root)

assert is_symetric_tree(Graph, New_Graph) is True
f.arg = 8
assert is_symetric_tree(Graph, New_Graph) is False
f.arg = 9
Graph.edge_angle[b, e] = 15
assert is_symetric_tree(Graph, New_Graph) is False
