# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by PayPal.
#
# Given a binary tree, determine whether or not it is height-balanced. A
# height-balanced binary tree can be defined as one in which the heights of the
# two subtrees of any node never differ by more than one.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


class Node:
    def __init__(self, arg):
        self.arg = arg
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.arg)


def is_binary_tree_height_balanced(root: Node) -> bool:
    def is_binary_tree_height_balanced_helper(root_: Node, level: int) -> None:
        if not root_.right and not root_.left:
            yield level
        if root_.left:
            yield from is_binary_tree_height_balanced_helper(root_.left, level + 1)
        if root_.right:
            yield from is_binary_tree_height_balanced_helper(root_.right, level + 1)

    min_level = maxsize
    max_level = -maxsize
    for high in is_binary_tree_height_balanced_helper(root, 0):
        if high < min_level:
            min_level = high
        if high > max_level:
            max_level = high
    return True if (max_level - min_level) == 1 or max_level == min_level else False


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
b.left = d
b.right = e

assert is_binary_tree_height_balanced(a) is True

f = Node(6)
d.left = f

assert is_binary_tree_height_balanced(a) is False
