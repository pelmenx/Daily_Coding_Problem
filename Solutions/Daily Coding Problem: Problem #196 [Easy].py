# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Given the root of a binary tree, find the most frequent subtree sum. The subtree
# sum of a node is the sum of all values under a node, including the node itself.
#
# For example, given the following tree:
#
#   5
#  / \
# 2  -5
#
#
# Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5
# - 5.
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


aa = Node(5)
bb = Node(2)
cc = Node(-5)

aa.left = bb
aa.right = cc

#    1
#   / \
#  2   3
#     / \
#    4   5
#   / \
#  6   7

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e
d.left = f
d.right = g


def common_subtree_sum(root):
    def search_for_nodes(root_):
        result = subtree_sum(root_, root_.arg)
        yield result
        if not root_.left and not root_.right:
            return
        if root_.left:
            yield from search_for_nodes(root_.left)
        if root_.right:
            yield from search_for_nodes(root_.right)

    def subtree_sum(root_, x):
        if root_.left:
            x = subtree_sum(root_.left, x + root_.left.arg)
        if root_.right:
            x = subtree_sum(root_.right, x + root_.right.arg)
        return x

    result_dict = {}
    common_sum = root.arg
    frequent = 1
    for sum in search_for_nodes(root):
        if sum not in result_dict:
            result_dict[sum] = 1
        else:
            result_dict[sum] += 1
            if result_dict[sum] > frequent:
                frequent = result_dict[sum]
                common_sum = sum

    return common_sum


assert common_subtree_sum(aa) == 2
assert common_subtree_sum(a) == 1
