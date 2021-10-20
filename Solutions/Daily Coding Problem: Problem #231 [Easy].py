# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by IBM.
#
# Given a string with repeated characters, rearrange the string so that no two
# adjacent characters are the same. If this is not possible, return None.
#
# For example, given "aaabbc", you could return "ababac". Given "aaab", return
# None.
#
#
# --------------------------------------------------------------------------------
#
#
from itertools import product


def replace(word):
    letters_dict = {}
    for letter in word:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    letters_list_count = list(letters_dict.values())
    letters_list = []
    for letter in letters_dict:
        letters_list.append([letter] * letters_dict[letter])
    if max(letters_list_count) <= sum(letters_list_count) - max(letters_list_count) + 1:
        for i in range(2, len(letters_list) + 1):
            for product_ in product((range(i)), repeat=len(letters_list)):
                flag = True
                if len(set(product_)) == i:
                    tmp_dict = {}
                    for j in range(i):
                        tmp_dict[j] = []
                    for label, block in zip(product_, letters_list):
                        tmp_dict[label] += block
                    block_list = list(tmp_dict.values())
                    block_lenght_list = []
                    for block in block_list:
                        block_lenght_list.append(len(block))
                    max_block_lenght = max(block_lenght_list)
                    for length in block_lenght_list:
                        if length == max_block_lenght or length + 1 == max_block_lenght:
                            pass
                        else:
                            flag = False
                            break
                    if flag:
                        word = ''
                        for i in range(max_block_lenght):
                            for block in block_list:
                                if len(block) > i:
                                    word += block[i]
                        if word[-2] == word[-1]:
                            word = word[-1] + word[:-1]
                        return word
                    else:
                        continue
    else:
        return None


assert replace("aaabbc") == "ababac"
assert replace("aaabbbcccc") == "cabcabcabc"
assert replace("aaab") is None
