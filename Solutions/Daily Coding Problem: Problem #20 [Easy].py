# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.
#
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
# node with value 8.
#
# In this example, assume nodes with the same value are the exact same node
# objects.
#
# Do this in O(M + N) time (where M and N are the lengths of the lists) and
# constant space.
#
#
# --------------------------------------------------------------------------------
#
#
def find_intersecting_node(linked_lists_value):
    checked_nodes_value = []
    for i in range(0, len(linked_lists_value)):
        for node in linked_lists_value[i]:
            if linked_lists_value[i].get(node) not in checked_nodes_value:
                checked_nodes_value.append(linked_lists_value[i].get(node))
            else:
                return linked_lists_value[i].get(node)


linked_lists_value = [{"a": 3, "b": 7, "c": 8, "d": 10}, {"a": 99, "b": 1, "c": 8, "d": 10}]

print(find_intersecting_node(linked_lists_value))
