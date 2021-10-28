# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Palantir.
#
# In academia, the h-index is a metric used to calculate the impact of a
# researcher's papers. It is calculated as follows:
#
# A researcher has index h if at least h of her N papers have h citations each. If
# there are multiple h satisfying this formula, the maximum is chosen.
#
# For example, suppose N = 5, and the respective citations of each paper are [4,
# 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with
# at least 3 citations.
#
# Given a list of paper citations of a researcher, calculate their h-index.
#
#
# --------------------------------------------------------------------------------
#
#
def find_h_index(citations_list: list) -> int:
    h_index = 0
    for item in citations_list:
        h = 0
        for citations in citations_list:
            if citations >= item:
                h += 1
        if h >= item:
            h_index = max(h_index, item)
    return h_index


find_h_index([4, 3, 0, 1, 5])
