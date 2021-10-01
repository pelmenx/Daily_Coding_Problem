# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.
#
#
# --------------------------------------------------------------------------------
#
#
import time


def scheduler(function, delay):
    time.sleep(delay)
    function()


def job():
    print("do some job")


scheduler(job, 3)
