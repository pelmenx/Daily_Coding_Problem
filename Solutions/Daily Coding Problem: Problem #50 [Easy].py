# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Suppose an arithmetic expression is given as a binary tree. Each leaf is an
# integer and each internal node is one of '+', '−', '∗', or '/'.
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
#
# You should return 45, as it is (3 + 2) * (4 + 5).
#
#
# --------------------------------------------------------------------------------
#
#
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve(root):
    if root.val.isdigit():
        return root.val
    else:
        return eval("{}{}{}".format(solve(root.left), root.val, solve(root.right)))


node_1 = Node("*")
node_2 = Node("+")
node_3 = Node("+")
node_1.left = node_2
node_1.right = node_3
node_4 = Node("3")
node_5 = Node("2")
node_2.left = node_4
node_2.right = node_5
node_6 = Node("4")
node_7 = Node("5")
node_3.left = node_6
node_3.right = node_7

print(solve(node_1))
