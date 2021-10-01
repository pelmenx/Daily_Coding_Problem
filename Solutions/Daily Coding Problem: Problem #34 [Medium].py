# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Quora.
#
# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than one
# palindrome of minimum length that can be made, return the lexicographically
# earliest one (the first one alphabetically).
#
# For example, given the string "race", you should return "ecarace", since we can
# add three letters to it (which is the smallest amount to make a palindrome).
# There are seven other palindromes that can be made from "race" by adding three
# letters, but "ecarace" comes first alphabetically.
#
# As another example, given the string "google", you should return "elgoogle".
#
#
# --------------------------------------------------------------------------------
#
#
def make_palindrome(string):
    if len(string) == 0:
        return False
    list = find_partician(string)
    palindromes = []
    for substring in list:
        if string.startswith(substring) is True:
            adding = string[len(substring):]
            palindromes.append(adding[::-1] + substring + adding)
        else:
            adding = string[:len(string) - len(substring)]
            palindromes.append(adding + substring + adding[::-1])
    alphabetically_min_palindrome = palindromes[0]
    for i in range(1, len(palindromes)):
        if palindromes[i] < alphabetically_min_palindrome:
            alphabetically_min_palindrome = palindromes[i]
    return alphabetically_min_palindrome


def find_partician(string):
    list = []
    for i in range(1, len(string) + 1):
        list.append(string[:i])
        list.append(string[i:])
    max_length = 0
    for i in range(len(list) - 1, -1, -1):
        if len(list[i]) != 1 and len(list[i]) != 0:
            if len(list[i]) % 2 == 0:
                s1 = list[i][:int(len(list[i]) / 2)]
                s2 = list[i][int(len(list[i]) / 2):]
                s2 = s2[::-1]
                if s1 != s2:
                    list.pop(i)
                else:
                    if len(list[i]) > max_length:
                        max_length = len(list[i])
            else:
                s1 = list[i][:int(len(list[i]) / 2)]
                s2 = list[i][int(len(list[i]) / 2) + 1:]
                s2 = s2[::-1]
                if s1 != s2:
                    list.pop(i)
                else:
                    if len(list[i]) > max_length:
                        max_length = len(list[i])
        elif len(list[i]) == 0:
            list.pop(i)
    for i in range(len(list) - 1, -1, -1):
        if len(list[i]) < max_length:
            list.pop(i)
    return list


print(make_palindrome("google"))
print(make_palindrome("googleel"))
print(make_palindrome("g"))
print(make_palindrome("ww"))
print(make_palindrome("abc"))
print(make_palindrome(""))
