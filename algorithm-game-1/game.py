"""
Name:   Jake Billings
Date:   10/10/2017
Class:  CSCI2511 Discrete Structures
Desc:   Implementation of a theoretical perfect strategy of the game from HW 2.9
Status: Runs on Python on my Mac
"""



"""
Implementation of a theoretical perfect strategy of the game from HW 2.9

Executes one round of game play using this strategy (for player 2)

decks - An array where the first element represents the number of cards in the left deck
        and the second element represents the number of cards in the right deck;

"""
def strategy_perfect(decks):
    # If the left is empty, take all the cards from the right
    if decks[0] > 0:
        decks[1] = 0
    # If the right is empty, take all the cards from the left
    if decks[1] > 0:
        decks[0] = 0

    # If there is only one card in the left, take all the cards in the right except one
    if decks[0] == 1:
        decks[1] = 1

    # Default strategy is to take all of the cards from the right except for one
    decks[1] = 1
