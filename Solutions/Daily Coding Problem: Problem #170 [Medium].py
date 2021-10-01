# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a start word, an end word, and a dictionary of valid words, find the
# shortest transformation sequence from start to end such that only one letter is
# changed at each step of the sequence, and each transformed word exists in the
# dictionary. If there is no possible transformation, return null. Each word in
# the dictionary have the same length as start and end and is lowercase.
#
# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop",
# "dat", "cat"}, return ["dog", "dot", "dat", "cat"].
#
# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
# return null as there is no possible transformation from dog to cat.
#
#
# --------------------------------------------------------------------------------
#
#
def transformation(start, end, dictionary):
    def transformation_inside(start_, end_, dictionary_, path):
        if start_ == end:
            yield path
        for i, item in enumerate(dictionary_):
            difference = 0
            for letter_1, letter_2 in zip(start_, item):
                if letter_1 != letter_2:
                    difference += 1
                    if difference > 1:
                        break
            if difference > 1:
                continue
            else:
                yield from transformation_inside(item, end, dictionary_[:i] + dictionary_[i + 1:], path + [item])
    min_path = None
    for path in transformation_inside(start, end, dictionary, [start]):
        if not min_path or len(path) < len(min_path):
            min_path = path
    if min_path:
        return min_path
    else:
        return None


assert transformation("dog", "cat", ["dot", "dop", "dat", "cat"]) == ['dog', 'dot', 'dat', 'cat']

assert transformation("dog", "cat", ["dot", "tod", "dat", "dar"]) is None
