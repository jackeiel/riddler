#! /usr/bin/env python

'''
You are playing your first ever game of Ticket to Ride, a board game in
which players compete to lay down railroad while getting so competitive they
risk ruining their marriages. At the start of the game, you are randomly dealt
a set of three Destination Tickets out of a deck of 30 different tickets. Each
reveals the two terminals you must connect with a railroad to receive points.
During the game, you eventually pick up another set of three Destination Tickets,
so you have now seen six of the 30 tickets in the game.
'''

'''
Later, because you enjoyed it so much, you and your friends play a second game.
The ticket cards are all returned and reshuffled. Again, you are dealt a set of
three tickets to begin play. Which is more likely: that you had seen at least
one of these three tickets before, or that they were all new to you?

SOLUTION:
https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/

'''

import numpy as np
from collections import deque
import statistics

def games():
    tickets = deque(range(1,31))
    np.random.shuffle(tickets)
    hand1 = []
    for i in range(6):
        hand1.append(tickets[i])

    np.random.shuffle(tickets)
    hand2 = []
    for i in range(3):
        hand2.append(tickets[i])

    for i in range(len(hand2)):
        if hand2[i] in hand1:
            return 1
    return 0

def MonteCarlo():
    seen = 0
    for i in range(50000):
        seen += games()
    return seen/50000

def CTL():
    avg = []
    for i in range(100):
        avg.append(MonteCarlo())
    return statistics.mean(avg)

print(CTL())

###########################
#                         #
#   Result: 0.50127       #
#                         #
###########################
