# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the sequence of keys visited by a postorder traversal of a binary search
# tree, reconstruct the tree.
#
# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the
# following tree:
#
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8
#
#
#
# --------------------------------------------------------------------------------
#
#
class binary_tree(object):
    def __init__(self, arg):
        super(binary_tree, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def postorder_to_binary_tree(array):
    def get_tree(array_, root_):
        # print(array_)
        if not array_:
            return
        right = None
        left = None
        left_position = 0
        for i in range(len(array_) - 1, -1, -1):
            if array_[i] < root_.arg:
                left = binary_tree(array_[i])
                left_position = i
                break
        root_.left = left
        if array_[-1] > root_.arg:
            right = binary_tree(array_[-1])
        root_.right = right
        get_tree(array_[:left_position], left)
        get_tree(array_[left_position + 1:-1], right)
    root = binary_tree(array[-1])
    get_tree(array[:-1], root)
    return root


r = postorder_to_binary_tree([2, 4, 3, 8, 7, 5])

assert r.arg == 5
assert r.left.arg == 3
assert r.left.left.arg == 2
assert r.left.left.left is None
assert r.left.left.right is None
assert r.left.right.arg == 4
assert r.left.right.left is None
assert r.left.right.right is None
assert r.right.arg == 7
assert r.right.left is None
assert r.right.right.arg == 8
assert r.right.right.left is None
