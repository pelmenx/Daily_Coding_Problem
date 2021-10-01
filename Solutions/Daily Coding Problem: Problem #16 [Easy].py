# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
#  * record(order_id): adds the order_id to the log
#  * get_last(i): gets the ith last element from the log. i is guaranteed to be
#    smaller than or equal to N.
#
# You should be as efficient with time and space as possible.
#
#
# --------------------------------------------------------------------------------
#
#
def record(order_id):
    global log
    log.append(order_id)


def get_last(i):
    global log
    print(log[-i:])


log = []
for i in range(0, 10):
    record(i)

get_last(5)
