# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given a Node where each edge has a weight, compute the length of the longest
# path in the Node.
#
# For example, given the following Node:
#
#    a
#   /|\
#  b c d
#     / \
#    e   f
#   / \
#  g   h
#
#
# and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the
# longest path would be c -> a -> d -> f, with a length of 17.
#
# The path does not have to pass through the root, and each node can have any
# amount of children.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


class Node_list(type):
    instances = list()

    def __call__(cls, *args, **kwargs):
        instance = super(Node_list, cls).__call__(*args, **kwargs)
        cls.instances.append(instance)
        return instance


class Node(object, metaclass=Node_list):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.paths = {}


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.paths = {b: 3, c: 5, d: 8}
b.paths = {a: 3}
c.paths = {a: 5}
d.paths = {a: 8, e: 2, f: 4}
e.paths = {d: 2, g: 1, h: 1}
f.paths = {d: 4}


def longest_path(node_list):
    def find_path(node, visited_nodes, value=0):
        for n_ in node.paths:
            check = 0
            if n_ not in visited_nodes:
                yield from find_path(n_, visited_nodes + [n_], value + node.paths[n_])
            else:
                check += 1
            if check == len(node.paths):
                yield value

    max = -maxsize
    for node_ in node_list:
        for long in find_path(node_, [node_]):
            if long > max:
                max = long
    return long


assert longest_path(Node.instances) == 17
