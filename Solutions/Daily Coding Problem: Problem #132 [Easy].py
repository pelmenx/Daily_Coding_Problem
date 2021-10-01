# Good morning! Here's your coding interview problem for today.
#
# This question was asked by Riot Games.
#
# Design and implement a HitCounter class that keeps track of requests (or hits).
# It should support the following operations:
#
#  * record(timestamp): records a hit that happened at timestamp
#  * total(): returns the total number of hits recorded
#  * range(lower, upper): returns the number of hits that occurred between
#    timestamps lower and upper (inclusive)
#
# Follow-up: What if our system has limited memory?
#
#
# --------------------------------------------------------------------------------
#
#
import datetime
import time


class Hit_counter(object):
    def __init__(self):
        super(Hit_counter, self).__init__()
        self.counter = 0
        self.timestamp_list = []

    def record(self):
        self.counter += 1
        self.timestamp_list.append(datetime.datetime.now().timestamp())

    def total(self):
        return(self.counter)

    def range(self, lower, upper):
        i = 0
        for item in self.timestamp_list:
            if lower <= item <= upper:
                i += 1
        return i


hit = Hit_counter()
hit.record()
time.sleep(1)
hit.record()
time.sleep(2)
hit.record()
assert hit.total() == 3
assert hit.range(datetime.datetime.now().timestamp() - 3, datetime.datetime.now().timestamp()) == 2
