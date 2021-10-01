# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a stack of N elements, interleave the first half of the stack with the
# second half reversed using only one other queue. This should be done in-place.
#
# Recall that you can only push or pop from a stack, and enqueue or dequeue from a
# queue.
#
# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
#
# Hint: Try working backwards from the end state.
#
#
# --------------------------------------------------------------------------------
#
#
class stack(object):
    def __init__(self):
        super(stack, self).__init__()
        self.st = []

    def pop(self):
        return self.st.pop()

    def push(self, arg):
        self.st.append(arg)


class queue(object):
    def __init__(self):
        super(queue, self).__init__()
        self.que = []

    def dequeue(self):
        return self.que.pop(0)

    def enqueue(self, arg):
        self.que.append(arg)


def rearrange_stack(stack_):
    num_of_elements = (len(stack_.st))
    que = queue()
    for i in range(num_of_elements - 1):
        for j in range(num_of_elements - 1 - i):
            que.enqueue(stack_.pop())
        for j in range(num_of_elements - 1 - i):
            stack_.push(que.dequeue())


st1 = stack()
st1.st = [1, 2, 3, 4, 5]

rearrange_stack(st1)
assert st1.st == [1, 5, 2, 4, 3]

st2 = stack()
st2.st = [1, 2, 3, 4]

rearrange_stack(st2)
assert st2.st == [1, 4, 2, 3]
