# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Triplebyte.
#
# You are given n numbers as well as n probabilities that sum up to 1. Write a
# function to generate one of the numbers with its corresponding probability.
#
# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2,
# 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3
# and 4 20% of the time.
#
# You can generate random numbers between 0 and 1 uniformly.
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def generate_numbers(numbers_list, numbers_probability):
    probabilities_list = []
    for probability in numbers_probability:
        probability = probability * 10
        if not probabilities_list:
            probabilities_list.append((0, probability - 1))
        else:
            probabilities_list.append((probabilities_list[-1][1] + 1, probabilities_list[-1][1] + probability))
    probabilities_dict = {}
    for key, value in zip(probabilities_list, numbers_list):
        probabilities_dict[key] = value
    probability = randint(0, 9)
    for key in probabilities_dict.keys():
        if key[0] <= probability <= key[1]:
            return probabilities_dict[key]


result_dict = {}
for i in range(1000000):
    result = generate_numbers([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
    if result not in result_dict:
        result_dict[result] = 1
    else:
        result_dict[result] += 1
print(result_dict)
