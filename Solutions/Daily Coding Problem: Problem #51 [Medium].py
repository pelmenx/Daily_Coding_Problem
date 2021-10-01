# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a function that generates perfectly random numbers between 1 and k
# (inclusive), where k is an input, write a function that shuffles a deck of cards
# represented as an array using only swaps.
#
# It should run in O(N) time.
#
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def shuffle():
    deck = [i for i in range(52)]
    for i, item in enumerate(deck):
        swap_item = rand(len(deck) - 1, i)
        deck[i], deck[swap_item] = deck[swap_item], deck[i]
    return deck


def rand(k, i):
    random = randint(0, k)
    return random


print(shuffle())
