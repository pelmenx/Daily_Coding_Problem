# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string of parentheses, find the balanced string that can be produced
# from it using the minimum number of insertions and deletions. If there are
# multiple solutions, return any of them.
#
# For example, given "(()", you could return "(())". Given "))()(", you could
# return "()()()()".
#
#
# --------------------------------------------------------------------------------
#
#


def solve_parentheses(parentheses):
    def solve_with_deletions(parentheses_):
        tmp = []
        result = []
        for item in parentheses_:
            if tmp:
                if item == ")" and tmp[-1] == "(":
                    tmp.pop()
                    for i in range(len(result) - 1, -1, -1):
                        if result[i] == "*":
                            result[i] = "("
                            result.append(")")
                            break

                else:
                    tmp.append(item)
                    result.append("*")
            else:
                tmp.append(item)
                result.append("*")
        for i in range(len(result) - 1, -1, -1):
            if result[i] == "*":
                result.pop(i)
        print("".join(result))

    solve_with_deletions(parentheses)


solve_parentheses("(()")
solve_parentheses("))()(")
solve_parentheses("()(()))")
