# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or 0.
#
#
# --------------------------------------------------------------------------------
#
#
def return_number(x, y, b):
    return (x * b + y * abs(b - 1))


assert return_number(5, 4, 1) == 5
assert return_number(5, 4, 0) == 4
