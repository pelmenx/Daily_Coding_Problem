# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a string, find the longest palindromic contiguous substring. If there are
# more than one with the maximum length, return any one.
#
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
# longest palindromic substring of "bananas" is "anana".
#
#
# --------------------------------------------------------------------------------
#
#
def find_the_longest_palindrom(string):
    if not string:
        return
    lengest_polindrom = ""
    polindrom = is_palindrom(string)
    if polindrom:
        return string
    polindroms = (find_the_longest_palindrom(string[:-1]), find_the_longest_palindrom(string[1:]))
    for item in polindroms:
        if item is not None:
            if len(item) > len(lengest_polindrom):
                lengest_polindrom = item
    return lengest_polindrom


def is_palindrom(string):
    half = int(len(string) / 2)
    if len(string) % 2 == 1:
        if string[:half] == string[:half:-1]:
            return string
    else:
        if string[:half] == string[:half - 1:-1]:
            return string


print(find_the_longest_palindrom("aabcdcb"))
print(find_the_longest_palindrom("bananas"))
print(find_the_longest_palindrom("a"))
print(find_the_longest_palindrom(""))
