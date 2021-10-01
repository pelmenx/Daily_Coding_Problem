# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Square.
#
# Given a list of words, return the shortest unique prefix of each word. For
# example, given the list:
#
#  * dog
#  * cat
#  * apple
#  * apricot
#  * fish
#
# Return the list:
#
#  * d
#  * c
#  * app
#  * apr
#  * f
#
#
# --------------------------------------------------------------------------------
#
#
def unique_prefix(word_list):
    def find_prefix():
        tmp_prefix = []
        for i, item in enumerate(prefix_list):
            if item in tmp_prefix:
                j = prefix_list.index(item)
                prefix_list[i] = word_list[i][0: len(prefix_list[i]) + 1]
                prefix_list[j] = word_list[j][0: len(prefix_list[j]) + 1]
                return find_prefix()
            else:
                tmp_prefix.append(item)
    prefix_list = []
    for word in word_list:
        prefix_list.append(word[0])
    find_prefix()
    return prefix_list


assert unique_prefix(['dog', 'cat', 'apple', 'apricot', 'fish']) == ['d', 'c', 'app', 'apr', 'f']
