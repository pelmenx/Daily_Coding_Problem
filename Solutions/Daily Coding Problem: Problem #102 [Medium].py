# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Lyft.
#
# Given a list of integers and a number K, return which contiguous elements of the
# list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
# [2, 3, 4], since 2 + 3 + 4 = 9.
#
#
# --------------------------------------------------------------------------------
#
#
def secuence_contiguous_element(array, k):
    if not array:
        return None
    for i in range(1, len(array) + 1):
        if sum(array[:i]) == k:
            return array[:i]
    return secuence_contiguous_element(array[1:], k)


assert secuence_contiguous_element([1, 2, 3, 4, 5], 9) == [2, 3, 4]
