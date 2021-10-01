# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You're given a string consisting solely of (, ), and *. * can represent either a
# (, ), or an empty string. Determine whether the parentheses are balanced.
#
# For example, (()* and (*) are balanced. )*( is not balanced.
#
#
# --------------------------------------------------------------------------------
#
#
def is_balanced(string):
    def check_balance(array):
        if not array:
            yield True
        elif array[0] == "(" and array[-1] == ")":
            yield from check_balance(array[1:-1])
        elif array[0] == "*":
            yield from check_balance(array[1:])
            yield from check_balance(["("] + array[1:])
            yield from check_balance([")"] + array[1:])
        elif array[-1] == "*":
            yield from check_balance(array[:-1])
            yield from check_balance(array[:-1] + ["("])
            yield from check_balance(array[:-1] + [")"])

    string = list(string)
    result = False
    for output in check_balance(string):
        result = output or result
    return result


assert is_balanced('(()*') is True
assert is_balanced('(*)') is True
assert is_balanced(')*(') is False
