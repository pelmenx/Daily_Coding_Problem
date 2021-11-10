# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Fitbit.
#
# Given a linked list, rearrange the node values such that they appear in
# alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3
# -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg) -> None:
        self.val = arg
        self.next = None

    def __repr__(self) -> str:
        return repr(self.val)


def get_list_of_nodes(root):
    nodes_list = []
    while root:
        nodes_list.append(root)
        root = root.next
    return nodes_list


def rearrange(nodes_list):
    nodes_list.sort(key=lambda x: x.val)
    left = 0
    if len(nodes_list) % 2 == 1:
        right = len(nodes_list) // 2 + 1
    else:
        right = len(nodes_list) // 2
    altering_list = []
    i = 0
    for i in range(len(nodes_list)):
        if i % 2 == 0:
            altering_list.append(nodes_list[left])
            left += 1
        else:
            altering_list.append(nodes_list[right])
            right += 1
        if len(altering_list) > 1:
            altering_list[-2].next = altering_list[-1]
        i += 1
    altering_list[-1].next = None
    print(altering_list)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

rearrange(get_list_of_nodes(a))
assert a.next == d
assert d.next == b
assert b.next == e
assert e.next == c
assert c.next is None
