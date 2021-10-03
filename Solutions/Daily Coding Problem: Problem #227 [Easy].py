# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many
# words as possible that can be formed by a sequence of adjacent letters in the
# grid, using each cell at most once. Given a game board and a dictionary of valid
# words, implement a Boggle solver.
#
#
# --------------------------------------------------------------------------------
#
#
class Boggle(object):
    def __init__(self):
        super(Boggle, self).__init__()
        self.board = [['e', 'i', 'p', 'k'],
                      ['g', 'l', 'a', 'm'],
                      ['a', 'e', 'u', 'f'],
                      ['d', 'o', 'p', 'o']]
        self.row_number = 4
        self.col_number = 4

        self.valid_words_list = {"dope", "gale", "pale", "pile", "lie", "gad", "dag", "pie", "male", "fuel", "pod"}


def solve_boggle_game(boggle):
    def solve(i, j, word):
        if len(word) >= 3:
            yield word
        visited.add((i, j))
        if i + 1 < boggle.row_number and (i + 1, j) not in visited:
            yield from solve(i + 1, j, word + boggle.board[i + 1][j])
            visited.remove((i + 1, j))
        if i - 1 >= 0 and (i - 1, j) not in visited:
            yield from solve(i - 1, j, word + boggle.board[i - 1][j])
            visited.remove((i - 1, j))
        if j + 1 < boggle.col_number and (i, j + 1) not in visited:
            yield from solve(i, j + 1, word + boggle.board[i][j + 1])
            visited.remove((i, j + 1))
        if j - 1 >= 0 and (i, j - 1) not in visited:
            yield from solve(i, j - 1, word + boggle.board[i][j - 1])
            visited.remove((i, j - 1))
        if i + 1 < boggle.row_number and j + 1 < boggle.col_number and (i + 1, j + 1) not in visited:
            yield from solve(i + 1, j + 1, word + boggle.board[i + 1][j + 1])
            visited.remove((i + 1, j + 1))
        if i + 1 < boggle.row_number and j - 1 >= 0 and (i + 1, j - 1) not in visited:
            yield from solve(i + 1, j - 1, word + boggle.board[i + 1][j - 1])
            visited.remove((i + 1, j - 1))
        if i - 1 >= 0 and j + 1 < boggle.col_number and (i - 1, j + 1) not in visited:
            yield from solve(i - 1, j + 1, word + boggle.board[i - 1][j + 1])
            visited.remove((i - 1, j + 1))
        if i - 1 >= 0 and j - 1 >= 0 and (i - 1, j - 1) not in visited:
            yield from solve(i - 1, j - 1, word + boggle.board[i - 1][j - 1])
            visited.remove((i - 1, j - 1))

    visited = set()
    words = set()
    for i_ in range(boggle.row_number):
        for j_ in range(boggle.col_number):
            for word_ in solve(i_, j_, boggle.board[i_][j_]):
                if word_ in boggle.valid_words_list:
                    words.add(word_)
            visited.remove((i_, j_))
    return words


boggle = Boggle()
assert solve_boggle_game(boggle) == boggle.valid_words_list
