# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a binary tree, return the level of the tree with minimum sum.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


class binary_tree(object,):
    def __init__(self, arg):
        super(binary_tree, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def level_sum(root):
    def check_next_level(array):
        next_level = []
        for item in array:
            if item.left:
                next_level.append(item.left)
            if item.right:
                next_level.append(item.right)
        return next_level
    current_level = [root]
    total = maxsize
    min_level = None
    while current_level:
        value = 0
        for item in current_level:
            value += item.arg
        if value < total:
            total = value
            min_level = current_level
        current_level = check_next_level(current_level)
    return min_level


a = binary_tree(1)
b = binary_tree(2)
c = binary_tree(3)
d = binary_tree(4)
e = binary_tree(5)
f = binary_tree(6)
g = binary_tree(7)
h = binary_tree(8)
a.left = b
a.right = c
b.right = d
c.left = e
c.right = f
e.left = g
e.right = h

assert level_sum(a) == [a]

a.arg = 10

assert level_sum(a) == [b, c]
