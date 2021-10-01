# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yelp.
#
# The horizontal distance of a binary tree node describes how far left or right
# the node will be when the tree is printed out.
#
# More rigorously, we can define it as follows:
#
#  * The horizontal distance of the root is 0.
#  * The horizontal distance of a left child is hd(parent) - 1.
#  * The horizontal distance of a right child is hd(parent) + 1.
#
# For example, for the following tree, hd(1) = -2, and hd(6) = 0.
#
#              5
#           /     \
#         3         7
#       /  \      /   \
#     1     4    6     9
#    /                /
#   0                8
#
#
# The bottom view of a tree, then, consists of the lowest node at each horizontal
# distance. If there are two nodes at the same depth and horizontal distance,
# either is acceptable.
#
# For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
#
# Given the root to a binary tree, return its bottom view.
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


def bottom_view_if_a_tree(root):
    def make_bottom_view(root_, horizontal_distance=0):
        bottom_view_dict[horizontal_distance] = root_.arg
        if root_.left:
            make_bottom_view(root_.left, horizontal_distance - 1)
        if root_.right:
            make_bottom_view(root_.right, horizontal_distance + 1)

    bottom_view_dict = {}
    make_bottom_view(root)
    bottom_view_list = []
    for i in range(min(bottom_view_dict.keys()), max(bottom_view_dict.keys()) + 1):
        bottom_view_list.append(bottom_view_dict[i])
    return bottom_view_list


a = Node(5)
b = Node(3)
c = Node(7)
a.left = b
a.right = c

d = Node(1)
e = Node(4)
f = Node(6)
g = Node(9)
b.left = d
b.right = e
c.left = f
c.right = g

h = Node(0)
d.left = h

i = Node(8)
g.left = i

assert bottom_view_if_a_tree(a) == [0, 1, 3, 6, 8, 9]
