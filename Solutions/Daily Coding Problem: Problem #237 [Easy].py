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


def is_symetric_tree(graph: Tree_node) -> bool:
    def is_symetric_tree_hepler(root1: Node, root2: Node) -> None:
        if root1 in graph.children and root2 in graph.children:
            if len(graph.children[root1]) == len(graph.children[root2]):
                length = len(graph.children[root1])
                left_children = graph.children[root1][:length // 2 + 1] if length % 2 == 1 else graph.children[root1][:length // 2]
                right_children = graph.children[root2][length // 2:] if length % 2 == 1 else graph.children[root2][length // 2:]
                right_children.reverse()
                for node1, node2 in zip(left_children, right_children):
                    if node1.arg == node2.arg:
                        if graph.edge_angle[root1, node1] == graph.max_angle - graph.edge_angle[root2, node2]:
                            yield from is_symetric_tree_hepler(node1, node2)
                        else:
                            yield False
                    else:
                        yield False
            else:
                yield False
        elif root1 in graph.children and root2 not in graph.children or root1 not in graph.children and root2 in graph.children:
            yield False

    for is_symetric in is_symetric_tree_hepler(graph.root, graph.root):
        if not is_symetric:
            return False
    return True


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

assert is_symetric_tree(Graph) is True
f.arg = 8
assert is_symetric_tree(Graph) is False
f.arg = 9
Graph.edge_angle[b, e] = 15
assert is_symetric_tree(Graph) is False
Graph.edge_angle[d, f] = 165
assert is_symetric_tree(Graph) is True
