# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a binary tree, return all paths from the root to leaves.
#
# For example, given the tree:
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#
#
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].
#
#
# --------------------------------------------------------------------------------
#
#
import copy


class nodes(object):
    def __init__(self, arg):
        super(nodes, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def all_pathes(root):
    def print_path(root_):
        path.append(root_.arg)
        if not root_.right and not root_.left:
            yield path
        if root_.left:
            yield from print_path(root_.left)
            path.pop()
        if root_.right:
            yield from print_path(root_.right)
            path.pop()
    path = []
    pathes = []
    for path in print_path(root):
        tmp = copy.deepcopy(path)
        pathes.append(tmp)
    return pathes


a = nodes(1)
b = nodes(2)
c = nodes(3)
d = nodes(4)
e = nodes(5)

a.left = b
a.right = c
c.left = d
c.right = e

assert all_pathes(a) == [[1, 2], [1, 3, 4], [1, 3, 5]]
