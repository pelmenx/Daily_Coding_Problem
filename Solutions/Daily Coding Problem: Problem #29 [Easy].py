# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Run-length encoding is a fast and simple method of encoding strings. The basic
# idea is to represent repeated successive characters as a single count and
# character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.
#
#
# --------------------------------------------------------------------------------
#
#
def encoding(string):
    tmp_list = []
    list = []
    for letter in string:
        if not(not tmp_list):
            if letter != tmp_list[-1]:
                list.append((len(tmp_list), tmp_list[-1]))
                tmp_list = []
        tmp_list.append(letter)
    list.append((len(tmp_list), tmp_list[-1]))
    encripted_text = ""
    for groups in list:
        for item in groups:
            encripted_text += str(item)
    return encripted_text


def decoding(string):
    tmp_list = []
    list = []
    for letter in string:
        if letter.isalpha():
            list.append(letter * int(''.join(map(str, tmp_list))))
            tmp_list = []
        else:
            tmp_list.append(letter)
    list = ''.join(map(str, list))
    return list


plain_text = "AAAABBBCCDAA"
encripted_text = encoding(plain_text)
decrypted_text = decoding(encripted_text)
if plain_text == decrypted_text:
    print(True)
else:
    print(False)
