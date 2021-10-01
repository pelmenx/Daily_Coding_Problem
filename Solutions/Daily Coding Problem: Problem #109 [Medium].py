# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Cisco.
#
# Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit
# should be swapped, the 3rd and 4th bit should be swapped, and so on.
#
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
#
# Bonus: Can you do this in one line?
#
#
# --------------------------------------------------------------------------------
#
#
def swap(integer):
    b = list(bin(integer))
    for i in range(3, len(b), 2):
        b[i], b[i - 1] = b[i - 1], b[i]
    b = int("".join(b), 2)
    return b


assert swap(5) == 3
