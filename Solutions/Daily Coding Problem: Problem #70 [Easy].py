# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.
#
#
# --------------------------------------------------------------------------------
#
#
def perfect_number(n):
    amount = 0
    for number in str(n):
        amount += int(number)
    if amount == 10:
        return n
    elif amount > 10:
        return None
    else:
        last_digit = 10 - amount
        return int(str(n) + str(last_digit))


assert perfect_number(1) == 19
assert perfect_number(2) == 28
assert perfect_number(12) == 127
assert perfect_number(10) == 109
assert perfect_number(23) == 235
assert perfect_number(19) == 19
assert perfect_number(29) is None
