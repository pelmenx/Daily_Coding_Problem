# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given
# "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases: "hello/world:here/",
# "hello//world:here"
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_word(string):
    string = list(string)
    letters = []
    delimiters = []
    for i, letter in enumerate(string):
        if letter.isalnum():
            if letters:
                if string[i - 1].isalnum():
                    letters[-1].append(letter)
                else:
                    letters.append([letter])
            else:
                letters.append([letter])
        else:
            if delimiters:
                if not string[i - 1].isalnum():
                    delimiters[-1].append(letter)
                else:
                    delimiters.append([letter])
            else:
                delimiters.append([letter])
    letters.reverse()
    result = []
    if string[0].isalnum():
        if len(letters) == len(delimiters):
            for word, delimiter in zip(letters, delimiters):
                result.extend(word)
                result.extend(delimiter)
        else:
            result.extend(letters[0])
            for word, delimiter in zip(letters[1:], delimiters):
                result.extend(delimiter)
                result.extend(word)
    else:
        if len(letters) == len(delimiters):
            for word, delimiter in zip(letters, delimiters):
                result.extend(delimiter)
                result.extend(word)
        else:
            result.extend(delimiters[0])
            for word, delimiter in zip(letters, delimiters[1:]):
                result.extend(word)
                result.extend(delimiter)
    result = "".join(result)
    return result


assert reverse_word("hello/world:here/") == "here/world:hello/"
assert reverse_word("hello//world:here") == "here//world:hello"
