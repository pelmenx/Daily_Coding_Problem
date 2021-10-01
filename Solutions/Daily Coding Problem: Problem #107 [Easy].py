# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Print the nodes in a binary tree level-wise. For example, the following should
# print 1, 2, 3, 4, 5.
#
#   1
#  / \
# 2   3
#    / \
#   4   5
#
#
#
# --------------------------------------------------------------------------------
#
#
class nodes(object):
    def __init__(self, arg):
        super(nodes, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def print_by_level(root):
    def check_level(current_level):
        for item in current_level:
            print(',', item.arg, end="")
            next_level_inside = []
            if item.left:
                next_level_inside.append(item.left)
            if item.right:
                next_level_inside.append(item.right)
        if not next_level_inside:
            return
        return check_level(next_level_inside)
    next_level = []
    if root.left:
        next_level.append(root.left)
    if root.right:
        next_level.append(root.right)
    print(root.arg, end="")
    check_level(next_level)


a = nodes(1)
b = nodes(2)
c = nodes(3)
d = nodes(4)
e = nodes(5)

a.left = b
a.right = c
c.left = d
c.right = e

print_by_level(a)
