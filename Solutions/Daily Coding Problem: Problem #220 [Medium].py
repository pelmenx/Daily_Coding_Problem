# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Square.
#
# In front of you is a row of N coins, with values v1, v1, ..., vn.
#
# You are asked to play the following game. You and an opponent take turns
# choosing either the first or last coin from the row, removing it from the row,
# and receiving the value of the coin.
#
# Write a program that returns the maximum amount of money you can win with
# certainty, if you move first, assuming your opponent plays optimally.
#
#
# --------------------------------------------------------------------------------
#
#
from sys import maxsize


class Game(object):
    def __init__(self, arg):
        super(Game, self).__init__()
        self.board = arg
        self.player_1_score = 0
        self.player_2_score = 0
        self.log = []
        self.white_to_move = True

    def possible_moves(self):
        moves = []
        if len(self.board) > 1:
            if self.white_to_move:
                moves.append([self.board[1:], self.player_1_score + self.board[0], self.player_2_score, self.log + [[self.board[0], self.white_to_move, 0]]])
                moves.append([self.board[:-1], self.player_1_score + self.board[-1], self.player_2_score, self.log + [[self.board[-1], self.white_to_move, 1]]])
            else:
                moves.append([self.board[1:], self.player_1_score, self.player_2_score + self.board[0], self.log + [[self.board[0], self.white_to_move, 0]]])
                moves.append([self.board[:-1], self.player_1_score, self.player_2_score + self.board[-1], self.log + [[self.board[-1], self.white_to_move, 1]]])
        elif len(self.board) == 1:
            if self.white_to_move:
                moves.append([self.board[1:], self.player_1_score + self.board[0], self.player_2_score, self.log + [[self.board[0], self.white_to_move, 0]]])
            else:
                moves.append([self.board[1:], self.player_1_score, self.player_2_score + self.board[0], self.log + [[self.board[0], self.white_to_move, 0]]])
        return moves

    def make_move(self, move):
        board = move[0]
        player_1_score = move[1]
        player_2_score = move[2]
        log = move[3]

        self.board = board
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score
        self.log = log
        self.white_to_move = not self.white_to_move

    def undo_move(self):
        last_move = self.log[-1]
        item = last_move[0]
        white_to_move = last_move[1]
        position = last_move[2]

        if white_to_move:
            self.player_1_score - item
            if position == 0:
                self.board.insert(0, item)
            else:
                self.board.append(item)
        else:
            self.player_2_score - item
            if position == 0:
                self.board.insert(0, item)
            else:
                self.board.append(item)

        self.log.pop()
        self.white_to_move = not self.white_to_move


def play(game):
    def negamax_ab(game, next_moves, alpha, beta, turn_multiplier):
        if not game.board:
            return turn_multiplier * (game.player_1_score - game.player_2_score)

        max_score = -maxsize
        for move in next_moves:
            game.make_move(move)
            next_moves_ = game.possible_moves()
            score = -negamax_ab(game, next_moves_, -beta, -alpha, -turn_multiplier)
            if score > max_score:
                max_score = score
            game.undo_move()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score

    possible_moves = game.possible_moves()

    difference = negamax_ab(game, possible_moves, -maxsize, maxsize, 1 if game.white_to_move else -1)
    return int(sum(game.board) / 2 + difference / 2)


game = Game([1, 2, 3, 4])
assert play(game) == 6

game = Game([1, 2, 3, 4, 5])
assert play(game) == 9

game = Game([1, 2, 3, 4, 5, 6])
assert play(game) == 12
