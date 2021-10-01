# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction, then
# return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
# "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath',
# 'and', 'beyond'].
#
#
# --------------------------------------------------------------------------------
#
#
def find_words(string, set_of_words):
    tmp_words = ""
    words_list = []
    for letter in string:
        tmp_words += letter
        if tmp_words in set_of_words:
            words_list.append(tmp_words)
            tmp_words = ""
    if not words_list:
        return None
    else:
        return words_list


print(find_words("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
print(find_words("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
print(find_words("bedbathandbeyonds", ['quick', 'brown', 'the', 'fox']))
