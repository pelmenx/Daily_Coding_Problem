# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given k sorted singly linked lists, write a function to merge all the lists into
# one sorted singly linked list.
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

    def get(head):
        def get(head, linked_list=[]):
            if not head:
                return linked_list
            linked_list.append(head)
            return get(head.next)
        return get(head)


def merge_nodes(*nodes):
    def merge_two_nodes(node_1, node_2, start=None):
        if node_1[0].arg <= node_2[0].arg:
            if not start:
                start = node_1[0]
            for i, item in enumerate(node_1):
                if item.next:
                    if item.arg <= node_2[0].arg <= item.next.arg:
                        node_2[0].next = item.next
                        item.next = node_2[0]
                        return merge_two_nodes([node_2[0]] + node_1[i + 1:], node_2[1:], start)
                else:
                    item.next = node_2[0]
                    return(singly_linked_list.get(start))

        else:
            if not start:
                start = node_1[0]
            for i, item in enumerate(node_2):
                if item.next:
                    if item.arg <= node_1[0].arg <= item.next.arg:
                        node_1[0].next = item.next
                        item.next = node_1[0]
                        return merge_two_nodes(node_1[1:], [node_1[0]] + node_2[i + 1:], start)
                else:
                    item.next = node_1[0]
                    return(singly_linked_list.get(start))

    if len(nodes) == 1:
        return nodes
    elif len(nodes) == 2:
        return merge_two_nodes(nodes[0], nodes[1])
    else:
        node = merge_two_nodes(nodes[0], nodes[1])
        return merge_nodes(node, nodes[2:])


a = singly_linked_list(1)
b = singly_linked_list(2)
c = singly_linked_list(5)
d = singly_linked_list(6)
e = singly_linked_list(8)


a.next = b
b.next = c
c.next = d
d.next = e

f = singly_linked_list(3)
g = singly_linked_list(4)
h = singly_linked_list(7)
i = singly_linked_list(9)
j = singly_linked_list(10)

f.next = g
g.next = h
h.next = i
i.next = j


assert merge_nodes(singly_linked_list.get(a), singly_linked_list.get(f)) == [a, b, f, g, c, d, h, e, i, j]
