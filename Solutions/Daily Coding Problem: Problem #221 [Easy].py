# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Zillow.
#
# Let's define a "sevenish" number to be one which is either a power of 7, or the
# sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and
# so on. Create an algorithm to find the nth sevenish number.
#
#
# --------------------------------------------------------------------------------
#
#
def find_nth_seventish_number(n):
    bit_representation_of_n = bin(n)
    sum = 0
    for i, item in enumerate(bit_representation_of_n[:1:-1]):
        if int(item):
            sum += 7 ** i
    return sum


assert find_nth_seventish_number(1) == 1
assert find_nth_seventish_number(2) == 7
assert find_nth_seventish_number(3) == 8
assert find_nth_seventish_number(4) == 49
assert find_nth_seventish_number(5) == 50
assert find_nth_seventish_number(6) == 56
