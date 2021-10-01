# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# Generate a finite, but an arbitrarily large binary tree quickly in O(1).
#
# That is, generate() should return a tree whose size is unbounded but finite.
#
#
# --------------------------------------------------------------------------------
#
#
from random import random, randint


class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def make_tree(n):
    def add_side():
        side = random()
        random_node = randint(0, i - 1)
        if side < 0.5:
            if node_dict[random_node].left:
                return add_side()
            else:
                node_dict[random_node].left = node_dict[i]
        elif side > 0.5:
            if node_dict[random_node].right:
                return add_side()
            else:
                node_dict[random_node].right = node_dict[i]
        else:
            return add_side()

    node_dict = {}
    for i in range(n):
        node_dict[i] = Node(int(random() * (n * 10)))
        if i > 0:
            add_side()


make_tree(1000000)
