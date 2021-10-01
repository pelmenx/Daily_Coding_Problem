# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a complete binary tree, count the number of nodes in faster than O(n)
# time. Recall that a complete binary tree has every level filled except the last,
# and the nodes in the last level are filled starting from the left.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self):
        super(Node, self).__init__()
        self.left = None
        self.right = None


def find_number_of_nodes(root):
    def find_number_of_nodes_(root, deapth=1, position=1):
        if root.right and not result:
            yield from find_number_of_nodes_(root.right, deapth + 1, position * 2)
        elif not root.right and not max_deapth and not result:
            yield None, deapth
        if root.right and max_deapth == deapth and not result:
            count = 0
            for i in range(0, deapth):
                count += 2 ** i
            yield count + position * 2, None
            return
        elif root.left and max_deapth == deapth and not result:
            count = 0
            for i in range(0, deapth):
                count += 2 ** i
            yield count + position * 2 - 1, None
            return
        elif root.left and not result:
            yield from find_number_of_nodes_(root.left, deapth + 1, position * 2 - 1)
    max_deapth = None
    result = None
    generator = find_number_of_nodes_(root)
    for sum_, deapth_ in generator:
        if deapth_:
            max_deapth = deapth_
        if sum_:
            result = sum_
    return result


a = Node()
b = Node()
c = Node()
a.left = b
a.right = c
d = Node()
e = Node()
b.left = d
b.right = e
f = Node()
g = Node()
c.left = f
c.right = g
h = Node()
i = Node()
d.left = h
d.right = i

j = Node()
k = Node()
e.left = j
e.right = k
ll = Node()
m = Node()
f.left = ll
f.right = m


assert find_number_of_nodes(a) == 13
