# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, carrace should return true, since it can be rearranged to form
# racecar, which is a palindrome. daily should return false, since there's no
# rearrangement that can form a palindrome.
#
#
# --------------------------------------------------------------------------------
#
#
def can_be_polindrome(string):
    letter_dict = {}
    for letter in string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict.pop(letter)
    if len(letter_dict) <= 1:
        return True
    else:
        return False


assert can_be_polindrome("racecar") is True
assert can_be_polindrome("daily") is False
