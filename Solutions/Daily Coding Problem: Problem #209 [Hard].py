# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by YouTube.
#
# Write a program that computes the length of the longest common subsequence of
# three given strings. For example, given "epidemiologist", "refrigeration", and
# "supercalifragilisticexpialodocious", it should return 5, since the longest
# common subsequence is "eieio".
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product


def find_longest_common_subsequence(array):
    shortest_word = None
    len_shortest_word = None
    for word in array:
        if not len_shortest_word:
            len_shortest_word = len(word)
            shortest_word = word
        else:
            if len(word) < len_shortest_word:
                len_shortest_word = len(word)
                shortest_word = word
    array.remove(shortest_word)
    len_longest_common_subsequence = 0
    for p_ in product((0, 1), repeat=len_shortest_word):
        suitable = True
        text = ""
        for position, digit in enumerate(p_):
            if digit:
                text += shortest_word[position]
        array_position_dict = {}
        for item in array:
            array_position_dict[item] = 0
        for letter in text:
            for word in array:
                position = word.find(letter, array_position_dict[word])
                if position != -1:
                    array_position_dict[word] = position
                else:
                    suitable = False
                    break
            if not suitable:
                break
        if suitable:
            if len(text) > len_longest_common_subsequence:
                len_longest_common_subsequence = len(text)
    return len_longest_common_subsequence


assert find_longest_common_subsequence(["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"]) == 5
