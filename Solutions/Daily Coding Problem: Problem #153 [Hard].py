# Good morning! Here's your coding interview problem for today.
#
# Find an efficient algorithm to find the smallest distance (measured in number of
# words) between any two given words in a string.
#
# For example, given words "hello", and "world" and a text content of "dog cat
# hello cat dog dog hello cat world", return 1 because there's only one word "cat"
# in between the two words.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def number_of_words_between(string, word_1, word_2):
    string_list = string.split()
    word_1_position = []
    word_2_position = []
    for i, word in enumerate(string_list):
        if word == word_1:
            word_1_position.append(i)
        elif word == word_2:
            word_2_position.append(i)
    min = maxsize
    for position_1 in word_1_position:
        for position_2 in word_2_position:
            if abs(position_1 - position_2) < min:
                min = abs(position_1 - position_2)
    if min == maxsize:
        return None
    else:
        return min - 1


assert number_of_words_between("dog cat hello cat dog dog hello cat world", "hello", "world") == 1
