# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Implement a file syncing algorithm for two computers over a low-bandwidth
# network. What if we know the files in the two computers are mostly the same?
#
#
# --------------------------------------------------------------------------------
#
#
import operator
from itertools import zip_longest


class file_system_1(object):
    def __init__(self, arg):
        super(file_system_1, self).__init__()
        self.arg = arg
        self.inside = None


class file_system_2(object):
    def __init__(self, arg):
        super(file_system_2, self).__init__()
        self.arg = arg
        self.inside = None


computer_1 = file_system_1("computer")
folder1 = file_system_1("folder1")
folder2 = file_system_1("folder2")
folder3 = file_system_1("folder3")
folder4 = file_system_1("folder4")
folder5 = file_system_1("folder5")
file1 = file_system_1("file1")
file2 = file_system_1("file2")
file3 = file_system_1("file3")
file4 = file_system_1("file4")
file5 = file_system_1("file5")
computer_1.inside = sorted([folder3, folder1, folder2, file1], key=operator.attrgetter('arg'))
folder1.inside = sorted([file2, file3], key=operator.attrgetter('arg'))
folder2.inside = sorted([file4], key=operator.attrgetter('arg'))
folder3.inside = sorted([folder4], key=operator.attrgetter('arg'))
folder4.inside = sorted([folder5, file5], key=operator.attrgetter('arg'))

computer_2 = file_system_2("computer")
folder11 = file_system_2("folder1")
folder12 = file_system_2("folder2")
folder13 = file_system_2("folder3")
folder14 = file_system_2("folder4")
folder15 = file_system_2("folder5")
folder16 = file_system_2("folder6")
file11 = file_system_2("file1")
file12 = file_system_2("file2")
file13 = file_system_2("file3")
file14 = file_system_2("file4")
computer_2.inside = sorted([folder13, folder11, folder12, file11, folder16], key=operator.attrgetter('arg'))
folder11.inside = sorted([file12, file13], key=operator.attrgetter('arg'))
folder12.inside = sorted([file14], key=operator.attrgetter('arg'))
folder13.inside = sorted([folder14], key=operator.attrgetter('arg'))
folder14.inside = sorted([folder15], key=operator.attrgetter('arg'))


def get_dict(value):
    if value.inside:
        return {value.arg: [get_dict(inside) for inside in value.inside]}
    else:
        return {value.arg: None}


def syncing(value1, value2):
    if value1.inside and value2.inside:
        for item1, item2 in zip_longest(value1.inside, value2.inside):
            if item1 is None:
                value1.inside.append(item2)
                value1.inside = sorted(value1.inside, key=operator.attrgetter('arg'))
                return syncing(value1, value2)
            elif item2 is None:
                value1.inside.remove(item1)
                del item1
                return syncing(value1, value2)
            elif item1.arg == item2.arg:
                syncing(item1, item2)
            elif item1.arg != item2.arg:
                if item1.arg < item2.arg:
                    value1.inside.remove(item1)
                    del item1
                    return syncing(value1, value2)
                else:
                    value1.inside.append(item2)
                    value1.inside = sorted(value1.inside, key=operator.attrgetter('arg'))
                    return syncing(value1, value2)
    else:
        if value1.inside:
            for item in value1.inside:
                del item
            value1.inside = value2.inside
        else:
            value1.inside = value2.inside


dict1 = get_dict(computer_1)
dict2 = get_dict(computer_2)
print(dict1 == dict2)

syncing(computer_1, computer_2)

dict1 = get_dict(computer_1)
dict2 = get_dict(computer_2)
print(dict1 == dict2)
