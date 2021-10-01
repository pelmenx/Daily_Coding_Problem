# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root of a binary search tree, and a target K, return two nodes in the
# tree whose sum equals K.
#
# For example, given the following tree and K of 20
#
#     10
#    /   \
#  5      15
#        /  \
#      11    15
#
#
# Return the nodes 5 and 15.
#
#
# --------------------------------------------------------------------------------
#
#
class Binary_tree(object):
    def __init__(self, arg):
        super(Binary_tree, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def find_two_nodes(root_, k):
    def find_two_nodes_inside(root):
        if k - root.arg in nodes_dict:
            yield nodes_dict[k - root.arg], root
        nodes_dict[root.arg] = root
        if root.left:
            yield from find_two_nodes_inside(root.left)
        if root.right:
            yield from find_two_nodes_inside(root.right)
    nodes_dict = {}
    for result in find_two_nodes_inside(root_):
        return result


a = Binary_tree(10)
b = Binary_tree(5)
c = Binary_tree(15)
d = Binary_tree(11)
e = Binary_tree(15)
a.left = b
a.right = c
c.left = d
c.right = e

assert find_two_nodes(a, 20) == (b, c)
