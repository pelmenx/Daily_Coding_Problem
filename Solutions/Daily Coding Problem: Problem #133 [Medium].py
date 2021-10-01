# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a node in a binary search tree, return the next bigger element, also known
# as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
#    10
#   /  \
#  5    30
#      /  \
#    22    35
#
#
# You can assume each node has a parent pointer.
#
#
# --------------------------------------------------------------------------------
#
#
class BST(object):
    def __init__(self, arg):
        super(BST, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None
        self.parent = None


def inorder_successor(node):
    def case_1(node_):
        if node_.left:
            return case_1(node_.left)
        else:
            return node_

    def case_2(ancestor, descendant):
        if ancestor.left == descendant:
            return ancestor
        else:
            return(ancestor.parent, ancestor)

    successor = None
    if node.right:
        successor = case_1(node.right)
    else:
        successor = case_2(node.parent, node)
    return successor


a = BST(10)
b = BST(5)
c = BST(30)
d = BST(22)
e = BST(35)

a.left = b
a.right = c
c.left = d
c.right = e

b.parent = a
c.parent = a
d.parent = c
e.parent = c

assert inorder_successor(d) == c
