import collections
from pprintpp import pprint as pprint

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA") 
    # => ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    suits = "spades diamonds clubs hearts".split()
    # => ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        # => [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), ...]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



if __name__ == "__main__":
    beer_card = Card("7", "diamonds")
    pprint(beer_card) # => Card(rank='7', suit='diamonds')
    print()

    deck = FrenchDeck()

    pprint(len(deck)) # => 52
    print()

    pprint(deck[0]) # => Card(rank='2', suit='spades')
    print()

    pprint(deck[-1]) # => Card(rank='A', suit='hearts')
    print()

    pprint(deck[:3]) # => [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    print()

    pprint(deck[12::13]) # => [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
    # note that the 12::13 is a slice, and it means start at 12, and take every 13th card
    print()

    # for card in deck:
    #     print(card)
