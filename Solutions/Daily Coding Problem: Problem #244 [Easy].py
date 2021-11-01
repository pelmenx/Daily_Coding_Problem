# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Square.
#
# The Sieve of Eratosthenes is an algorithm used to generate all prime numbers
# smaller than N. The method is to take increasingly larger prime numbers, and
# mark their multiples as composite.
#
# For example, to find all primes less than 100, we would first mark [4, 6, 8,
# ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on.
# Once we have done this for all primes less than N, the unmarked numbers that
# remain will be prime.
#
# Implement this algorithm.
#
# Bonus: Create a generator that produces primes indefinitely (that is, without
# taking N as an input).
#
#
# --------------------------------------------------------------------------------
#
#
def Sieve_of_Eratosthenes(N):
    numbers_set = set([i for i in range(2, N)])
    for i in range(2, N // 2 + 1):
        j = 2
        while j * i < N:
            numbers_set.discard(j * i)
            j += 1
    return numbers_set


def next_prime_number(prime_numbers):
    yield prime_numbers[-1]
    possible_number = prime_numbers[-1] + 1
    while True:
        for prime in prime_numbers:
            if possible_number % prime == 0:
                break
        else:
            prime_numbers.append(possible_number)
            yield possible_number
        possible_number += 1


def produce_prime_numbers():
    prime_numbers = [2]
    yield from next_prime_number(prime_numbers)


primes = Sieve_of_Eratosthenes(100)
next_prime = produce_prime_numbers()
for prime in primes:
    assert prime == next(next_prime)
