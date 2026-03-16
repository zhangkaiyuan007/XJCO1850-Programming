'''
In this file, you have two Classes, Card and Deck.

Both have been set up with some basic methods (constructors, and a couple of dunder methods)

Deck has two methods which need completing - shuffle and deal.

With these methods, you should be able to create almost any card game which you can think of!

I recommend having a go at implementing one of:
- snap (easiest)
- blackjack (easy scoring)
- baccarat (slightly harder scoring)
- poker (more difficult)


If you have another card game you want to implement - go for it!

You can edit/add to/change these classes are you need to.
'''

import random

class Card:
    '''
    Class to represent a single playing card.
    '''

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        return f"{self.rank} of {self.suite}"


class Deck:

    '''
    Class to represent a deck of cards.
    '''

    SUITES = ["HEARTS", "SPADES", "CLUBS", "DIAMONDS"]
    RANKS = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

    def __init__(self, is_shuffled):
        ''' boolean input for whether the deck needs to be shuffled on creation or not '''
        self.deck = []
        for suite in self.SUITES:
            for rank in self.RANKS:
                self.deck.append(Card(rank,suite))
        if is_shuffled:
            self.shuffle()

    # NEEDS COMPLETING
    def shuffle(self):
        ''' shuffle the list in place '''
        pass

    # NEEDS COMPLETING
    def deal(self):
        ''' return the top item from the deck & remove'''
        pass

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return "\n".join([str(c) for c in self.deck])


# Implement a card game!