# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Implement 3 stacks using a single list:
#
# class Stack:
#     def __init__(self):
#         self.list = []
#
#     def pop(self, stack_number):
#         pass
#
#     def push(self, item, stack_number):
#         pass
#
#
#
# --------------------------------------------------------------------------------
#
#
class Stack:
    def __init__(self):
        self.list = []
        self.stack_1 = 0
        self.stack_2 = 0
        self.stack_3 = 0

    def pop(self, stack_number):
        if stack_number == 1:
            if self.stack_1 > 0:
                self.list.pop(self.stack_1 - 1)
                self.stack_1 -= 1
                self.stack_2 -= 1
                self.stack_3 -= 1
            else:
                print("stack_1 is empty")
                return
        elif stack_number == 2:
            if self.stack_2 > self.stack_1:
                self.list.pop(self.stack_2 - 1)
                self.stack_2 -= 1
                self.stack_3 -= 1
            else:
                print("stack_2 is empty")
                return
        elif stack_number == 3:
            if self.stack_3 > self.stack_2:
                self.list.pop(self.stack_3 - 1)
                self.stack_3 -= 1
            else:
                print("stack_3 is empty")
                return

    def push(self, item, stack_number):
        if stack_number == 1:
            self.list.insert(self.stack_1, item)
            self.stack_1 += 1
            self.stack_2 += 1
            self.stack_3 += 1
        elif stack_number == 2:
            self.list.insert(self.stack_2, item)
            self.stack_2 += 1
            self.stack_3 += 1
        elif stack_number == 3:
            self.list.insert(self.stack_3, item)
            self.stack_3 += 1
