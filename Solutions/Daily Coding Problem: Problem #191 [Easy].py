# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given a collection of intervals, find the minimum number of intervals you need
# to remove to make the rest of the intervals non-overlapping.
#
# Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered
# overlapping.
#
# For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last
# interval can be removed and the first two won't overlap.
#
# The intervals are not necessarily sorted in any order.
#
#
# --------------------------------------------------------------------------------
#
#
def remove_overlap(sets):
    def remove_overlap_inside(sets):
        overlapping = False
        for i, set1 in enumerate(sets):
            for j, set2 in enumerate(sets[i + 1:]):
                if set1[0] < set2[0] < set1[1] or set1[0] < set2[1] < set1[1] or set2[0] < set1[0] < set2[1] or set2[0] < set1[1] < set2[1]:
                    yield from remove_overlap_inside(sets[:j + 1] + sets[j + 2:])
                    yield from remove_overlap_inside(sets[:i] + sets[i + 1:])
                    overlapping = True
        if overlapping is False:
            yield sets
    number_subsets_removed = len(sets)
    for subset in remove_overlap_inside(sets):
        if len(subset) < number_subsets_removed:
            number_subsets_removed = len(subset)
    number_subsets_removed = len(sets) - number_subsets_removed
    return number_subsets_removed


assert remove_overlap([(0, 1), (1, 2)]) == 0
assert remove_overlap([(7, 9), (2, 4), (5, 8)]) == 1
assert remove_overlap([(7, 9), (2, 4), (5, 8), (1, 3)]) == 2
