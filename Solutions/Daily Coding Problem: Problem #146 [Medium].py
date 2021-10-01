# Good morning! Here's your coding interview problem for today.
#
# This question was asked by BufferBox.
#
# Given a binary tree where all nodes are either 0 or 1, prune the tree so that
# subtrees containing all 0s are removed.
#
# For example, given the following tree:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0
#
#
# should be pruned to:
#
#    0
#   / \
#  1   0
#     /
#    1
#
#
# We do not remove the tree at the root or its left child because it still has a 1
# as a descendant.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def prune_tree(node):
    if node.left:
        if node.left.arg == 0:
            if not node.left.left and not node.left.right:
                node.left = None
    if node.right:
        if node.right.arg == 0:
            if not node.right.left and not node.right.right:
                node.right = None
    if node.left:
        prune_tree(node.left)
    if node.right:
        prune_tree(node.right)


a = Node(0)
b = Node(1)
c = Node(0)
d = Node(1)
e = Node(0)
f = Node(0)
g = Node(0)

a.left = b
a.right = c
c.left = d
c.right = e
d.left = f
d.right = g

prune_tree(a)

assert a.arg == 0
assert a.left.arg == 1
assert a.left.left is None
assert a.left.right is None
assert a.right.arg == 0
assert a.right.left.arg == 1
assert a.right.right is None
assert a.right.left.left is None
assert a.right.left.right is None
