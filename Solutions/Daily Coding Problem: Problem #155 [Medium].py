# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by MongoDB.
#
# Given a list of elements, find the majority element, which appears more than
# half the time (> floor(len(lst) / 2.0)).
#
# You can assume that such element exists.
#
# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
#
#
# --------------------------------------------------------------------------------
#
#
def find_majority_element(array):
    frequencies_dict = {}
    for item in array:
        if item not in frequencies_dict:
            frequencies_dict[item] = 1
        else:
            frequencies_dict[item] += 1
            if frequencies_dict[item] > float(len(array) / 2.0):
                return item


assert find_majority_element([1, 2, 1, 1, 3, 4, 1]) == 1
assert find_majority_element([1, 1, 1]) == 1
assert find_majority_element([1, 1, 2]) == 1
assert find_majority_element([]) is None
