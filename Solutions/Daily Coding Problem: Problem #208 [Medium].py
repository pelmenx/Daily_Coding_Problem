# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by LinkedIn.
#
# Given a linked list of numbers and a pivot k, partition the linked list so that
# all nodes less than k come before nodes greater than or equal to k.
#
# For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution
# could be 1 -> 0 -> 5 -> 8 -> 3.
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


def rearange_linled_list(node, pivot):
    first_lesser_node = None
    last_lesser_node = None
    first_grater_or_equal_node = None
    last_grater_or_equal_node = None

    while node:
        if node.arg < pivot:
            if not first_lesser_node:
                first_lesser_node = node
            if not last_lesser_node:
                last_lesser_node = node
            else:
                last_lesser_node.next = node
                last_lesser_node = node
        else:
            if not first_grater_or_equal_node:
                first_grater_or_equal_node = node
            if not last_grater_or_equal_node:
                last_grater_or_equal_node = node
            else:
                last_grater_or_equal_node.next = node
                last_grater_or_equal_node = node
        node = node.next
    last_lesser_node.next = first_grater_or_equal_node


a = Node(5)
b = Node(1)
c = Node(8)
d = Node(0)
e = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e

rearange_linled_list(a, 3)
assert b.arg == 1
assert b.next.arg == 0
assert b.next.next.arg == 5
assert b.next.next.next.arg == 8
assert b.next.next.next.next.arg == 3
assert b.next.next.next.next.next is None
