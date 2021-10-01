# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by LinkedIn.
#
# Determine whether a tree is a valid binary search tree.
#
# A binary search tree is a tree with two children, left and right, and satisfies
# the constraint that the key in the left child must be less than or equal to the
# root and the key in the right child must be greater than or equal to the root.
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


def is_binary_tree_is_valid(root):
    def is_binary_tree_is_valid_unside(root_):
        if not root_.right and not root_.left:
            yield True
        if root_.left:
            if root_.left.arg <= root_.arg:
                yield from is_binary_tree_is_valid_unside(root_.left)
            else:
                yield False
        if root_.right:
            if root_.right.arg >= root_.arg:
                yield from is_binary_tree_is_valid_unside(root_.right)
            else:
                yield False
    check = True
    for result in is_binary_tree_is_valid_unside(root):
        check = check and result
        if check is False:
            return False
    return True


a = Binary_tree(50)
b = Binary_tree(25)
c = Binary_tree(75)
a.left = b
a.right = c

assert is_binary_tree_is_valid(a) is True

a = Binary_tree(50)
b = Binary_tree(25)
c = Binary_tree(25)
a.left = b
a.right = c

assert is_binary_tree_is_valid(a) is False
