# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.
#
#
# --------------------------------------------------------------------------------
#
#
def check_brackets(string):
    list = []
    for brackets in string:
        if brackets == "(" or brackets == "{" or brackets == "[":
            list.append(brackets)
        else:
            if brackets == ")":
                if list[-1] == "(":
                    list.pop()
                else:
                    return False
            elif brackets == "}":
                if list[-1] == "{":
                    list.pop()
                else:
                    return False
            elif brackets == "]":
                if list[-1] == "[":
                    list.pop()
                else:
                    return False
    if not list:
        return True
    else:
        return False


print(check_brackets("([])[]({})"))
print(check_brackets("([)]"))
print(check_brackets("((()"))
