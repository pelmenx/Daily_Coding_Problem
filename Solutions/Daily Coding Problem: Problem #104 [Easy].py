# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Determine whether a doubly linked list is a palindrome. What if it’s singly
# linked?
#
# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
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


def is_linked_list_is_a_polindrome(node):
    def check_list(node_):
        linked_list_.append(node_.arg)
        if node_.next:
            return check_list(node_.next)
        else:
            if len(linked_list_) % 2 == 0:
                left = linked_list_[:len(linked_list_) // 2]
                right = linked_list_[len(linked_list_) // 2:]
                if left == right[::-1]:
                    return True
                else:
                    return False
            else:
                left = linked_list_[:len(linked_list_) // 2]
                right = linked_list_[len(linked_list_) // 2 + 1:]
                if left == right[::-1]:
                    return True
                else:
                    return False
    linked_list_ = []
    return check_list(node)


a = linked_list(1)
b = linked_list(4)
c = linked_list(3)
d = linked_list(4)
e = linked_list(1)
a.next = b
b.next = c
c.next = d
d.next = e

assert is_linked_list_is_a_polindrome(a) is True
