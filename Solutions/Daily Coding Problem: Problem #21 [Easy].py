# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given an array of time intervals (start, end) for classroom lectures (possibly
# overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
#
#
# --------------------------------------------------------------------------------
#
#
import sys


def find_min_number_of_room(time_intervals):
    min = sys.maxsize
    max = -sys.maxsize
    for meeting in time_intervals:
        for time in meeting:
            if time < min:
                min = time
            if time > max:
                max = time
    counter = 0
    for i in range(min, max):
        tmp_counter = 0
        for meeting in time_intervals:
            if meeting[0] <= i < meeting[1]:
                tmp_counter += 1
                if tmp_counter > counter:
                    counter = tmp_counter
    return counter


time_intervals0 = [(30, 75), (0, 50), (60, 150)]
time_intervals1 = [(30, 75), (0, 50), (10, 60), (60, 150)]
time_intervals2 = [(60, 150), (60, 150), (150, 170)]
time_intervals3 = [(60, 150), (150, 169)]
time_intervals4 = [(60, 150)]
time_intervals5 = []

print(find_min_number_of_room(time_intervals0))

print(find_min_number_of_room(time_intervals1))

print(find_min_number_of_room(time_intervals2))

print(find_min_number_of_room(time_intervals3))

print(find_min_number_of_room(time_intervals4))

print(find_min_number_of_room(time_intervals5))
