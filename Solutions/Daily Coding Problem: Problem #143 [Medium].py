# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
#  * The first part contains all elements in lst that are less than x
#  * The second part contains all elements in lst that are equal to x
#  * The third part contains all elements in lst that are larger than x
#
# Ordering within a part can be arbitrary.
#
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may
# be [9, 3, 5, 10, 10, 12, 14].
#
#
# --------------------------------------------------------------------------------
#
#
def tree_parts(array, x):
    part_1 = []
    part_2 = []
    part_3 = []
    for item in array:
        if item < x:
            part_1.append(item)
        elif item == x:
            part_2.append(item)
        else:
            part_3.append(item)
    return part_1 + part_2 + part_3


assert tree_parts([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]
