# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a linked list, sort it in O(n log n) time and constant space.
#
# For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99
# .
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


def quick_sort(head):
    def quick_sort_inside(array):
        position = len(array) // 2
        left = []
        right = []
        for item in array[:position] + array[position + 1:]:
            if item.arg < array[position].arg:
                left.append(item)
            else:
                right.append(item)
        if left:
            yield from quick_sort_inside(left)
        yield array[position]
        if right:
            yield from quick_sort_inside(right)
    node_list = []
    while head:
        node_list.append(head)
        head = head.next
    tmp = None
    for arr_ in quick_sort_inside(node_list):
        if tmp:
            tmp.next = arr_
        tmp = arr_
    tmp.next = None


a = linked_list(4)
b = linked_list(1)
c = linked_list(-3)
d = linked_list(99)

a.next = b
b.next = c
c.next = d

quick_sort(a)

assert c.next == b
assert b.next == a
assert a.next == d
assert d.next is None
