# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a word W and a string S, find all starting indices in S which are anagrams
# of W.
#
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import permutations


def find_anagrams(word, string):
    anagrams = {}
    anagrams_position = []
    for p_ in permutations(word, len(word)):
        p_ = "".join(p_)
        anagrams[p_] = None
    for i in range(len(string[:-len(word) + 1])):
        if string[i:i + len(word)] in anagrams:
            anagrams_position.append(i)
    return anagrams_position


assert find_anagrams("ab", "abxaba") == [0, 3, 4]
