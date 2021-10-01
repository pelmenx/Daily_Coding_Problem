# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# Given a list of words, find all pairs of unique indices such that the
# concatenation of the two words is a palindrome.
#
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0),
# (2, 3)].
#
#
# --------------------------------------------------------------------------------
#
#
def concatenation_polindrome(array):
    def is_polindrome(word):
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    polindme_list = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if is_polindrome(array[i] + array[j]):
                polindme_list.append((i, j))
            if is_polindrome(array[j] + array[i]):
                polindme_list.append((j, i))
    return polindme_list


assert concatenation_polindrome(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
