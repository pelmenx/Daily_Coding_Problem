# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given a string of digits, generate all possible valid IP address combinations.
#
# IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers
# between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed,
# except for 0 itself.
#
# For example, given "2542540123", you should return ['254.25.40.123',
# '254.254.0.123'].
#
#
# --------------------------------------------------------------------------------
#
#
def find_possible_ip_adresses(string):
    def possible_ip_adresses(string_, address=[], repeat=4):
        if address:
            if len(address[-1]) > 1:
                if address[-1][0] == "0":
                    return
        if repeat == 0:
            if not string_:
                yield address
            else:
                return
        tmp = ""
        for i, digit in enumerate(string_):
            if int(tmp + digit) <= 255:
                yield from possible_ip_adresses(string_[i + 1:], address + [tmp + digit], repeat - 1)
            tmp = tmp + digit

    ip_adresses = []
    for ip in possible_ip_adresses(string):
        ip_address_ = ""
        for item in ip:
            ip_address_ += item + "."
        ip_address_ = ip_address_[:-1]
        ip_adresses.append(ip_address_)
    return ip_adresses


assert find_possible_ip_adresses("2542540123") == ['254.25.40.123', '254.254.0.123']
