# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an array of a million integers between zero and a billion, out of order,
# how can you efficiently sort it? Assume that you cannot store an array of a
# billion elements in memory.
#
#
# --------------------------------------------------------------------------------
#
#
def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return heapify(arr, n, largest)


def heapSort(arr: list[int]) -> None:
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


array = [12, 11, 13, 5, 6, 7]
heapSort(array)
assert array == [5, 6, 7, 11, 12, 13]
