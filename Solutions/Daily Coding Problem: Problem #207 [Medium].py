# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Given an undirected graph G, check whether it is bipartite. Recall that a graph
# is bipartite if its vertices can be divided into two independent sets, U and V,
# such that no edge connects vertices of the same set.
#
#
# --------------------------------------------------------------------------------
#
#
class Node(object):
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.edges = []


def is_graph_bipartite(node):
    def through_graph(node_list, is_even=True):
        next_node_level_list = []
        for node_ in node_list:
            for next_node in node_.edges:
                if next_node not in odd_even_dict:
                    next_node_level_list.append(next_node)
                    odd_even_dict[next_node] = is_even
                else:
                    if odd_even_dict[next_node] != is_even:
                        return False
        if next_node_level_list:
            return through_graph(next_node_level_list, not is_even)
        else:
            return True

    odd_even_dict = {}
    return through_graph([node])


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)

a.edges = [b, c]
b.edges = [a, d]
c.edges = [a, d]
d.edges = [b, c, e]
e.edges = [d, f, g, h]
f.edges = [e]
g.edges = [e]
h.edges = [e, i]
i.edges = [h]

assert is_graph_bipartite(a) is True

b.edges = [a, d, c]
c.edges = [a, d, b]
assert is_graph_bipartite(a) is False
