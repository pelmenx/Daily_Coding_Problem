# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an array of numbers representing the stock prices of a company in
# chronological order and an integer k, return the maximum profit you can make
# from k buys and sells. You must buy the stock before you can sell it, and you
# must sell the stock before you can buy it again.
#
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def best_value(array, k):
    value_list = []
    buy_price = maxsize
    sell_price = None
    for i, item in enumerate(array):
        if item <= buy_price:
            if sell_price:
                value_list.append(sell_price - buy_price)
                buy_price = item
                sell_price = None
            else:
                buy_price = item
        else:
            if sell_price:
                if sell_price < item:
                    sell_price = item
            else:
                sell_price = item
            if i == len(array) - 1:
                value_list.append(sell_price - buy_price)
    if len(value_list) > k:
        for i in range(len(value_list) - k):
            value_list.remove(min(value_list))
    return sum(value_list)


print(best_value([5, 2, 4, 0, 1], 2))
