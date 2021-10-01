# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Square.
#
# Given a string and a set of characters, return the shortest substring containing
# all the characters in the set.
#
# For example, given the string "figehaeci" and the set of characters {a, e, i},
# you should return "aeci".
#
# If there is no substring containing all the characters in the set, return null.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def shortest_substring(string, set):
    def shortest_substring_inside(string_inside):
        if len(string_inside) < len(set):
            return
        if not string_inside:
            return
        for i in range(len(set), len(string_inside) + 1):
            check = True
            for item in set:
                if item not in string_inside[:i]:
                    check = False
                    break
            if check:
                yield string_inside[:i]
        yield from shortest_substring_inside(string_inside[1:])
    substring_shortest = copy.deepcopy(string)
    substring = None
    for substring in shortest_substring_inside(string):
        if len(substring) < len(substring_shortest):
            substring_shortest = substring
    if substring:
        print(substring_shortest)
        return(substring_shortest)
    else:
        return None


shortest_substring("figehaeci", {"a", "e", "i"})
