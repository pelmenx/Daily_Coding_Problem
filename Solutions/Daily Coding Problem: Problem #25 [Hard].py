# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Implement regular expression matching with the following special characters:
#
#  * . (period) which matches any single character
#  * * (asterisk) which matches zero or more of the preceding element
#
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string "raymond"
# should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should
# return true. The same regular expression on the string "chats" should return
# false.
#
#
# --------------------------------------------------------------------------------
#
#
import sys


def check_list():
    global list
    if True in list:
        list = []
        return True
    else:
        list = []
        return False


def regexp_validator(regexp, string):
    global list
    try:
        if regexp[0] != "*":
            if len(regexp) == 1:
                if len(string) == 1:
                    list.append(True)
            else:
                if regexp[0] == string[0] or regexp[0] == ".":
                    return regexp_validator(regexp[1:], string[1:])

        else:
            counter = 0
            count = 0
            for symbols in regexp:
                if symbols == "." or symbols == "*":
                    counter += 1
                    if symbols == ".":
                        count += 1
            if counter == len(regexp) and count <= len(string):
                list.append(True)
            else:
                min_i = sys.maxsize
                for i in range(0, len(regexp)):
                    if regexp[i] != "." and regexp[i] != "*" and i < min_i:
                        min_i = i

                for j in range(0, len(string)):
                    if regexp[min_i] == string[j]:
                        regexp_validator(regexp[min_i:], string[j:])
    except IndexError:
        pass


list = []
regexp_validator("ra.", "ray")
print(check_list())
regexp_validator("ra.", "raymond")
print(check_list())
regexp_validator(".*at", "chatat")
print(check_list())
regexp_validator(".*at", "chats")
print(check_list())
regexp_validator(".*", "chhat")
print(check_list())
regexp_validator("*******t", "chhat")
print(check_list())
regexp_validator(".*..a**.", "chhat")
print(check_list())
