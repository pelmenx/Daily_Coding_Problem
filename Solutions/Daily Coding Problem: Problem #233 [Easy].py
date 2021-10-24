# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement the function fib(n), which returns the nth number in the Fibonacci
# sequence, using only O(1) space.
#
#
# --------------------------------------------------------------------------------
#
#
def fib(n: int) -> int:
    if n > 0:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            fib_que: list[int] = [0, 1]
            for _ in range(2, n):
                fib_que = fib_que[-1:] + [sum(fib_que)]
            return fib_que[-1]


assert fib(1) == 0
assert fib(2) == 1
assert fib(3) == 1
assert fib(4) == 2
assert fib(5) == 3
assert fib(6) == 5
assert fib(7) == 8
assert fib(8) == 13
