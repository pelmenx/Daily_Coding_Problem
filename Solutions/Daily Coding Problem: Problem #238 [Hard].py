# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by MIT.
#
# Blackjack [https://en.wikipedia.org/wiki/Blackjack] is a two player card game
# whose rules are as follows:
#
#  * The player and then the dealer are each given two cards.
#  * The player can then "hit", or ask for arbitrarily many additional cards, so
#    long as their total does not exceed 21.
#  * The dealer must then hit if their total is 16 or lower, otherwise pass.
#  * Finally, the two compare totals, and the one with the greatest sum not
#    exceeding 21 is the winner.
#
# For this problem, cards values are counted as follows: each card between 2 and
# 10 counts as their face value, face cards count as 10, and aces count as 1.
#
# Given perfect knowledge of the sequence of cards in the deck, implement a
# blackjack solver that maximizes the player's score (that is, wins minus losses).
#
#
# --------------------------------------------------------------------------------
#
#
from random import shuffle
from collections import defaultdict


class BlackJack():
    def __init__(self):
        self.cards_value = {2: 2,
                            3: 3,
                            4: 4,
                            5: 5,
                            6: 6,
                            7: 7,
                            8: 8,
                            9: 9,
                            10: 10,
                            "J": 10,
                            "Q": 10,
                            "K": 10,
                            "A": 1}
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.player_hand_sum = 0
        self.dealer_hand_sum = 0
        self.number_of_starting_cards = 2

    def start_new_game(self):
        self.shuffle_deck()
        self.initialize_player_hand()
        self.initialize_dealer_hand()

    def shuffle_deck(self):
        new_deck = list(self.cards_value) * 4
        shuffle(new_deck)
        self.deck = new_deck

    def initialize_player_hand(self):
        self.player_hand = []
        for _ in range(self.number_of_starting_cards):
            self.player_hand.append(self.deck.pop())
        self.player_hand_sum = sum([self.cards_value[x] for x in self.player_hand])

    def initialize_dealer_hand(self):
        self.dealer_hand = []
        for _ in range(self.number_of_starting_cards):
            self.dealer_hand.append(self.deck.pop())
        self.dealer_hand_sum = sum([self.cards_value[x] for x in self.dealer_hand])

    def player_hit(self):
        hitted_card = self.deck.pop()
        self.player_hand.append(hitted_card)
        self.player_hand_sum += self.cards_value[hitted_card]

    def dealer_hit(self):
        hitted_card = self.deck.pop()
        self.dealer_hand.append(hitted_card)
        self.dealer_hand_sum += self.cards_value[hitted_card]

    def dealer_hit_back(self):
        hitted_back_card = self.dealer_hand.pop()
        self.dealer_hand_sum -= self.cards_value[hitted_back_card]
        self.deck.append(hitted_back_card)

    def compare(self):
        if self.dealer_hand_sum < self.player_hand_sum <= 21:
            return "Player win"
        elif self.player_hand_sum < self.dealer_hand_sum <= 21:
            return "Dealer win"
        elif self.player_hand_sum <= 21 and self.dealer_hand_sum > 21:
            return "Player win"
        elif self.dealer_hand_sum <= 21 and self.player_hand_sum > 21:
            return "Dealer win"
        else:
            return "Draw"


def blackjack_solver(game):
    def simulate_game():
        while True:
            i = 0
            while game.dealer_hand_sum < 17:
                i += 1
                game.dealer_hit()
            yield game.compare()
            for _ in range(i):
                game.dealer_hit_back()
            if game.player_hand_sum > 21:
                break
            game.player_hit()

    game.start_new_game()
    result = set()
    for game_result in simulate_game():
        if game_result == "Player win":
            return game_result
        result.add(game_result)
    if "Draw" in result:
        return "Draw"
    else:
        return "Dealer win"


BJ = BlackJack()
results = defaultdict(int)
for _ in range(1000):
    res = blackjack_solver(BJ)
    results[res] += 1

print(results)
