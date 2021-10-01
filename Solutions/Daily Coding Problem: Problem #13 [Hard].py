# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that
# contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct
# characters is "bcb".
#
#
# --------------------------------------------------------------------------------
#
#
def longest_substring_with_k_distinct_characters(string, k):
    length = 0
    for i in range(0, len(string)):
        if len(string) - i > length:
            substring = ""
            distinct_characters = []
            distinct_characters.append(string[i])
            for j in range(i, len(string)):
                if string[j] not in distinct_characters:
                    distinct_characters.append(string[j])
                if len(distinct_characters) > k:
                    if len(substring) > length:
                        length = len(substring)
                        longest_substrin = substring
                    break
                substring += string[j]
        else:
            return(length, longest_substrin)
    return(len(string), string)


print(longest_substring_with_k_distinct_characters("abcba", 2))
print(longest_substring_with_k_distinct_characters("abccbba", 2))
print(longest_substring_with_k_distinct_characters("abcbbbabbcbbadd", 2))
print(longest_substring_with_k_distinct_characters("abcbbbaaaaaaaaaabbcbbadd", 1))
print(longest_substring_with_k_distinct_characters("abccbba", 3))
