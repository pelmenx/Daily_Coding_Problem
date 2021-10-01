# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Yelp.
#
# Given a mapping of digits to letters (as in a phone number), and a digit string,
# return all possible letters the number could represent. You can assume each
# valid number in the mapping is a single digit.
#
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should
# return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
#
#
# --------------------------------------------------------------------------------
#
#
def letters_represeted(keyboard, string):
    def represent_2_number(string_1, string_2):
        letters_represeted_list = []
        if len(string_1) == 1:
            for letter_1 in keyboard.get(string_1):
                for letter_2 in keyboard.get(string_2):
                    letters_represeted_list.append(letter_1 + letter_2)
            return letters_represeted_list

    def represent_number_recursion(substring_1, string_2):
        if not string_2:
            return substring_1
        letters_represeted_list = []
        for item in substring_1:
            for letter_2 in keyboard.get(string_2):
                letters_represeted_list.append(item + letter_2)
        return represent_number_recursion(letters_represeted_list, string_2[1:])

    if len(string) == 1:
        return keyboard[string]
    elif len(string) == 2:
        return represent_2_number(string[0], string[1])
    else:
        substring = represent_2_number(string[0], string[1])
        return represent_number_recursion(substring, string[2:])


phone_keyboard = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

assert letters_represeted(phone_keyboard, "23") == ["ad", "ae", "af",
                                                    "bd", "be", "bf",
                                                    "cd", "ce", "cf"]

assert letters_represeted(phone_keyboard, "234") == ['adg', 'adh', 'adi',
                                                     'aeg', 'aeh', 'aei',
                                                     'afg', 'afh', 'afi',
                                                     'bdg', 'bdh', 'bdi',
                                                     'beg', 'beh', 'bei',
                                                     'bfg', 'bfh', 'bfi',
                                                     'cdg', 'cdh', 'cdi',
                                                     'ceg', 'ceh', 'cei',
                                                     'cfg', 'cfh', 'cfi']
