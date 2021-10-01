# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of numbers and an index i, return the index of the nearest larger
# number of the number at index i, where distance is measured in array indices.
#
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
#
# If two distances to larger numbers are the equal, then return any one of them.
# If the array at i doesn't have a nearest larger integer, then return null.
#
# Follow-up: If you can preprocess the array, can you do this in constant time?
#
#
# --------------------------------------------------------------------------------
#
#
def larger_number(array, index):
    left = index - 1
    right = index + 1
    while left >= 0 or right < len(array):
        if left >= 0:
            if array[left] > array[index]:
                return left
            left -= 1
        if right < len(array):
            if array[right] > array[index]:
                return right
            right += 1
    return None


def larger_number_constant_time(array, index):
    def preprocess(array_, index_):
        i = 1
        while i < len(array_):
            j = i
            while array_[j - 1] >= array_[j] and j - 1 >= 0:
                array_[j], array_[j - 1] = array_[j - 1], array_[j]
                if j - 1 == index_:
                    index_ = j
                elif j == index_:
                    index_ = j - 1
            i += 1
        return index_, array_

    index, array = preprocess(array, index)
    if index < len(array) - 1:
        return index + 1
    else:
        return None


assert larger_number([4, 1, 3, 5, 6], 0) == 3

assert larger_number_constant_time([4, 1, 3, 5, 6], 0) == 3
