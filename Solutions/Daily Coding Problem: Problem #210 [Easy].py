# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# A Collatz sequence in mathematics can be defined as follows. Starting with any
# positive integer:
#
#  * if n is even, the next number in the sequence is n / 2
#  * if n is odd, the next number in the sequence is 3n + 1
#
# It is conjectured that every such sequence eventually reaches the number 1. Test
# this conjecture.
#
# Bonus: What input n <= 1000000 gives the longest sequence?
#
#
# --------------------------------------------------------------------------------
#
#
def collatz_sequence(integer):
    count = 0
    while integer != 1:
        if integer % 2 == 0:
            integer = integer // 2
        else:
            integer = 3 * integer + 1
        count += 1
    return count


max_round_number = 0
max_round_integer = None
for i in range(1, 1000001):
    round = collatz_sequence(i)
    if round > max_round_number:
        max_round_number = round
        max_round_integer = i
print(max_round_integer)
