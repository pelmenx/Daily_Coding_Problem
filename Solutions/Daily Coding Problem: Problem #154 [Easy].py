# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Implement a stack API using only a heap. A stack implements the following
# methods:
#
#  * push(item), which adds an element to the stack
#  * pop(), which removes and returns the most recently added element (or throws
#    an error if there is nothing on the stack)
#
# Recall that a heap has the following operations:
#
#  * push(item), which adds a new key to the heap
#  * pop(), which removes and returns the max value of the heap
#
#
# --------------------------------------------------------------------------------
#
#

from heapq import heappush, heappop
from sys import maxsize


class Heap(object):
    def __init__(self):
        super(Heap, self).__init__()
        self.heap = []
        self.counter = maxsize

    def push(self, item):
        heappush(self.heap, (self.counter, item))
        self.counter -= 1

    def pop(self):
        heappop(self.heap)
        self.counter += 1


class Stack(object):
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = Heap()

    def push(self, item):
        self.stack.push(item)

    def pop(self):
        self.stack.pop()
