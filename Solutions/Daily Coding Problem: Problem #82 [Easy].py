# Good morning! Here's your coding interview problem for today.
#
# This problem was asked Microsoft.
#
# Using a read7() method that returns 7 characters from a file, implement readN(n)
# which reads n characters.
#
# For example, given a file with the content “Hello world”, three read7() returns
# “Hello w”, “orld” and then “”.
#
#
# --------------------------------------------------------------------------------
#
#
class file(object):
    """docstring forfile."""

    def __init__(self, arg):
        super(file, self).__init__()
        self.arg = arg
        self.last_readed_letter = 0

    def read7(self):
        if self.last_readed_letter < len(self.arg):
            result = self.arg[self.last_readed_letter:self.last_readed_letter + 7]
            self.last_readed_letter += 7
            return result
        else:
            return ""

    def read_N(self, N):
        if N > 7:
            dev = N // 7
            mod = N % 7
            tmp = ""
            for i in range(dev):
                tmp += self.read7()
            tmp += self.arg[self.last_readed_letter:self.last_readed_letter + mod]
            self.last_readed_letter += mod
            return tmp
        elif N < 7:
            mod = N % 7
            tmp = self.read7()
            tmp = tmp[:7 - mod + 1]
            self.last_readed_letter -= mod - 1
            return tmp
        else:
            return self.read7()


file1 = file("Hello world")
print(file1.read7())
print(file1.read7())
print(file1.read7())

file1 = file("Hello world")
print(file1.read_N(9))
print(file1.read_N(9))
print(file1.read_N(9))

file1 = file("Hello world")
print(file1.read_N(4))
print(file1.read_N(4))
print(file1.read_N(4))
print(file1.read_N(4))

file1 = file("Hello world")
print(file1.read_N(7))
print(file1.read_N(7))
print(file1.read_N(7))
