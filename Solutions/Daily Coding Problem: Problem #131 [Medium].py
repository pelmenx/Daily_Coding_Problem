# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Snapchat.
#
# Given the head to a singly linked list, where each node also has a “random”
# pointer that points to anywhere in the linked list, deep clone the list.
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
        self.random = None


def deepcopy(root):
    def make_copy_next(root_, head=None, tmp=None):
        node_dict[root_] = Node(root_.arg)
        if not head:
            head = node_dict[root_]
        node_list.append(node_dict[root_])
        if tmp:
            tmp.next = node_dict[root_]
        if not root_.next:
            return head
        if root_.next:
            tmp = node_dict[root_]
            return make_copy_next(root_.next, head, tmp)

    def make_copy_random(root_):
        randon_node = root_.random
        tmp_root = root
        i = 0
        while True:
            if tmp_root == randon_node:
                break
            else:
                i += 1
                tmp_root = tmp_root.next
        node_dict[root_].random = node_list[i]
        if root_.next:
            return make_copy_random(root_.next)
    node_dict = {}
    node_list = []
    head_node = make_copy_next(root)
    make_copy_random(root)
    return head_node


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

a.random = e
b.random = d
c.random = c
d.random = b
e.random = a

new_sll = deepcopy(a)
assert a.arg == new_sll.arg
assert a.random.arg == new_sll.random.arg
assert a.next.arg == new_sll.next.arg
assert a.next.random.arg == new_sll.next.random.arg
assert a.next.next.arg == new_sll.next.next.arg
assert a.next.next.random.arg == new_sll.next.next.random.arg
assert a.next.next.next.arg == new_sll.next.next.next.arg
assert a.next.next.next.random.arg == new_sll.next.next.next.random.arg
assert a.next.next.next.next.arg == new_sll.next.next.next.next.arg
assert a.next.next.next.next.random.arg == new_sll.next.next.next.next.random.arg
