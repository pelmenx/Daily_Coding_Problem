# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# You are given an array of length 24, where each element represents the number of
# new subscribers during the corresponding hour. Implement a data structure that
# efficiently supports the following:
#
#  * update(hour: int, value: int): Increment the element at index hour by value.
#  * query(start: int, end: int): Retrieve the number of subscribers that have
#    signed up between start and end (inclusive).
#
# You can assume that all values get cleared at the end of the day, and that you
# will not be asked for start and end values that wrap around midnight.
#
#
# --------------------------------------------------------------------------------
#
#
class Subscribers:
    def __init__(self):
        self.subscribers_list = [0 for _ in range(24)]

    def update(self, hour: int, value: int):
        self.subscribers_list[hour] += value

    def query(self, start: int, end: int) -> int:
        return sum(self.subscribers_list[start:end + 1])


subs = Subscribers()
subs.update(2, 50)
subs.update(5, 110)
assert subs.query(1, 24) == 160
