# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by PayPal.
#
# Given a string and a number of lines k, print the string in zigzag form. In
# zigzag, characters are printed out diagonally from top left to bottom right
# until reaching the kth line, then back up to top right, and so on.
#
# For example, given the sentence "thisisazigzag" and k = 4, you should print:
#
# t     a     g
#  h   s z   a
#   i i   i z
#    s     g
#
#
#
# --------------------------------------------------------------------------------
#
#
def zig_zag_print(word: str, k: int) -> None:
    assert k > 1, "k should be > 1"
    word_list = [[] for _ in range(k)]
    len_block = k * 2 - 2
    number_of_blocks = len(word)//len_block
    for i in range(number_of_blocks+1):
        start_block = i * len_block
        end_block = (i + 1) * len_block
        indent = 1
        for j in range(k):
            if j == 0:
                if start_block + j < len(word):
                    string = word[start_block: end_block][j]
                    string = string + " " * (len_block - 1)
                    word_list[j].append(string)
                else:
                    break
            elif j == k - 1:
                if start_block + j < len(word):
                    string = word[start_block: end_block][j]
                    string = " " * (len_block // 2) + string
                    string = string + " " * (len_block // 2 - 1)
                    word_list[j].append(string)
            else:
                if start_block + j < len(word):
                    string1 = word[start_block: end_block][j]
                    string1 = " " * indent + string1
                    string1 = string1.ljust(len_block // 2, " ")
                    word_list[j].append(string1 + ' ')
                else:
                    break
                if start_block + (len_block - j) < len(word):
                    string2 = word[start_block: end_block][len_block - j]
                    string2 = string2 + " " * (indent - 1)
                    string2 = string2.rjust(len_block // 2 - 1, " ")
                    word_list[j].append(string2)
                indent += 1

    for line in word_list:
        output = "".join(line)
        output = output.rstrip()
        print(output)
    print()


zig_zag_print("thisisazigzag", 4)


zig_zag_print("thisisazigzag", 5)
