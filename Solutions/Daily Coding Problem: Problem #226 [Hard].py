# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# You come across a dictionary of sorted words in a language you've never seen
# before. Write a program that returns the correct order of letters in this
# language.
#
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return
# ['x', 'z', 'w', 'y'].
#
#
# --------------------------------------------------------------------------------
#
#
def make_alphabet(array):
    unique_letter_set = set()
    alphabet_list = []
    alphabet_unsure_list = []

    def make_alphabet_(i=1):
        if i > max_len:
            return
        for word1, word2 in zip(array[:-1], array[1:]):
            if len(word1) < i or len(word2) < i:
                continue
            if word1[:i - 1] == word2[:i - 1] and word1[:i][-1] != word2[:i][-1]:
                if word1[:i][-1] not in alphabet_list and word2[:i][-1] not in alphabet_list:
                    alphabet_list.append(word1[:i][-1])
                    alphabet_list.append(word2[:i][-1])
                elif word1[:i][-1] in alphabet_list and word2[:i][-1] not in alphabet_list:
                    if alphabet_list[-1] == word1[:i][-1]:
                        alphabet_list.append(word2[:i][-1])
                    else:
                        if [word1[:i][-1], word2[:i][-1]] not in alphabet_unsure_list:
                            alphabet_unsure_list.append([word1[:i][-1], word2[:i][-1]])
                elif word1[:i][-1] not in alphabet_list and word2[:i][-1] in alphabet_list:
                    if alphabet_list[0] == word2[:i][-1]:
                        alphabet_list.insert(0, word1[:i][-1])
                    else:
                        if [word1[:i][-1], word2[:i][-1]] not in alphabet_unsure_list:
                            alphabet_unsure_list.append([word1[:i][-1], word2[:i][-1]])
        return make_alphabet_(i + 1)

    def resolve_the_alphabetical_unsurence():
        if len(alphabet_list) == len(unique_letter_set):
            return

        for i in range(len(alphabet_unsure_list) - 1, -1, -1):
            if alphabet_unsure_list[i][0] in alphabet_list and alphabet_unsure_list[i][1] in alphabet_list:
                alphabet_unsure_list.pop(i)

        for i, item1 in enumerate(alphabet_unsure_list):
            for j, item2 in enumerate(alphabet_unsure_list[i + 1:]):
                if item2[1] == item1[0] and item2[0] != item1[1]:
                    if item2[0] in alphabet_list and item1[1] in alphabet_list:
                        if alphabet_list.index(item2[0]) + 1 == alphabet_list.index(item1[1]):
                            alphabet_list.insert(alphabet_list.index(item1[1]), item2[1])
                            alphabet_unsure_list.pop(i)
                            alphabet_unsure_list.pop(j)
                            return resolve_the_alphabetical_unsurence()

                elif item1[1] == item2[0] and item1[0] != item2[1]:
                    if item1[0] in alphabet_list and item2[1] in alphabet_list:
                        if alphabet_list.index(item1[0]) + 1 == alphabet_list.index(item2[1]):
                            alphabet_list.insert(alphabet_list.index(item2[1]), item1[1])
                            alphabet_unsure_list.pop(i)
                            alphabet_unsure_list.pop(j)
                            return resolve_the_alphabetical_unsurence()
    max_len = 0
    for item in array:
        if len(item) > max_len:
            max_len = len(item)
        for letter in item:
            if letter not in unique_letter_set:
                unique_letter_set.add(letter)
    make_alphabet_()
    resolve_the_alphabetical_unsurence()

    return alphabet_list


assert make_alphabet(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']) == ['x', 'z', 'w', 'y']
