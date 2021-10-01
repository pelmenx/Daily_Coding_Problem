# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an array and a number k that's smaller than the length of the array,
# rotate the array to the right k elements in-place.
#
#
# --------------------------------------------------------------------------------
#
#
def rotate_array(array, k):
    array[:] = array[len(array) - k:] + array[:len(array) - k]
    print(array)


array = [1, 2, 3, 4, 5]
assert array == [1, 2, 3, 4, 5]
rotate_array(array, 2)
assert array == [4, 5, 1, 2, 3]
rotate_array(array, 4)
assert array == [5, 1, 2, 3, 4]
rotate_array(array, 4)
assert array == [1, 2, 3, 4, 5]
