# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string which we can delete at most k, return whether you can make a
# palindrome.
#
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get
# 'waterretaw'.
#
#
# --------------------------------------------------------------------------------
#
#
def is_palindrome(string, k):
    def get_substring_(string_, rep=0):
        if rep == k + 1:
            return
        yield string_
        for i in range(0, len(string_)):
            yield from get_substring_(string_[:i] + string_[i + 1:], rep + 1)
    for substring in get_substring_(string):
        if len(substring) % 2 == 0:
            left = substring[:len(substring) // 2]
            right = substring[len(substring) // 2:]
            right = right[::-1]
            if left == right:
                return True
        else:
            left = substring[:len(substring) // 2]
            right = substring[len(substring) // 2 + 1:]
            right = right[::-1]
            if left == right:
                return True
    return False


assert is_palindrome('waterrfetawx', 2) is True
assert is_palindrome('waterrfetawx', 1) is False
