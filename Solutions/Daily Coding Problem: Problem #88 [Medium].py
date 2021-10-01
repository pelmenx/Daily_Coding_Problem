# Good morning! Here's your coding interview problem for today.
#
# This question was asked by ContextLogic.
#
# Implement division of two positive integers without using the division,
# multiplication, or modulus operators. Return the quotient as an integer,
# ignoring the remainder.
#
#
# --------------------------------------------------------------------------------
#
#
def division(a, b):
    if a == b:
        return 1
    dev = 0
    c = b
    while a >= c:
        c += b
        dev += 1
    return dev


assert division(11, 2) == 5
assert division(4, 2) == 2
assert division(2, 2) == 1
assert division(2, 11) == 0
