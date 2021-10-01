# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Alice wants to join her school's Probability Student Club. Membership dues are
# computed via one of two simple probabilistic games.
#
# The first game: roll a die repeatedly. Stop rolling once you get a five followed
# by a six. Your number of rolls is the amount you pay, in dollars.
#
# The second game: same, except that the stopping condition is a five followed by
# a five.
#
# Which of the two games should Alice elect to play? Does it even matter? Write a
# program to simulate the two games and calculate their expected value.
#
#
# --------------------------------------------------------------------------------
#
#
from random import randint


def probabilistic_games():
    def first_game(prev_roll=None, counter=0):
        if not prev_roll:
            roll = randint(1, 6)
            return first_game(roll, 1)
        else:
            roll = randint(1, 6)
            if prev_roll == 6 and roll == 5:
                return counter
            else:
                return first_game(roll, counter + 1)

    def second_game(prev_roll=None, counter=0):
        if not prev_roll:
            roll = randint(1, 6)
            return second_game(roll, 1)
        else:
            roll = randint(1, 6)
            if prev_roll == 5 and roll == 5:
                return counter
            else:
                return second_game(roll, counter + 1)
    pay1 = first_game()
    pay2 = second_game()
    return pay1, pay2


p1 = 0
p2 = 0
while True:
    p1_, p2_ = probabilistic_games()
    p1 += p1_
    p2 += p2_
    if p1 > 10000000:
        break
print(p1, p2)
# Alice has to play first game.
# Because in case of rolling 6 we can win if next time we roll 5.
# Futhermore there is another optin after rolling 6, next time we can roll 6 again
# that means we are again in one step from win.
# It's impossible in second game, after rolling 5 we have one option to win with
# with next 5. However if we roll anoter number, we have roll again until we get 5
# to have opportunity to to win in next roll
