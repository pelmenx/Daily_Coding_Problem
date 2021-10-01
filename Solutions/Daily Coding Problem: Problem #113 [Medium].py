# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string of words delimited by spaces, reverse the words in string. For
# example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation
# in-place?
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_word(string):
    string = list(string)
    left = 0
    right = len(string) - 1
    old_left = 0
    old_right = len(string)
    while left <= right:
        if string[left] == " " and string[right] == " ":
            string = string[:old_left] + string[right + 1:old_right] + string[left:right + 1] + string[old_left:left] + string[old_right:]
            tmp = left
            left = old_left + old_right - right
            right = old_right - ((tmp - old_left) + 2)
            old_left = left
            old_right = right + 1
        elif string[left] != " " and string[right] != " ":
            left += 1
            right -= 1
        elif string[left] == " " and string[right] != " ":
            right -= 1
        elif string[right] == " " and string[left] != " ":
            left += 1
    string = "".join(string)
    return string


assert reverse_word("hello world here") == "here world hello"
