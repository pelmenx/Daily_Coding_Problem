# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Goldman Sachs.
#
# You are given N identical eggs and access to a building with k floors. Your task
# is to find the lowest floor that will cause an egg to break, if dropped from
# that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks
# when dropped from the xth floor, you can assume it will also break when dropped
# from any floor greater than x.
#
# Write an algorithm that finds the minimum number of trial drops it will take, in
# the worst case, to identify this floor.
#
# For example, if N = 1 and k = 5, we will need to try dropping the egg at every
# floor, beginning with the first, until we reach the fifth floor, so our solution
# will be 5.
#
#
# --------------------------------------------------------------------------------
#
#
def find_lower_floor(N, k):
    if N == 1:
        return k

    counter = N - 2
    while N > 2:
        N -= 1
        tmp_k = k / 2
        k = int(k / 2)
        if tmp_k != k:
            k += 1

    i = 1
    count = 1
    while i < k:
        count += 1
        i += count
    return count + counter


assert find_lower_floor(1, 100) == 100
assert find_lower_floor(2, 100) == 14
assert find_lower_floor(3, 100) == 11
assert find_lower_floor(4, 100) == 9
