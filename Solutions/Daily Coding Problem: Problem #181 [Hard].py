# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string, split it into as few strings as possible such that each string
# is a palindrome.
#
# For example, given the input string racecarannakayak, return ["racecar", "anna",
# "kayak"].
#
# Given the input string abc, return ["a", "b", "c"].
#
#
# --------------------------------------------------------------------------------
#
#
def split_into_polindromes(string):
    def spliting(string_, array=[]):
        if not string_:
            for item in array:
                if len(item) % 2 == 1:
                    if item[:len(item) // 2] != item[:len(item) // 2:-1]:
                        return
                else:
                    if item[:len(item) // 2] != item[:len(item) // 2 - 1:-1]:
                        return
            yield array
        if string_:
            yield from spliting(string_[1:], array + [string_[:1]])
        if array:
            if string_:
                yield from spliting(string_[1:], array[:-1] + [array[-1] + string_[:1]])
    result = None
    lenght = len(string) + 1
    for splited in spliting(string):
        if len(splited) < lenght:
            lenght = len(splited)
            result = splited
    return result


assert split_into_polindromes('racecarannakayak') == ['racecar', 'anna', 'kayak']
assert split_into_polindromes('abc') == ['a', 'b', 'c']
