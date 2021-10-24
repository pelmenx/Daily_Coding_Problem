# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Implement a PrefixMapSum class with the following methods:
#
#  * insert(key: str, value: int): Set a given key's value in the map. If the key
#    already exists, overwrite the value.
#  * sum(prefix: str): Return the sum of all values of keys that begin with a
#    given prefix.
#
# For example, you should be able to run the following code:
#
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3
#
# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5
#
#
#
# --------------------------------------------------------------------------------
#
#
class PrefixMapSum(object):
    def __init__(self):
        super(PrefixMapSum, self).__init__()
        self.dict = {}

    def insert(self, key: str, value: int):
        self.dict[key] = value

    def sum(self, prefix: str):
        sum_ = 0
        for key in self.dict:
            if key.startswith(prefix):
                sum_ += self.dict[key]
        return sum_


mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
