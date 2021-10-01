# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Write a program that checks whether an integer is a palindrome. For example, 121
# is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the
# integer into a string.
#
#
# --------------------------------------------------------------------------------
#
#
def is_polindrome(integer):
    digits_list = []
    while integer > 0:
        digits_list.append(integer % 10)
        integer = integer // 10

    left = digits_list[:int(len(digits_list) / 2)]
    right = digits_list[-int(len(digits_list) / 2):]
    right.reverse()
    if left == right:
        return True
    else:
        return False


assert is_polindrome(1221) is True
assert is_polindrome(121) is True
assert is_polindrome(888) is True
assert is_polindrome(678) is False
