# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Spreadsheets often use this alphabetical encoding for its columns: "A", "B",
# "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
#
# Given a column number, return its alphabetical column id. For example, given 1,
# return "A". Given 27, return "AA".
#
#
# --------------------------------------------------------------------------------
#
#
def return_alphabetical_column_id(number):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    column_id = ""
    while number > 26:
        number = number // 26
        column_id += alphabet[number - 1]
    column_id += str(alphabet[number % 26 - 1])
    print(column_id)


return_alphabetical_column_id(27)
