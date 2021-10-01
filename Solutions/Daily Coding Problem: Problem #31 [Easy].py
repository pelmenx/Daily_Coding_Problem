# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the
# other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
#
# Given two strings, compute the edit distance between them.
#
#
# --------------------------------------------------------------------------------
#
#
def distance_between_two_strings(string1, string2):
    print(string1, string2)
    if string1 == string2:
        return 0
    elif not string1:
        return len(string2)
    elif not string2:
        return len(string1)

    if string1[0] == string2[0]:
        return distance_between_two_strings(string1[1:], string2[1:])

    return 1 + min(
        distance_between_two_strings(string1[1:], string2),      # deletion from string1
        distance_between_two_strings(string1, string2[1:]),      # addition to string1
        distance_between_two_strings(string1[1:], string2[1:]))  # modification to string1


print(distance_between_two_strings("asd", "qwe"))
