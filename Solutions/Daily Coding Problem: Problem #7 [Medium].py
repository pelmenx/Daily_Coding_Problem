# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.
#
#
# --------------------------------------------------------------------------------
#
#
def encoder(encode_text, mapper=[]):
    global value
    if len(encode_text) == 1:
        try:
            mapper = value[-1][1].split(" ")
        except IndexError:
            pass
        finally:
            mapper.append(encode_text)
            count = mapping(mapper, 1)
    elif len(encode_text) == 2:
        if int(encode_text) >= 1 and int(encode_text) <= 26:
            try:
                mapper = value[-1][1].split(" ")
            except IndexError:
                pass
            finally:
                mapper.append(encode_text)
                count = mapping(mapper, 2)
                try:
                    mapper = value[-1][1].split(" ")
                except IndexError:
                    mapper.clear()
                finally:
                    mapper.append(encode_text[0])
                    mapper.append(encode_text[1])
                    count = mapping(mapper, count)
        else:
            try:
                mapper = value[-1][1].split(" ")
            except IndexError:
                pass
            finally:
                mapper.append(encode_text[0])
                mapper.append(encode_text[1])
                count = mapping(mapper, 1)
    else:
        if value == []:
            value.append([1, encode_text[:1]])
        else:
            i = value[len(value) - 1][0]
            i += 1
            j = value[len(value) - 1][1]
            j = j + " " + encode_text[:1]
            value.append([i, j])
        count = encoder(encode_text[1:])
        if int(encode_text[:2]) >= 1 and int(encode_text[:2]) <= 26:
            tmp_length = length - len(encode_text)
            check = 0
            for item in value:
                if item[0] == tmp_length:
                    check = 1
                    ind = value.index(item) + 1
            if check == 1:
                value = value[:ind]
                i = value[len(value) - 1][0]
                i += 2
                j = value[len(value) - 1][1]
                j = j + " " + encode_text[:2]
                value.append([i, j])
            else:
                value = []
                value.append([2, encode_text[:2]])

            count += encoder(encode_text[2:])

    return count


def mapping(mapper, count, encrypted_text=""):
    map = {"1": "a", "2": "b", "3": "c", "4": "d",
           "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
           "10": "j", "11": "k", "12": "l", "13": "m", "14": "n",
           "15": "o", "16": "p", "17": "q", "18": "r", "19": "s", "20": "t",
           "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
    try:
        for ref in mapper:
            encrypted_text += map[ref]
        print(mapper, encrypted_text)
    except KeyError:
        count -= 1
    finally:
        return count


value = []
text = "111"
length = len(text)
print("number of ways", text, "can be decoded", encoder(text))
