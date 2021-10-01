# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an integer n, return the length of the longest consecutive run of 1s in
# its binary representation.
#
# For example, given 156, you should return 3.
#
#
# --------------------------------------------------------------------------------
#
#
def longest_run_of_1s(integer):
    max_counter = 0
    current_counter = 0
    for item in bin(integer)[2:]:
        if item == "1":
            current_counter += 1
            if current_counter > max_counter:
                max_counter = current_counter
        else:
            current_counter = 0
    return max_counter


assert longest_run_of_1s(156) == 3
