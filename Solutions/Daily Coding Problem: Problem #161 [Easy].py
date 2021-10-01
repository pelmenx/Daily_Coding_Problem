# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a 32-bit integer, return the number with its bits reversed.
#
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_bits(integer):
    binary = list(integer)
    for i, item in enumerate(binary):
        if item == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'
    binary = "".join(binary)
    return binary


assert reverse_bits('11110000111100001111000011110000') == "00001111000011110000111100001111"
