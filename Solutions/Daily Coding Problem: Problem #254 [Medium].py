# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yahoo.
#
# Recall that a full binary tree is one in which each node is either a leaf node,
# or has two children. Given a binary tree, convert it to a full one by removing
# nodes with only one child.
#
# For example, given the following tree:
#
#          0
#       /     \
#     1         2
#   /            \
# 3                 4
#   \             /   \
#     5          6     7
#
#
# You should convert it to:
#
#      0
#   /     \
# 5         4
#         /   \
#        6     7
#
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg) -> None:
        self.arg = arg
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return repr(self.arg)


def make_full_binary_tree(root, branch=0):  # sourcery skip: remove-redundant-if
    if root.left and not root.right:
        if branch == 0:
            root.parent.left = root.left
        else:
            root.parent.right = root.left
        root.left.parent = root.parent
        make_full_binary_tree(root.left, 0)
    elif root.right and not root.left:
        if branch == 0:
            root.parent.left = root.right
        else:
            root.parent.right = root.right
        root.right.parent = root.parent
        make_full_binary_tree(root.right, 1)
    elif root.left and root.right:
        make_full_binary_tree(root.left, 0)
        make_full_binary_tree(root.right, 1)


a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)
h = Node(7)
a.left = b
b.parent = a
b.left = d
d.parent = b
d.right = f
f.parent = d
a.right = c
c.parent = a
c.right = e
e.parent = c
e.left = g
g.parent = e
e.right = h
h.parent = e

make_full_binary_tree(a)
assert a.left == f
assert f.left is None
assert f.right is None
assert f.parent == a
assert a.right == e
assert e.parent == a
assert e.left == g
assert g.left is None
assert g.right is None
assert g.parent == e
assert e.right == h
assert h.left is None
assert h.right is None
assert h.parent == e
