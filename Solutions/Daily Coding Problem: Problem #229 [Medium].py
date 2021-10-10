# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Flipkart.
#
# Snakes and Ladders [https://en.wikipedia.org/wiki/Snakes_and_Ladders] is a game
# played on a 10 x 10 board, the goal of which is get from square 1 to square 100.
# On each turn players will roll a six-sided die and move forward a number of
# spaces equal to the result. If they land on a square that represents a snake or
# ladder, they will be transported ahead or behind, respectively, to a new square.
#
# Find the smallest number of turns it takes to play snakes and ladders.
#
# For convenience, here are the squares representing snakes and ladders, and their
# outcomes:
#
# snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
# ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
#
#
#
# --------------------------------------------------------------------------------
#
#
class Snakes_and_Ladders(object):
    def __init__(self):
        super(Snakes_and_Ladders, self).__init__()
        self.snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_snake_and_ladder(self, pos):
        if pos in self.snakes:
            return self.snakes[pos]
        if pos in self.ladders:
            return self.ladders[pos]
        return pos


def find_smallest_number_of_turn(game):
    def play_game_hepler():
        start_position = 1
        tmp_position = []
        for i in range(1, 7):
            tmp_position.append(start_position + i)
        return tmp_position

    def play_game(current_position, turn):
        tmp = []
        for pos in current_position:
            for i in range(1, 7):
                new_position = game.check_snake_and_ladder(pos + i)
                if new_position > 100:
                    continue
                elif new_position == 100:
                    return turn + 1
                elif new_position not in visited:
                    visited.add(new_position)
                    tmp.append(new_position)
        return play_game(tmp, turn + 1)

    visited = set()
    first_positions = play_game_hepler()
    min_turn_number = play_game(first_positions, turn=1)
    return min_turn_number


SaL = Snakes_and_Ladders()
assert find_smallest_number_of_turn(SaL) == 8
