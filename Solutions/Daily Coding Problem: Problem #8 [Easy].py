# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0(a)
#   /    \
#  1(b)  0(c)
#       /   \
#      1(d) 0(e)
#     /  \
#  1(f)  1(g)
#
#
#
# --------------------------------------------------------------------------------
#
#
def count_unival_subtree(graph_tree, graph_tree_value):
    roads = make_roads(graph_tree)
    bottom_leafs = check_bottom_leafs(graph_tree, roads)
    count = 0
    for leaf in bottom_leafs:
        count += counting(leaf, bottom_leafs, graph_tree_value)
    return count


def make_roads(graph_tree):
    roads = []
    for leaf in graph_tree:
        try:
            for item in graph_tree.get(leaf):
                roads.append([leaf, item])
        except TypeError:
            pass

    return roads


def check_bottom_leafs(graph_tree, roads, tmp=[]):
    bottom_leafs = {}
    for leaf in graph_tree:
        for road in roads:
            if road[0] in tmp:
                tmp.append(road[1])
            elif road[0] == leaf:
                tmp.append(road[1])
        if not tmp:
            bottom_leafs[leaf] = None
        else:
            bottom_leafs[leaf] = tmp
        tmp = []
    return bottom_leafs


def counting(leaf, bottom_leafs, graph_tree_value, count=0):
    if bottom_leafs.get(leaf) is None:
        count += 1
        return count
    else:
        for item in bottom_leafs.get(leaf):
            if graph_tree_value[item] != graph_tree_value[leaf]:
                return count
    count += 1
    return count


graph_tree = {"a": ["b", "c"], "b": None, "c": ["d", "e"], "d": ["f", "g"], "e": None, "f": None, "g": None}
graph_tree_value = {"a": 0, "b": 1, "c": 0, "d": 1, "e": 0, "f": 1, "g": 1}


print(count_unival_subtree(graph_tree, graph_tree_value))
