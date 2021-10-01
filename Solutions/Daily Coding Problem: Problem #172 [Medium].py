# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Given a string s and a list of words words, where each word is the same length,
# find all starting indices of substrings in sthat is a concatenation of every
# word in words exactly once.
#
# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return
# [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.
#
# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there
# are no substrings composed of "dog" and "cat" in s.
#
# The order of the indices does not matter.
#
#
# --------------------------------------------------------------------------------
#
#
def find_concatenation(string, words):
    def find_all_concatenation(words_list, st_=""):
        if not words_list:
            yield st_
        for i, word in enumerate(words_list):
            yield from find_all_concatenation(words_list[:i] + words_list[i + 1:], st_ + word)
    concatenation_list = []
    for string_ in find_all_concatenation(words):
        concatenation_list.append(string_)
    result = []
    for i in range(0, len(string) - len(concatenation_list[0]) + 1):
        for item in concatenation_list:
            if string[i:i + len(concatenation_list[0])] == item:
                result.append(i)
    return result


assert find_concatenation("dogcatcatcodecatdog", ["cat", "dog"]) == [0, 13]
