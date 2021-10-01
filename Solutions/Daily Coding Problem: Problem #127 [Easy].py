# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Let's represent an integer in a linked list format by having each node represent
# a digit in the number. The nodes make up the number in reversed order.
#
# For example, the following linked list:
#
# 1 -> 2 -> 3 -> 4 -> 5
#
#
# is the number 54321.
#
# Given two linked lists in this format, return their sum in the same linked list
# format.
#
# For example, given
#
# 9 -> 9
#
#
# 5 -> 2
#
#
# return 124 (99 + 25) as:
#
# 4 -> 2 -> 1
#
#
#
# --------------------------------------------------------------------------------
#
#
class linked_list_1(object):
    head = None

    def __init__(self, arg):
        super(linked_list_1, self).__init__()
        self.arg = arg
        self.next = None
        if not linked_list_1.head:
            linked_list_1.head = self


class linked_list_2(object):
    head = None

    def __init__(self, arg):
        super(linked_list_2, self).__init__()
        self.arg = arg
        self.next = None
        if not linked_list_2.head:
            linked_list_2.head = self


class linked_list_3(object):
    head = None

    def __init__(self, arg):
        super(linked_list_3, self).__init__()
        self.arg = arg
        self.next = None
        if not linked_list_3.head:
            linked_list_3.head = self


def get_number(first, second):
    number_1 = ''
    number_2 = ''
    while first or second:
        if first:
            number_1 += str(first.arg)
            first = first.next
        if second:
            number_2 += str(second.arg)
            second = second.next
    number_1 = int(number_1[::-1])
    number_2 = int(number_2[::-1])
    sum = str(number_1 + number_2)
    linked_list_3_dict = {}
    for i, item in enumerate(sum):
        linked_list_3_dict[i] = linked_list_3(int(item))
        linked_list_3.head = linked_list_3_dict[i]
        if i > 0:
            linked_list_3_dict[i].next = linked_list_3_dict[i - 1]


a = linked_list_1(9)
b = linked_list_1(9)
a.next = b

c = linked_list_2(5)
d = linked_list_2(2)
c.next = d


get_number(linked_list_1.head, linked_list_2.head)
assert linked_list_3.head.arg == 4
assert linked_list_3.head.next.arg == 2
assert linked_list_3.head.next.next.arg == 1
