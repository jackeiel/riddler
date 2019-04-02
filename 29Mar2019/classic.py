#! /usr/bin/env python3

'''
You are competing in a spelling bee alongside nine other contestants.
You can each spell words perfectly from a certain portion of the dictionary but
will misspell any word not in that portion of the book. Specifically, you have 99
percent of the dictionary down cold, and your opponents have 98 percent, 97 percent,
96 percent, and so on down to 90 percent memorized. The bee’s rules are simple:
The contestants take turns spelling in some fixed order, which then restarts with
the first surviving speller at the end of a round. Miss a word and you’re out, and
the last speller standing wins. The bee words are chosen randomly from the dictionary.
'''

'''
First, say the contestants go in decreasing order of their knowledge, so that you go 
first. What are your chances of winning the spelling bee? Second, say the contestants
 go in increasing order of knowledge, so that you go last. What are your chances of 
 winning now?
'''

import random

#spelling bee
def compete(order):
    while len(order)>1:
        elim = []
        for contestant in range(len(order)):
            if random.randint(1,101) in order[contestant]:
                continue
            elim.append(order[contestant])
        # only remove contestants if at least one person spelled a word correctly
        if len(elim) < len(order):
            for contestant in elim:
                order.remove(contestant)
        else:
            continue
    return order[0][-1]

def forw(n):
    fWins = 0
    for i in range(n):
        forward = [range(1, 91), range(1, 92), range(1, 93), range(1, 94), range(1, 95),
                   range(1, 96), range(1, 97), range(1, 98), range(1, 99), range(1, 100)]
        if compete(forward) == 99:
            fWins += 1
    print(float(fWins/n))

def back(n):
    bWins = 0
    for i in range(n):
        backward = [range(1, 100), range(1, 99), range(1, 98), range(1, 97), range(1, 96),
                    range(1, 95), range(1, 94), range(1, 93), range(1, 92), range(1, 91)]
        if compete(backward) == 99:
            bWins += 1
    print(float(bWins/n))

#####################################
#                                   #
#   classic.forw(100000) == 0.39    #
#                                   #
#   classic.back(100000) == 0.39    #
#                                   #
#####################################