# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in
# the tree. Assume that each node in the tree also has a pointer to its parent.
#
# According to the definition of LCA on Wikipedia
# [https://en.wikipedia.org/wiki/Lowest_common_ancestor]: “The lowest common
# ancestor is defined between two nodes v and w as the lowest node in T that has
# both v and w as descendants (where we allow a node to be a descendant of
# itself).”
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
        self.left = None
        self.right = None


def lowest_common_ancestor(node_1, node_2):
    def find_lowest_common_ancestor(node_, depth=0):
        if node_ == node_1:
            yield depth
        if node_ == node_2:
            yield depth
        if node_.left:
            yield from find_lowest_common_ancestor(node_.left, depth + 1)
        if node_.right:
            yield from find_lowest_common_ancestor(node_.right, depth + 1)
    depth_ = maxsize
    ancestor = None
    for node in Node.instances:
        descendants = []
        for result in find_lowest_common_ancestor(node):
            descendants.append(result)
        if len(descendants) == 2:
            if min(descendants) == 0:
                return node
            if min(descendants) < depth_:
                depth_ = min(descendants)
                ancestor = node
    return ancestor


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.left = b
a.right = c
b.right = d
c.left = e
c.right = f
e.left = g
e.right = h

assert lowest_common_ancestor(e, h) == e
assert lowest_common_ancestor(f, h) == c
