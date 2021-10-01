# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# Given a linked list and a positive integer k, rotate the list to the right by k
# places.
#
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become
# 3 -> 5 -> 7 -> 7.
#
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4
# -> 5 -> 1 -> 2.
#
#
# --------------------------------------------------------------------------------
#
#
class linked_list(object):
    def __init__(self, arg):
        super(linked_list, self).__init__()
        self.arg = arg
        self.next = None


def rotate(head, k):
    def rotate_inside(head_, tail_, k_):
        if k_ == 0:
            return head_
        next = head_.next
        tail_.next = head_
        head_.next = None
        return rotate_inside(next, tail_.next, k_ - 1)

    tail = head
    i = 1
    while tail.next:
        tail = tail.next
        i += 1
    i -= k
    # print(i)
    new_head_ = rotate_inside(head, tail, i)
    return new_head_


a = linked_list(7)
b = linked_list(7)
c = linked_list(3)
d = linked_list(5)
a.next = b
b.next = c
c.next = d

e = linked_list(1)
f = linked_list(2)
g = linked_list(3)
h = linked_list(4)
i = linked_list(5)
e.next = f
f.next = g
g.next = h
h.next = i

new_head = rotate(a, 2)
assert new_head == c
assert new_head.next == d
assert new_head.next.next == a
assert new_head.next.next.next == b
assert new_head.next.next.next.next is None

new_head = rotate(e, 3)
assert new_head == g
assert new_head.next == h
assert new_head.next.next == i
assert new_head.next.next.next == e
assert new_head.next.next.next.next == f
assert new_head.next.next.next.next.next is None
