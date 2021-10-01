# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in,
# first-out) data structure with the following methods: enqueue, which inserts an
# element into the queue, and dequeue, which removes it.
#
#
# --------------------------------------------------------------------------------
#
#
class queue(object):

    def __init__(self):
        super(queue, self).__init__()
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, arg):
        self.stack1.append(arg)

    def dequeue(self):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
            while self.stack2:
                self.stack1.append(self.stack2.pop())


q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.stack1)
