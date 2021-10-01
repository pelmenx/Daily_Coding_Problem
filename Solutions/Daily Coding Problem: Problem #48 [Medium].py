# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given pre-order and in-order traversals of a binary tree, write a function to
# reconstruct the tree.
#
# For example, given the following preorder traversal:
#
# [a, b, d, e, c, f, g]
#
# And the following inorder traversal:
#
# [d, b, e, a, f, c, g]
#
# You should return the following tree:
#
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
#
#
#
# --------------------------------------------------------------------------------
#
#
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def get_tree(preorder, inorder):
    root = preorder[0]
    if not preorder or not inorder:
        return None
    if len(preorder) == 1:
        return Node(root)
    root_node = Node(root)
    for i, char in enumerate(inorder):
        if char == root:
            root_node.left = get_tree(preorder[1:i + 1], inorder[:i])
            root_node.right = get_tree(preorder[i + 1:], inorder[i + 1:])
    return root_node


tree = get_tree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])

print(" " * 5, tree.val)
print(" " * 1, tree.left.val, " " * 5, tree.right.val)
print(tree.left.left.val, tree.left.right.val, tree.right.left.val, tree.right.right.val, sep="   ")
