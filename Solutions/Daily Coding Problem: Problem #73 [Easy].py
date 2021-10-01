# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the head of a singly linked list, reverse it in-place.
#
#
# --------------------------------------------------------------------------------
#
#
class singly_linked_list(object):
    def __init__(self):
        super(singly_linked_list, self).__init__()
        self.next = None

    def reverse(head, next_head=None):
        if not head:
            return next_head
        new_head = head.next
        head.next = next_head
        return singly_linked_list.reverse(new_head, head)

    def get(head):
        def get(head, linked_list=[]):
            if not head:
                return linked_list
            linked_list.append(head)
            return get(head.next)
        return get(head)


a = singly_linked_list()
b = singly_linked_list()
c = singly_linked_list()
d = singly_linked_list()
f = singly_linked_list()

a.next = b
b.next = c
c.next = d
d.next = f

before_reverse = singly_linked_list.get(a)

singly_linked_list.reverse(a)

after_reverse = singly_linked_list.get(f)

assert before_reverse == after_reverse[::-1]
