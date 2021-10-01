# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a string and a pattern, find the starting indices of all occurrences of
# the pattern in the string. For example, given the string "abracadabra" and the
# pattern "abr", you should return [0, 7].
#
#
# --------------------------------------------------------------------------------
#
#
def find_pattern_position(string, pattern):
    pattern_starts_index_list = []
    for i in range(0, len(string) - (len(pattern) - 1)):
        if string[i:i + len(pattern)] == pattern:
            pattern_starts_index_list.append(i)
    return pattern_starts_index_list


assert find_pattern_position("abracadabra", "abr") == [0, 7]
