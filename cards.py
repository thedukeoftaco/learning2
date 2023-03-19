import random

# input by hand just so I can easily visualize and test
# 4 suits: green, black, pink, & blue / 13 numbers in each suit
deck = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10', 'g11', 'g12', 'g13',
        'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k10', 'k11', 'k12', 'k13',
        'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13',
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13']

hand = []

stack = []

# workaround to test if hand is empty
bandaid = []

# draws a hand of 13 from the deck at random and removes it from deck
n = 0
while n < 13:
    hand += random.choices(deck, k=1)
    n += 1
    for card in hand:
        if card in deck:
            deck.remove(card)

# I'll figure out how to sort this properly later...
hand.sort()
print('Your hand:')
print(hand)
print('Please type a card to play it. You can also look at your hand by typing "hand".')

# asks you to play a card & checks if it is in your hand
while hand != bandaid:  # this part wasn't working when using "None" so I used a workaround
    inp = input('> ')
    if inp == 'hand':
        print(hand)
        continue
    elif inp in hand:
        print('Played ' + inp + '.')
        hand.remove(inp)
    else:
        print('You do not have a ' + inp + '.')

# should I make a class of cards with each card being an object?
