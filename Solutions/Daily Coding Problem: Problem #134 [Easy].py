# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# You have a large array with most of the elements as zero.
#
# Use a more space-efficient data structure, SparseArray, that implements the same
# interface:
#
#  * init(arr, size): initialize with the original large array and size.
#  * set(i, val): updates index at i with val.
#  * get(i): gets the value at index i.
#
#
# --------------------------------------------------------------------------------
#
#
class SparseArray(object):
    def __init__(self):
        super(SparseArray, self).__init__()
        self.storage = {}

    def init(self, arr, size):
        for i, item in enumerate(arr):
            if item:
                self.storage[i] = item

    def set(self, i, val):
        if 0 <= i < len(self.storage):
            if i in self.storage:
                if val == 0:
                    self.storage.pop(i)
                else:
                    self.storage[i] = val
            else:
                self.storage[i] = val
        else:
            print("index out of range")

    def get(self, i):
        if 0 <= i < len(self.storage):
            if i in self.storage:
                return self.storage[i]
            else:
                return 0
        else:
            print("index out of range")


array = [1, 2, 0, 0, 3, 0, 0, 4, 0, 0]
s_array = SparseArray()
s_array.init(array, len(array))

assert s_array.storage == {0: 1, 1: 2, 4: 3, 7: 4}

s_array.set(0, 9)

assert s_array.storage == {0: 9, 1: 2, 4: 3, 7: 4}

assert s_array.get(0) == 9
assert s_array.get(2) == 0
