# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a number in Roman numeral [https://en.wikipedia.org/wiki/Roman_numerals]
# format, convert it to decimal.
#
# The values of Roman numerals are as follows:
#
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
#
#
# In addition, note that the Roman numeral system uses subtractive notation
# [https://en.wikipedia.org/wiki/Subtractive_notation] for numbers such as IV and
# XL.
#
# For the input XIV, for instance, you should return 14.
#
#
# --------------------------------------------------------------------------------
#
#
def convert_roman_to_decimal(roman):
    value_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def check_next(position):
        result = value_dict[roman[position]]
        for i in range(position + 1, len(roman)):
            if value_dict[roman[position]] < value_dict[roman[i]]:
                result = value_dict[roman[i]]
                tmp_text = roman[position: i]
                for item in tmp_text[::-1]:
                    result = result - value_dict[item]
                return result, i - position + 1
        return result, 1

    i = 0
    sum = 0
    while i < len(roman):
        tmp_sum, shift = check_next(i)
        sum += tmp_sum
        i += shift
    return sum


assert convert_roman_to_decimal("XIV") == 14
assert convert_roman_to_decimal("DCCCLXXXVIII") == 888
assert convert_roman_to_decimal("XCVII") == 97
