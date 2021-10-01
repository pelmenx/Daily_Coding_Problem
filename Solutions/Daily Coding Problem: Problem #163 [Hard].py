# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# Given an arithmetic expression in Reverse Polish Notation
# [https://en.wikipedia.org/wiki/Reverse_Polish_notation], write a program to
# evaluate it.
#
# The expression is given as a list of numbers and operands. For example: [5, 3,
# '+'] should return 5 + 3 = 8.
#
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should
# return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) =
# 5.
#
# You can assume the given expression is always valid.
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_Polish_notation(array, position=0):
    if len(array) == 1:
        return array[0]
    for i in range(position, len(array)):
        if isinstance(array[i], str):
            left = array[i - 2]
            right = array[i - 1]
            operand = array[i]
            if operand == "+":
                result = left + right
            elif operand == "-":
                result = left - right
            elif operand == "*":
                result = left * right
            elif operand == "/":
                result = left / right
            return reverse_Polish_notation(array[:i - 2] + [result] + array[i + 1:], i - 1)


assert reverse_Polish_notation([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5
