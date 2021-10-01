# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root of a binary tree, return a deepest node. For example, in the
# following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d
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


a = Node("root")
b = Node("l")
c = Node("r")
d = Node("ll")

a.left = b
a.right = c
b.left = d


def deepest_node(root_):
    def deepest_node_inside(root, depth=0):
        if not root.right and not root.left:
            return root, depth
        depth_right = depth
        if root.right:
            root_right, depth_right = deepest_node_inside(root.right, depth + 1)
        depth_left = depth
        if root.left:
            root_left, depth_left = deepest_node_inside(root.left, depth + 1)
        if depth_left > depth_right:
            return(root_left, depth_left)
        else:
            return(root_right, depth_right)
    return deepest_node_inside(root_)[0]


assert deepest_node(a) == d
