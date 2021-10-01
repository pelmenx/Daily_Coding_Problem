# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a
# prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal],
# return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to
# speed up queries.
#
#
# --------------------------------------------------------------------------------
#
#
def autocomplete(query, set_string):
    autocomplete_set = []
    for string in set_string:
        if query in string:
            autocomplete_set.append(string)
    return autocomplete_set


print(autocomplete("de", ["dog", "deer", "deal"]))
