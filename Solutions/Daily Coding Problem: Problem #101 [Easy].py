# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Alibaba.
#
# Given an even number (greater than 2), return two prime numbers whose sum will
# be equal to the given number.
#
# A solution will always exist. See Goldbach’s conjecture
# [https://en.wikipedia.org/wiki/Goldbach%27s_conjecture].
#
# Example:
#
# Input: 4
# Output: 2 + 2 = 4
#
#
# If there are more than one solution possible, return the lexicographically
# smaller solution.
#
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <=
# d, then
#
# [a, b] < [c, d]
#
#
# If a < c OR a==c AND b < d.
#
#
# --------------------------------------------------------------------------------
#
#
def find_two_prime_numbers(number):
    def is_prime(num):
        for i_ in range(2, num // 2):
            if num % i_ == 0:
                return False
        return True
    if number < 3 or number % 2 == 1:
        return None
    for i in range(2, number - 1):
        if_i_is_prime_number = is_prime(i)
        if if_i_is_prime_number:
            j = number - i
            if_j_is_prime_number = is_prime(j)
            if if_j_is_prime_number:
                return(i, j)


assert find_two_prime_numbers(4) == (2, 2)
assert find_two_prime_numbers(100) == (3, 97)
