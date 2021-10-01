# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an unsorted array of integers, find the length of the longest consecutive
# elements sequence.
#
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
# sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#
#
# --------------------------------------------------------------------------------
#
#
def longest_consecutive_element_sequence(array):
    consecutive_elements_dict = {}
    consecutive_elements_list = []
    max_length = 0
    for item in array:
        if (item + 1 in consecutive_elements_dict) and (item - 1 in consecutive_elements_dict):
            if len(consecutive_elements_list[consecutive_elements_dict[item + 1]]) >= len(consecutive_elements_list[consecutive_elements_dict[item - 1]]):
                consecutive_elements_list[consecutive_elements_dict[item + 1]].append(item)
                consecutive_elements_list[consecutive_elements_dict[item + 1]].extend(consecutive_elements_list[consecutive_elements_dict[item - 1]])
                position = consecutive_elements_dict[item - 1]
                for key in consecutive_elements_list[consecutive_elements_dict[item - 1]]:
                    consecutive_elements_dict[key] = consecutive_elements_dict[item + 1]
                consecutive_elements_list[position].clear()
                consecutive_elements_dict[item] = consecutive_elements_dict[item + 1]
                if len(consecutive_elements_list[consecutive_elements_dict[item + 1]]) > max_length:
                    max_length = len(consecutive_elements_list[consecutive_elements_dict[item + 1]])
            else:
                consecutive_elements_list[consecutive_elements_dict[item - 1]].append(item)
                consecutive_elements_list[consecutive_elements_dict[item - 1]].extend(consecutive_elements_list[consecutive_elements_dict[item + 1]])
                position = consecutive_elements_dict[item + 1]
                for key in consecutive_elements_list[consecutive_elements_dict[item + 1]]:
                    consecutive_elements_dict[key] = consecutive_elements_dict[item - 1]
                consecutive_elements_list[position].clear()
                consecutive_elements_dict[item] = consecutive_elements_dict[item - 1]
                if len(consecutive_elements_list[consecutive_elements_dict[item - 1]]) > max_length:
                    max_length = len(consecutive_elements_list[consecutive_elements_dict[item - 1]])
        elif item + 1 in consecutive_elements_dict:
            consecutive_elements_list[consecutive_elements_dict[item + 1]].append(item)
            consecutive_elements_dict[item] = consecutive_elements_dict[item + 1]
            if len(consecutive_elements_list[consecutive_elements_dict[item + 1]]) > max_length:
                max_length = len(consecutive_elements_list[consecutive_elements_dict[item + 1]])
        elif item - 1 in consecutive_elements_dict:
            consecutive_elements_list[consecutive_elements_dict[item - 1]].append(item)
            consecutive_elements_dict[item] = consecutive_elements_dict[item - 1]
            if len(consecutive_elements_list[consecutive_elements_dict[item - 1]]) > max_length:
                max_length = len(consecutive_elements_list[consecutive_elements_dict[item - 1]])
        else:
            consecutive_elements_dict[item] = len(consecutive_elements_dict)
            consecutive_elements_list.append([item])
    return max_length


assert longest_consecutive_element_sequence([100, 4, 200, 1, 3, 2]) == 4
