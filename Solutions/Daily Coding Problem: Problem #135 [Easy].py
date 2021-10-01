# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Apple.
#
# Given a binary tree, find a minimum path sum from root to a leaf.
#
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
#
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1
#
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def min_sum_path_from_root_to_leafs(root):
    def paths(node_, sum=0, path_=[]):
        if not node_.left and not node_.right:
            yield sum + node_.arg, path_ + [node_.arg]
        if node_.left:
            yield from paths(node_.left, sum + node_.arg, path_ + [node_.arg])
        if node_.right:
            yield from paths(node_.right, sum + node_.arg, path_ + [node_.arg])
    min_sum = maxsize
    result_path = None
    for current_sum, path in paths(root):
        if current_sum < min_sum:
            min_sum = current_sum
            result_path = path
    return min_sum, result_path


a = Node(10)
b = Node(5)
c = Node(5)
d = Node(2)
e = Node(1)
f = Node(-1)

a.left = b
a.right = c
b.right = d
c.right = e
e.left = f

assert min_sum_path_from_root_to_leafs(a) == (15, [10, 5, 1, -1])
