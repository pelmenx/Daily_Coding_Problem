# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Quora.
#
# Given an absolute pathname that may have . or .. as part of it, return the
# shortest standardized path.
#
# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
#
#
# --------------------------------------------------------------------------------
#
#
def standardized_path(path):
    splited_path = path.split('/')[1:-1]
    stack = []
    for directory in splited_path:
        if directory == ".":
            pass
        elif directory == "..":
            stack.pop()
        else:
            stack.append(directory)
    return "/" + "/".join(stack) + "/"


assert standardized_path("/usr/bin/../bin/./scripts/../") == "/usr/bin/"
