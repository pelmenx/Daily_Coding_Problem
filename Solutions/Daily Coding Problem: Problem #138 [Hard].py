# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a
# 1¢.
#
#
# --------------------------------------------------------------------------------
#
#
def find_min_number_of_coins(value):
    coins_values = [1, 5, 10, 25]
    amount = 0
    counter = 0
    while amount != value:
        if value - amount >= coins_values[-1]:
            amount += coins_values[-1]
            counter += 1
        else:
            coins_values.pop()
    return counter


assert find_min_number_of_coins(16) == 3
assert find_min_number_of_coins(90) == 5
assert find_min_number_of_coins(100) == 4
