# ask professor
import numpy as np
import random

def explore():
    return random.choice(playable_cards)
def exploit():
    return values.index(max(values)) # gives the max value card
def Black_Choice():
    if random.random() > epsilon:
        return exploit()
    else:
        return explore() # till we find the max val card
def update(red_choice, black_choice):
    winner = payoff_Black[red_choice, black_choice]
    counts[black_choice] += 1
    reward[black_choice] += winner

    values[black_choice] = float(reward[black_choice])/float(counts[black_choice])

playable_cards = [0, 1, 2, 3]
# 0 = king | 1 = Ace | 2 = Card No. 2 of Spades | 3 = Card No. 3 of Spades
epsilon = 0.1

reward = [0, 0, 0, 0]
counts = [0, 0, 0, 0]
values = [0, 0, 0, 0]

payoff_Black = np.array([
    [-1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1]
])

def play(i):
    for x in range(i):
        red_choice = np.random.choice(playable_cards, p =[0.4, 0.2, 0.2, 0.2])
        black_choice = Black_Choice()
        update(red_choice, black_choice)

        i += 1
    print(reward)
    print(counts)
    print(values)

play(10000)