# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yahoo.
#
# Write an algorithm that computes the reversal of a directed graph. For example,
# if a graph consists of A -> B -> C, it should become A <- B <- C.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.next = None


def reverse_linked_list(root):
    prev_node = None

    while root:
        tmp = root.next
        root.next = prev_node
        prev_node = root
        root = tmp


a = Node("A")
b = Node("B")
c = Node("C")
a.next = b
b.next = c

reverse_linked_list(a)

assert c.next == b
assert b.next == a
assert a.next is None
