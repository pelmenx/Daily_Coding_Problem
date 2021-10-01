# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, swap every two nodes and return its
# head.
#
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
#
#
# --------------------------------------------------------------------------------
#
#
class singly_linked_list(object):

    def __init__(self, arg):
        super(singly_linked_list, self).__init__()
        self.arg = arg
        self.next = None


def swap(node):
    if node.next:
        head = node.next
    else:
        return None
    while True:
        tmp = node.next
        tmp_ = node.next.next
        if not tmp_:
            node.next = None
            tmp.next = node
            return head
        elif not node.next.next.next:
            node.next = node.next.next
            tmp.next = node
            return head
        else:
            node.next = node.next.next.next
            tmp.next = node
        node = tmp_


a = singly_linked_list(1)
b = singly_linked_list(2)
c = singly_linked_list(3)
d = singly_linked_list(4)
e = singly_linked_list(5)

a.next = b
b.next = c
c.next = d
d.next = e

head = swap(a)

assert head.arg == 2
assert head.next.arg == 1
assert head.next.next.arg == 4
assert head.next.next.next.arg == 3
assert head.next.next.next.next.arg == 5
