# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the
# list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
#
#
# --------------------------------------------------------------------------------
#
#


def find_numbers(array, goal):
    past_number = []
    for items in array:
        for number in past_number:
            if items == number:
                return(goal - items, items)
        past_number.append(goal - items)

    return False


# tests
print(find_numbers([10, 15, 3, 7], 17))
print(find_numbers([10, 15, 3], 17))
print(find_numbers([10, 0, -10], 0))
