# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Compute the running median of a sequence of numbers. That is, given a stream of
# numbers, print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle
# numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
# print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
#
#
#
# --------------------------------------------------------------------------------
#
#
def find_median(sequence):
    for i in range(0, len(sequence)):
        tmp = sequence[:i + 1]
        tmp.sort()
        if i == 0:
            print(tmp[0])
        elif (i + 1) % 2 == 0:
            if ((tmp[int(len(tmp) / 2)] + tmp[int(len(tmp) / 2) - 1]) / 2) == int((tmp[int(len(tmp) / 2)] + tmp[int(len(tmp) / 2) - 1]) / 2):
                print(int((tmp[int(len(tmp) / 2)] + tmp[int(len(tmp) / 2) - 1]) / 2))
            else:
                print((tmp[int(len(tmp) / 2)] + tmp[int(len(tmp) / 2) - 1]) / 2)
        elif (i + 1) % 2 == 1:
            print(tmp[int(len(tmp) / 2)])


find_median([2, 1, 5, 7, 2, 0, 5])
