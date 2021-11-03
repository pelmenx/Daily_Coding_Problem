# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Implement a 2D iterator class. It will be initialized with an array of arrays,
# and should implement the following methods:
#
#  * next(): returns the next element in the array of arrays. If there are no more
#    elements, raise an exception.
#  * has_next(): returns whether or not the iterator still has elements left.
#
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
# repeatedly should output 1, 2, 3, 4, 5, 6.
#
# Do not use flatten or otherwise clone the arrays. Some of the arrays can be
# empty.
#
#
# --------------------------------------------------------------------------------
#
#
class iterator(object):
    def __init__(self, arg):
        super(iterator, self).__init__()
        self.array = arg
        self.position = [0, -1]

    def next(self):
        if self.position[1] < len(self.array[self.position[0]]) - 1:
            self.position[1] += 1
            return self.array[self.position[0]][self.position[1]]
        else:
            self.position[0] += 1
            self.position[1] = -1
            return self.next()

    def has_next(self,):
        for i in range(self.position[0], len(self.array)):
            if i == self.position[0]:
                for _ in range(self.position[1] + 1, len(self.array[i])):
                    return True
            else:
                for _ in range(0, len(self.array[i])):
                    return True
        return False


it = iterator([[1, 2], [3], [], [4, 5, 6], [], []])
assert it.has_next() is True
assert it.next() == 1
assert it.has_next() is True
assert it.next() == 2
assert it.has_next() is True
assert it.next() == 3
assert it.has_next() is True
assert it.next() == 4
assert it.has_next() is True
assert it.next() == 5
assert it.has_next() is True
assert it.next() == 6
assert it.has_next() is False
try:
    it.next()
except IndexError:
    print("IndexError")
