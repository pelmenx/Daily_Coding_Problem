# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two neighboring
# houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nthhouse with kth color, return the minimum cost which achieves this
# goal.
#
#
# --------------------------------------------------------------------------------
#
#
import sys


def find_all_pairs(matrix, counter):
    global list, tmp_list
    if counter > 0:
        for i in range(0, len(matrix[counter])):
            tmp_list.append([i, matrix[counter][i]])
            find_all_pairs(matrix, counter - 1)
            tmp_list.pop()

    else:
        for j in range(0, len(matrix[counter])):
            tmp_list.append([j, matrix[counter][j]])
            # print(tmp_list)
            list.append(tmp_list.copy())
            tmp_list.pop()
    return list


def find_min_cost_for_houses(pairs):
    cost = sys.maxsize
    for pair in pairs:
        tmp_cost = 0
        for i in range(0, len(pair)):
            tmp_cost += pair[i][1]
            if i < len(pair) - 1:
                if pair[i][0] == pair[i + 1][0]:
                    break
            if i == len(pair) - 1:
                if tmp_cost < cost:
                    cost = tmp_cost
    return cost


N_by_K_matrix = [[7, 3, 8, 6, 1, 2],
                 [5, 6, 7, 2, 4, 3],
                 [10, 1, 4, 9, 7, 6],
                 [10, 1, 4, 9, 7, 6]]

list = []
tmp_list = []

print(find_min_cost_for_houses(find_all_pairs(N_by_K_matrix, len(N_by_K_matrix) - 1)))
