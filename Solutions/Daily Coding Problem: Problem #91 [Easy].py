# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# What does the below code snippet print out? How can we fix the anonymous
# functions to behave as we'd expect?
#
# functions = []
# for i in range(10):
#     functions.append(lambda : i)
#
# for f in functions:
#     print(f())
#
#
#
# --------------------------------------------------------------------------------
#
#
'''
function returns 9s because last value of i is 9
we have to add new itteration to fix the function
'''
functions = []
for i in range(10):
    functions.append(lambda: i)


i = 0
for f in functions:
    print(f())
    i += 1
