# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of list[i]s which represents each line, fully
# justified.
#
# More specifically, you should have as many words as possible in each line. There
# should be at least one space between each word. Pad extra spaces when necessary
# so that each line has exactly length k. Spaces should be distributed as equally
# as possible, with the extra spaces, if any, distributed starting from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side
# with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly
#
#
#
# --------------------------------------------------------------------------------
#
#
def algorithm_to_justify_text(list_of_words, k):
    tmp_list = ""
    list = []
    for word in list_of_words:
        if not tmp_list:
            tmp_list += word
        else:
            if len(tmp_list + " " + word) <= k:
                tmp_list += " " + word
            else:
                list.append(tmp_list)
                tmp_list = word
    list.append(tmp_list)
    print(list)
    list = add_spaces(list, k)
    return list


def add_spaces(list, k):
    for i in range(len(list)):
        print(len(list[i]), k - len(list[i]), list[i].count(" "))
        if list[i].count(" ") == 0:
            string = list[i] + " " * (k - len(list[i]))
            list[i] = string

        else:
            spaces_list = []
            string_list = []
            for j in range(0, len(list[i])):
                if list[i][j] == " ":
                    spaces_list.append(j)
                string_list.append(list[i][j])
            counter = k - len(list[i])
            while counter > 0:
                for coordinate in spaces_list:
                    string_list.insert(coordinate, " ")
                    for j in range(0, len(spaces_list)):
                        spaces_list[j] += 1
                    counter -= 1
                    if counter == 0:
                        list[i] = ''.join(map(str, string_list))
                        break

    return list


print(algorithm_to_justify_text(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "qwertyuiop"], 16))
