# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Implement the singleton pattern with a twist. First, instead of storing one
# instance, store two instances. And in every even call of getInstance(), return
# the first instance and in every odd call of getInstance(), return the second
# instance.
#
#
# --------------------------------------------------------------------------------
#
#
class singleton(object):
    def __init__(self, arg1, arg2):
        super(singleton, self).__init__()
        self.arg = arg1, arg2
        self.status = 0

    def getInstance(self):
        if self.status == 0:
            self.status += 1
            return self.arg[0]
        else:
            self.status -= 1
            return self.arg[1]


a = singleton(1, 0)
assert singleton.getInstance(a) == 1
assert singleton.getInstance(a) == 0
assert singleton.getInstance(a) == 1
assert singleton.getInstance(a) == 0
