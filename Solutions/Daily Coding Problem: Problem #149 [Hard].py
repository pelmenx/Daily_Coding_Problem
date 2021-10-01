# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Goldman Sachs.
#
# Given a list of numbers L, implement a method sum(i, j) which returns the sum
# from the sublist L[i:j] (including i, excluding j).
#
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]),
# which is 5.
#
# You can assume that you can do some pre-processing. sum() should be optimized
# over the pre-processing step.
#
#
# --------------------------------------------------------------------------------
#
#
class Sub_array_sum(object):

    def __init__(self, arg):
        super(Sub_array_sum, self).__init__()
        self.list = arg
        self.total = [0]
        self.pre_processing()

    def pre_processing(self):
        tmp = 0
        for number in self.list:
            tmp += number
            self.total.append(tmp)

    def sum(self, i, j):
        if 0 <= i <= j <= len(self.list):
            return self.total[j] - self.total[i]


sas = Sub_array_sum([1, 2, 3, 4, 5])
assert sas.sum(1, 3) == 5
