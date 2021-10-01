# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Affirm.
#
# Given a array of numbers representing the stock prices of a company in
# chronological order, write a function that calculates the maximum profit you
# could have made from buying and selling that stock. You're also given a number
# fee that represents a transaction fee for each buy and sell transaction.
#
# You must buy before you can sell the stock, but you can make as many
# transactions as you like.
#
# For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since
# you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4
# dollars and sell it at 10 dollars. Since we did two transactions, there is a 4
# dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


def find_profit(array, fee):
    predicted_profit = [0] * len(array)

    def find_max_profit(array_, position=0, buy_price=maxsize, current_profit=0):
        nonlocal predicted_profit
        for i, item in enumerate(array_[position:]):
            if position + i > 0:
                if predicted_profit[position + i - 1] > predicted_profit[position + i]:
                    predicted_profit[position + i] = predicted_profit[position + i - 1]
            if item < buy_price:
                buy_price = item
            elif item - fee > buy_price and max(predicted_profit[:position + i + 1]) < item - fee - buy_price + current_profit:
                predicted_profit[position + i] = item - fee - buy_price + current_profit
                yield from find_max_profit(array_, position + i + 1, buy_price, current_profit + 0)
                yield from find_max_profit(array_, position + i + 1, maxsize, current_profit + item - fee - buy_price)
        yield current_profit
    max_profit = 0
    for profit in find_max_profit(array):
        max_profit = max(profit, max_profit)
    return max_profit


assert find_profit([1, 3, 2, 8, 4, 10], 2) == 9
