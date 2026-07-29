class Deck:

    def __init__(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]


    def __len__(self):
        print(self._cards)
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

my_deck = Deck()
print(len(my_deck))       # Output: 52 (Calls __len__)
print(my_deck[0])         # Output: 2 of Spades (Calls __getitem__)
print(my_deck[-1])        # Output: A of Clubs (Calls __getitem__)

# Because __getitem__ exists, Python automatically knows how to loop over it!
for card in my_deck[:3]:
    print(card)
