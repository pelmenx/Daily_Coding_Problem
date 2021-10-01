# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Salesforce.
#
# Connect 4 is a game where opponents take turns dropping red or black discs into
# a 7 x 6 VERTICAL_LINESly suspended grid. The game ends either when one player creates
# a line of four consecutive discs of their color (HORIZONTAL_LINESly, VERTICAL_LINESly, or
# diagonally), or when there are no more spots left in the grid.
#
# Design and implement Connect 4.
#
#
# --------------------------------------------------------------------------------
#
#
import pygame as p
import sys


WIDTH_TABLE = 560
HIGH_TABLE = 480
HORIZONTAL_LINES = 6
VERTICAL_LINES = 7
SQUARE_SIZE = WIDTH_TABLE // 7


class Connect_4(object):
    def __init__(self):
        super(Connect_4, self).__init__()
        self.board = [[None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None]]
        self.to_move = True
        self.screen = p.display.set_mode((WIDTH_TABLE, HIGH_TABLE))
        self.gave_over = False

    def draw_board(self):
        p.display.set_caption("Connect 4")
        self.screen.fill(p.Color("white"))
        for i in range(1, VERTICAL_LINES + 1):
            p.draw.line(self.screen, "black", (0, i * SQUARE_SIZE), (WIDTH_TABLE, i * SQUARE_SIZE))
        for i in range(1, HORIZONTAL_LINES + 1):
            p.draw.line(self.screen, "black", (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HIGH_TABLE))
        p.display.update()

    def make_move(self, row, column):
        if self.to_move:
            p.draw.circle(self.screen, "blue", (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
            self.board[row][column] = 0
            p.display.update()
        else:
            p.draw.circle(self.screen, "red", (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2)
            self.board[row][column] = 1
            p.display.update()
        self.check_board(row, column)
        self.to_move = not self.to_move

    def check_board(self, row, column):
        for i in range(4):
            if column - i >= 0 and column - i + 3 < VERTICAL_LINES:
                if len(set(self.board[row][column - i:column - i + 4])) == 1:
                    print(self.to_move, "win horz")
                    return self.game_over()
            if row - i >= 0 and row - i + 3 < HORIZONTAL_LINES:
                if len(set([self.board[row - i][column], self.board[row - i + 1][column], self.board[row - i + 2][column], self.board[row - i + 3][column]])) == 1:
                    print(self.to_move, "win vert")
                    return self.game_over()
            if column - i >= 0 and column - i + 3 < VERTICAL_LINES and row - i >= 0 and row - i + 3 < HORIZONTAL_LINES:
                if len(set([self.board[row - i][column - i], self.board[row - i + 1][column - i + 1], self.board[row - i + 2][column - i + 2], self.board[row - i + 3][column - i + 3]])) == 1:
                    print(self.to_move, "win diag left")
                    return self.game_over()
            if row + 3 - i < HORIZONTAL_LINES and row + 3 - i >= 0 and column - 3 + i >= 0 and column - 3 + i < VERTICAL_LINES:
                if row - i < HORIZONTAL_LINES and row - i >= 0 and column + i >= 0 and column + i < VERTICAL_LINES:
                    if len(set([self.board[row + 3 - i][column - 3 + i], self.board[row + 2 - i][column - 2 + i], self.board[row + 1 - i][column - 1 + i], self.board[row - i][column + i]])) == 1:
                        print(self.to_move, "win diag left")
                        return self.game_over()

    def game_over(self):
        end_font = p.font.Font(None, SQUARE_SIZE * 2)
        if self.to_move:
            end_text = end_font.render("Blue win", True, "black")
            text_rect = end_text.get_rect(center=(WIDTH_TABLE // 2, HIGH_TABLE // 2))
            self.screen.blit(end_text, text_rect)
        else:
            end_text = end_font.render("Red win", True, "black")
            text_rect = end_text.get_rect(center=(WIDTH_TABLE // 2, HIGH_TABLE // 2))
            self.screen.blit(end_text, text_rect)

        font = p.font.Font(None, int(SQUARE_SIZE * 0.65))
        restart_text = font.render("press 'R' to restart the game", True, "black")
        restart_text_rect = end_text.get_rect(center=(WIDTH_TABLE // 2, HIGH_TABLE // 1.3))
        self.screen.blit(restart_text, restart_text_rect)
        self.gave_over = True
        p.display.update()


def main():
    p.init()
    game = Connect_4()
    game.draw_board()
    while True:
        for event in p.event.get():
            if not game.gave_over:
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if game.board[row][col] is None:
                        game.make_move(row, col)
            else:
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_r:
                        game = Connect_4()
                        game.draw_board()


if __name__ == "__main__":
    main()
