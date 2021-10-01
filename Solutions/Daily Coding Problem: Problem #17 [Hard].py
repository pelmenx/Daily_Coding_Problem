# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Suppose we reppathent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" reppathents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.
#
# The string
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# reppathents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
#
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.extand an empty second-levels sub-directory subsubdir1.
# subdir2 contains a second-levels sub-directorysubsubdir2 containing a file
# file2.ext.
#
# We are intepathted in finding the longest (number of characters) absolute path to
# a file within our file system. For example, in the second example above, the
# longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
# 32 (not including the double quotes).
#
# Given a string reppathenting the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system. If
# there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.
#
#
# --------------------------------------------------------------------------------
#
#
import re


def check_suitability(string):
    roads = []
    try:
        string.index(".")
    except ValueError:
        return 0
    else:
        find_all_pathes(string, roads)
        return roads


def find_all_pathes(string, roads):
    list, levels, path = make_lists(string)
    count = 0
    check_level = []
    road = []
    for level in levels:
        if len(path) == 2:
            road.append(path[0])
            road.append(path[1])
            road = '/'.join(map(str, road))
            roads.append(road)
            return roads

        if level not in check_level:
            check_level.append(level)
            count += 1

        else:
            for i in range(0, count + 1):
                road.append(path[i])
            road = '/'.join(map(str, road))
            roads.append(road)
            string = re.sub("\n" + '\t' * count + path[count], '', string)
            break
    find_all_pathes(string, roads)


def make_lists(string):
    levels = re.findall("\s+", string)
    path = re.split("\s+", string)
    list = []
    for i in range(0, len(path)):
        if i > 0:
            list.append([levels[i - 1], path[i]])
    return list, levels, path


def check_lenght_of_roads(roads):

    max_lenght = 0
    try:
        for road in roads:
            if "." in road:
                if len(road) > max_lenght:
                    max_lenght = len(road)
                    max_road = road
    except TypeError:
        return 0
    else:
        roads = []
        return (max_lenght, max_road)


string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\tfile11.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tasd\n\tqwe"
string1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\tfile11.ext\n\tsubdir2\n\t\tsubsubdir2\n\tasd\n\tqwe"
string2 = "dir\n\tsubdir1\n\t\tfile1"
print(check_lenght_of_roads(check_suitability(string)))
print(check_lenght_of_roads(check_suitability(string1)))
print(check_lenght_of_roads(check_suitability(string2)))
