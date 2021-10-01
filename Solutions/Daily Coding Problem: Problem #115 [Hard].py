# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two non-empty binary trees s and t, check whether tree t has exactly the
# same structure and Binary_tree_1 values with a subtree of s. A subtree of s is a tree
# consists of a Binary_tree_1 in s and all of this Binary_tree_1's descendants. The tree s could
# also be considered as a subtree of itself.
#
#
# --------------------------------------------------------------------------------
#
#
class Binary_tree_1_list(type):
    instances = list()

    def __call__(cls, *args, **kwargs):
        instance = super(Binary_tree_1_list, cls).__call__(*args, **kwargs)
        cls.instances.append(instance)
        return instance


class Binary_tree_1(object, metaclass=Binary_tree_1_list):
    def __init__(self, arg):
        super(Binary_tree_1, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


class Binary_tree_2(object):
    def __init__(self, arg):
        super(Binary_tree_2, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


class Binary_tree_3(object):
    def __init__(self, arg):
        super(Binary_tree_3, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


a = Binary_tree_1(1)
b = Binary_tree_1(2)
c = Binary_tree_1(3)
d = Binary_tree_1(4)
e = Binary_tree_1(5)
f = Binary_tree_1(6)
g = Binary_tree_1(7)
h = Binary_tree_1(8)
a.left = b
a.right = c
b.right = d
c.left = e
c.right = f
e.left = g
e.right = h

c1 = Binary_tree_2(3)
e1 = Binary_tree_2(5)
f1 = Binary_tree_2(6)
g1 = Binary_tree_2(7)
h1 = Binary_tree_2(8)
c1.left = e1
c1.right = f1
e1.left = g1
e1.right = h1

c2 = Binary_tree_3(3)
e2 = Binary_tree_3(5)
f2 = Binary_tree_3(6)
g2 = Binary_tree_3(7)
h2 = Binary_tree_3(9)
c2.left = e2
c2.right = f2
e2.left = g2
e2.right = h2


def is_tree2_in_tree1(node_list, node_2_):
    def is_tree2_in_tree1_inside(node_1, node_2):
        if node_1.arg == node_2.arg:
            yield
        if node_1.left and node_2.left:
            yield from is_tree2_in_tree1_inside(node_1.left, node_2.left)
        if node_1.right and node_2.right:
            yield from is_tree2_in_tree1_inside(node_1.right, node_2.right)

    def lenght_tree(node):
        yield
        if node.left:
            yield from lenght_tree(node.left)
        if node.right:
            yield from lenght_tree(node.right)

    lenght_tree2 = 0
    for lenght in lenght_tree(node_2_):
        lenght_tree2 += 1
    for node in node_list:
        if node.arg == node_2_.arg:
            node_match = 0
            for result in is_tree2_in_tree1_inside(node, node_2_):
                node_match += 1
            if node_match == lenght_tree2:
                return True
    return False


assert is_tree2_in_tree1(Binary_tree_1.instances, c1) is True
assert is_tree2_in_tree1(Binary_tree_1.instances, c2) is False
