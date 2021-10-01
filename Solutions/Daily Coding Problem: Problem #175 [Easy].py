# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given a starting state start, a list of transition probabilities for a
# Markov chain, and a number of steps num_steps. Run the Markov chain starting
# from start for num_steps and compute the number of times we visited each state.
#
# For example, given the starting state a, number of steps 5000, and the following
# transition probabilities:
#
# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]
#
#
# One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656,
# 'c': 332 }.
#
#
# --------------------------------------------------------------------------------
#
#
from random import random


def markov_chain(starting_state, num_steps):
    probabilities = [('a', 'a', 0.9),
                     ('a', 'b', 0.075),
                     ('a', 'c', 0.025),
                     ('b', 'a', 0.15),
                     ('b', 'b', 0.8),
                     ('b', 'c', 0.05),
                     ('c', 'a', 0.25),
                     ('c', 'b', 0.25),
                     ('c', 'c', 0.5)]
    visited_node_dict = {}
    visited_node_dict[starting_state] = 1
    while num_steps > 0:
        rand = random()
        prob = 0
        for path in probabilities:
            if path[0] == starting_state:
                prob += path[2]
                if rand <= prob:
                    if path[1] in visited_node_dict:
                        visited_node_dict[path[1]] += 1
                    else:
                        visited_node_dict[path[1]] = 1
                    starting_state = path[1]
                    num_steps -= 1
                    break
    print(visited_node_dict)


markov_chain("a", 5000)
