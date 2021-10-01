# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Given a tree, find the largest tree/subtree that is a BST.
#
# Given a tree, return the size of the largest tree/subtree that is a BST.
#
#
# --------------------------------------------------------------------------------
#
#
class Node_list(type):
    instances = list()

    def __call__(cls, *args, **kwargs):
        instance = super(Node_list, cls).__call__(*args, **kwargs)
        cls.instances.append(instance)
        return instance


class Node(object, metaclass=Node_list):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


a = Node(50)
b = Node(25)
c = Node(75)
d = Node(12)
e = Node(500)
f = Node(62)
g = Node(87)
h = Node(100)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
g.right = h


def find_valid_BST(root_list):
    def subtree(root, flag):
        if root:
            if flag == "left" and root.arg > instance.arg:
                raise Exception
            if flag == "right" and root.arg < instance.arg:
                raise Exception
            yield root.arg
            if root.right:
                yield from subtree(root.right, flag)
            if root.left:
                yield from subtree(root.left, flag)

    def deepest_node_inside(root, depth=0):
        if not root.right and not root.left:
            return
        if root.right:
            if root.right.arg >= root.arg:
                deepest_node_inside(root.right)
            else:
                raise Exception
        if root.left:
            if root.left.arg <= root.arg:
                deepest_node_inside(root.left)
            else:
                raise Exception

    max_size = 0
    root_ = None
    for instance in root_list:
        try:
            left_subtree = []
            right_subtree = []
            for node in subtree(instance.left, "left"):
                left_subtree.append(node)
            for node in subtree(instance.right, "right"):
                right_subtree.append(node)
            deepest_node_inside(instance)
        except Exception:
            continue
        else:
            if (len(left_subtree) + len(right_subtree) + 1) >= max_size:
                max_size = len(left_subtree) + len(right_subtree) + 1
                root_ = instance
    return root_, max_size


assert find_valid_BST(Node.instances) == (c, 4)
