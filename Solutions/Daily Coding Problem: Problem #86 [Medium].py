# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string of parentheses, write a function to compute the minimum number of
# parentheses to be removed to make the string valid (i.e. each open parenthesis
# is eventually closed).
#
# For example, given the string "()())()", you should return 1. Given the string
# ")(", you should return 2, since we must remove all of them.
#
#
# --------------------------------------------------------------------------------
#
#
def parentheses(string):
    list_of_parentheses = []
    counter = 0
    for item in string:
        if item == "(":
            list_of_parentheses.append(item)
        else:
            if list_of_parentheses:
                list_of_parentheses.pop()
            else:
                counter += 1
    return len(list_of_parentheses) + counter


assert parentheses("()())()") == 1
assert parentheses(")(") == 2
