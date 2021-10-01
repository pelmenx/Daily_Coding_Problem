# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Implement a bit array.
#
# A bit array is a space efficient array that holds a value of 1 or 0 at each
# index.
#
#  * init(size): initialize the array with size
#  * set(i, val): updates index at i with val where val is either 1 or 0.
#  * get(i): gets the value at index i.
#
#
# --------------------------------------------------------------------------------
#
#
class Bit_array(object):
    def __init__(self):
        super(Bit_array, self).__init__()
        self.list = []

    def init(self, size):
        self.list = [0] * size

    def set(self, i, val):
        if (val == 0 or val == 1):
            if 0 <= i < len(self.list):
                self.list[i] = val

    def get(self, i):
        if 0 <= i < len(self.list):
            return self.list[i]


b_a = Bit_array()
b_a.init(6)
assert b_a.list == [0, 0, 0, 0, 0, 0]

b_a.set(0, 1)
assert b_a.list == [1, 0, 0, 0, 0, 0]

b_a.set(3, 1)
assert b_a.list == [1, 0, 0, 1, 0, 0]

assert b_a.get(3) == 1
