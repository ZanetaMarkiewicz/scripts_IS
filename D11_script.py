import random
import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import os


class Card(object):
    FIGURES = ["ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "jack", "queen", "king"]
    COLORS = ["hearts", "clubs", "diamonds", "spades"]

    def __init__(self, figure, color):
        self.__figure = figure
        self.__color = color

    def __str__(self):
        return f"{self.__figure} of {self.__color}"


class CardDeck(object):
    def __init__(self):
        self.__deck = []
        for figure in Card.FIGURES:
            for color in Card.COLORS:
                self.__deck.append(Card(figure, color))

    def shuffle(self):
        random.shuffle(self.__deck)

    def cards_count(self):
        return len(self.__deck)

    def __str__(self):
        return self.show_all_the_cards()

    def show_all_the_cards(self):
        # string_to_return = ""
        # for card in self.__deck:
        #     string_to_return += str(card) + "\n"
        all_cards = "\n".join(str(x) for x in self.__deck)
        return all_cards


deck_of_cards = CardDeck()
deck_of_cards.shuffle()
print(deck_of_cards)
