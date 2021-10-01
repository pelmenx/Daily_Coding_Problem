# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a binary tree of integers, find the maximum path sum between two nodes.
# The path must go through at least one node, and does not need to go through the
# root.
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


def find_max_sum_of_node(root):
    def find_max_sum_of_node_inside(root, current_max=0, overall_max=0, right_sum=0, left_sum=0):
        current_max = max(root.arg, current_max + root.arg)
        overall_max = max(overall_max, current_max)
        if not root.left and not root.right:
            return overall_max
        if root.right:
            right_sum = find_max_sum_of_node_inside(root.right, current_max, overall_max)
        if root.left:
            left_sum = find_max_sum_of_node_inside(root.left, current_max, overall_max)

        return max(overall_max, left_sum, right_sum)
    return find_max_sum_of_node_inside(root)


a = Node(1)
assert find_max_sum_of_node(a) == 1

b = Node(2)
a.left = b
assert find_max_sum_of_node(a) == 3

c = Node(3)
a.right = c
assert find_max_sum_of_node(a) == 4
