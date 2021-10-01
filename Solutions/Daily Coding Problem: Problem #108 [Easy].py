# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two strings A and B, return whether or not A can be shifted some number of
# times to get B.
#
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb
# , return false.
#
#
# --------------------------------------------------------------------------------
#
#
def is_shifted(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i:] + string_1[:i] == string_2:
            return True
    return False


assert is_shifted('abcde', 'cdeab') is True
assert is_shifted('abc', 'acb') is False
