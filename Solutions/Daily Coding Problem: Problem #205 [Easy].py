# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by IBM.
#
# Given an integer, find the next permutation of it in absolute order. For
# example, given 48975, the next permutation would be 49578.
#
#
# --------------------------------------------------------------------------------
#
#
def find_next_permutartion(integer):
    digits_list = []
    for i in range(len(str(integer))):
        digits_list.append(int(str(integer)[i]))
    tmp_list = [digits_list.pop()]
    for i in range(len(digits_list) - 1, -1, -1):
        if digits_list[i] < max(tmp_list):
            tmp_list.append(digits_list.pop())
            digits_list.append(max(tmp_list))
            tmp_list.remove(max(tmp_list))
            break
        else:
            tmp_list.append(digits_list.pop())
    while tmp_list:
        digits_list.append(min(tmp_list))
        tmp_list.remove(min(tmp_list))
    output = ""
    for item in digits_list:
        output += str(item)
    output = int(output)
    return output


assert find_next_permutartion(48975) == 49578
