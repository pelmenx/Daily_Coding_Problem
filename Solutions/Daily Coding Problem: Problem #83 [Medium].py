# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Invert a binary tree.
#
# For example, given the following tree:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
#
#
# should become:
#
#   a
#  / \
#  c  b
#  \  / \
#   f e  d
#
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

    def invert(root):
        if not root.right and not root.left:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            Node.invert(root.left)
        if root.right:
            Node.invert(root.right)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

Node.invert(a)

assert a.left == c
assert a.right == b
assert c.right == f
assert b.left == e
assert b.right == d
