# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Given a list of numbers, create an algorithm that arranges them in order to form
# the largest possible integer. For example, given [10, 7, 76, 415], you should
# return 77641510.
#
#
# --------------------------------------------------------------------------------
#
#
def form_the_largest_number(array):
    def sort_group(array_, value):

        array_ = list(map(str, array_))
        i = 1
        while i < len(array_):
            j = i
            while j > 0:
                if len(array_[j]) == len(array_[j - 1]):
                    if int(array_[j]) < int(array_[j - 1]):
                        array_[j], array_[j - 1] = array_[j - 1], array_[j]
                    else:
                        break
                elif len(array_[j]) < len(array_[j - 1]):
                    pointer = 0
                    for letter1, letter2 in zip(array_[j], array_[j - 1]):
                        if letter1 == letter2:
                            pointer += 1
                        else:
                            break
                    if int(array_[j - 1][pointer:pointer + 1]) < value:
                        array_[j], array_[j - 1] = array_[j - 1], array_[j]
                    else:
                        break
                elif len(array_[j]) > len(array_[j - 1]):
                    pointer = 0
                    for letter1, letter2 in zip(array_[j], array_[j - 1]):
                        if letter1 == letter2:
                            pointer += 1
                        else:
                            break
                    if int(array_[j][pointer:pointer + 1]) < value:
                        array_[j], array_[j - 1] = array_[j - 1], array_[j]
                    else:
                        break
                j -= 1
            i += 1
        array_.reverse()
        return "".join(array_)

    groups_dict = {}
    visited = set()
    for i, item1 in enumerate(array):
        if i in visited:
            continue
        tmp = [item1]
        for j, item2 in enumerate(array[i + 1:]):
            if str(item1)[0] == str(item2)[0]:
                tmp.append(item2)
                visited.add(j + 1 + i)
        if len(tmp) > 1:
            tmp = sort_group(tmp, int(str(item1)[0]))
            groups_dict[str(item1)[0]] = tmp
        else:
            tmp = str(tmp[0])
            groups_dict[str(item1)[0]] = tmp

    keys = list(groups_dict.keys())
    keys.sort()
    keys.reverse()
    output = ""
    for key in keys:
        output += groups_dict[key]
    return int(output)


assert form_the_largest_number([10, 7, 76, 415]) == 77641510
