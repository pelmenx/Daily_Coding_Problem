# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Implement a stack that has the following methods:
#
#  * push(val), which pushes an element onto the stack
#  * pop(), which pops off and returns the topmost element of the stack. If there
#    are no elements in the stack, then it should throw an error or return null.
#  * max(), which returns the maximum value in the stack currently. If there are
#    no elements in the stack, then it should throw an error or return null.
#
# Each method should run in constant time.
#
#
# --------------------------------------------------------------------------------
#
#
class Stack:
    def __init__(self):
        self.stack = []
        self.max_value = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_value or value >= self.max_value[-1]:
            self.max_value.append(value)

    def pop(self):
        if not self.stack:
            raise Exception
        if self.stack[-1] == self.max_value[-1]:
            self.max_value.pop()
        self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        else:
            return self.max_value[-1]


s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(3)
s.push(2)
s.pop()
s.pop()
print(s.max())
