# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# Suppose you are given a table of currency exchange rates, represented as a 2D
# array. Determine whether there is a possible arbitrage: that is, whether there
# is some sequence of trades you can make, starting with some amount A of any
# currency, so that you can end up with some amount greater than A of that
# currency.
#
# There are no transaction costs and you can trade fractional quantities.
#
#
# --------------------------------------------------------------------------------
#
#
def find_arbitrages(currency_exchange_rates_list, currency_list, currency_dict):
    sequence_of_trade_list = []
    for i in range(2, len(currency_list) + 1):
        sequence_of_trade_list += permutations_update(list(permutations(currency_list, i)))
    value = 0
    for sequence in sequence_of_trade_list:
        amount_of_money = 10000
        amount_before_tradings = amount_of_money
        for pair in sequence:
            amount_of_money = amount_of_money * currency_exchange_rates_list[currency_dict.get(pair[0])][currency_dict.get(pair[1])]
        if amount_of_money / amount_before_tradings > value:
            value = amount_of_money / amount_before_tradings
            path = sequence
    return path, value


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:
            return


def permutations_update(list):
    new_list = []
    for i in range(0, len(list)):
        tmp = []
        for j in range(0, len(list[i])):
            if j != (len(list[i]) - 1):
                tmp.append([list[i][j], list[i][j + 1]])
            else:
                tmp.append([list[i][j], list[i][0]])
        new_list.append(tmp)
    return(new_list)


currency_exchange_rates_list = [[1, 0.7141, 0.6164, 1.0826, 1.1006],
                                [1.4004, 1, 0.8632, 1.5160, 1.5412],
                                [1.6223, 1.1585, 1, 1.7563, 1.7855],
                                [0.9237, 0.6596, 0.5694, 1, 1.0166],
                                [0.9086, 0.6488, 0.5601, 0.9836, 1]]

currency_list = ["USD", "EUR", "GBP", "CHF", "CAD"]
currency_dict = {"USD": 0, "EUR": 1, "GBP": 2, "CHF": 3, "CAD": 4}


print(find_arbitrages(currency_exchange_rates_list, currency_list, currency_dict))


print('{0:10}{1:10}{2:10}{3:10}{4:10}{5:10}'.format("", "USD", "EUR", "GBP", "CHF", "CAD"))
print("USD", end="")
for item in currency_exchange_rates_list[0]:
    print('{0:10}'.format(item), end="")
print()
print("EUR", end="")
for item in currency_exchange_rates_list[1]:
    print('{0:10}'.format(item), end="")
print()
print("GBP", end="")
for item in currency_exchange_rates_list[2]:
    print('{0:10}'.format(item), end="")
print()
print("CHF", end="")
for item in currency_exchange_rates_list[3]:
    print('{0:10}'.format(item), end="")
print()
print("CAD", end="")
for item in currency_exchange_rates_list[4]:
    print('{0:10}'.format(item), end="")
