# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a 2D matrix of characters and a target word, write a function that returns
# whether the word can be found in the matrix by going left-to-right, or
# up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
#
# and the target word 'FOAM', you should return true, since it's the leftmost
# column. Similarly, given the target word 'MASS', you should return true, since
# it's the last row.
#
#
# --------------------------------------------------------------------------------
#
#
def if_word_in_matrix(matrix, word):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if len(matrix) - i >= len(word) or len(row) - j >= len(word):
                if item == word[0]:
                    column = []
                    for k, line in enumerate(matrix[i:]):
                        column.append(line[j])
                    if list(word) == row[j:] or list(word) == column:
                        return True
            else:
                break
    return False


matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]
word = "FOAM"
print(if_word_in_matrix(matrix, word))
