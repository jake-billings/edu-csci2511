"""
Name:   Jake Billings
Date:   10/10/2017
Class:  CSCI 2511 Discrete Structures
Desc:   Implementation of a theoretical perfect strategy of the game from HW 2.9
Status: Runs on Python on my Mac

The Following file depends on the following game description from HW 2 of CSCI2511 Discrete Structures by Ellen Gethner:

"Suppose that we have two piles of playing cards, each with n cards. Two players play the following game. Each player,
 in turn, chooses one pile and then removes any number cards, but must remove at least one, from the chosen pile. The
 last player to pick up a card or cards wins the game. Prove that the second player can always win the game."
"""


# Implementation of a theoretical perfect strategy of the game from HW 2.9
#
# Executes one round of game play using this strategy (which is perfect for player 2)
#
# decks - An array where the first element represents the number of cards in the left deck
#        and the second element represents the number of cards in the right deck.
#
# Returns an array representing the state of the decks array after the player has played one round
def strategy_perfect(decks):
    # If decks = [0, 0], the game has already halted. There are no cards to pick up.
    #  Throw an error (raise an exception)
    if (decks[0] + decks[1]) < 1:
        raise Exception('Cannot execute a round of strategy on a complete game')

    # If the other player left us only one deck to draw from, we take the card and win.
    # If the left is empty, take all the cards from the right
    if decks[0] == 0:
        decks[1] = 0
    # If the right is empty, take all the cards from the left
    elif decks[1] == 0:
        decks[0] = 0

    # If the other player left only one card in either position, take all except one in the other.
    #  This forces the other player to take one card and leave is in an automatic-win state.
    # If there is only one card in the left, take all the cards in the right except one
    elif decks[0] == 1 and decks[1] > 1:
        decks[1] = 1
    elif decks[1] == 1 and decks[0] > 1:
        decks[0] = 1

    # These will never happen but are included for complete-ness
    #  We would be putting the other player in an automatic-win state
    elif decks[0] == 1 and decks[1] == 1:
        decks[0] = 0
    elif decks[1] == 1 and decks[0] == 1:
        decks[0] = 1

    # Default strategy is to take all of the cards from the right except for one
    else:
        decks[1] = 1

    # Return the new state of the game
    return decks


# Passes strategic decisions to a human so that we can interact with the perfect strategy
#
# Executes one round of game play using human input as its strategy
#
# decks - An array where the first element represents the number of cards in the left deck
#        and the second element represents the number of cards in the right deck.
#
# Returns an array representing the state of the decks array after the player has played one round
def strategy_human(decks):
    # If decks = [0, 0], the game has already halted. There are no cards to pick up.
    #  Throw an error (raise an exception)
    if (decks[0] + decks[1]) < 1:
        raise Exception('Cannot execute a round of strategy on a complete game')

    # Ask which deck to draw cards from
    deck = -1
    while not (0 <= deck < len(decks)) or decks[deck] < 1:
        deck = input("Choose a deck with cards in it to draw from (0 or 1): ")

    # Ask how many cards to draw from the deck
    count = -1
    while not (0 < count <= decks[deck]):
        count = input('Choose how many cards to draw: ')

    # Simulate drawing cards from the deck
    decks[deck] -= count

    # Return the new state of the game
    return decks


# Plays a full game of the game by calling strategy functions repeatedly
#
# n - Integer representing the number of cards to store in each deck
# strategy_player_1 - function that accepts a decks array and returns a new decks array (see strategy_perfect())
# strategy_player_2 - function that accepts a decks array and returns a new decks array (see strategy_perfect())
#
# Returns a boolean representing whether player 1 won
def play_game(n, strategy_player_1, strategy_player_2):
    # An array where the first element represents the number of cards in the left deck
    #  and the second element represents the number of cards in the right deck.
    #  See strategy_perfect()
    decks = [n, n]

    # Print a message for easy debugging
    print "Start with: ", decks

    # Store the current player as a boolean by storing the fact that it's player 1's turn or not
    #  Player 1 is the first player, so this variable starts as true.
    player_1_turn = True

    # The game halts when no cards remain on the table. The last player to pickup a card wins.
    #  Check if the game is over by adding the two decks together and checking if the sum is greater
    #  than 0.
    while (decks[0] + decks[1]) > 0:
        # If it's player 1's turn, execute player 1's strategy. If it's not player 1's turn,
        #  then it is player 2's turn. If it is player 2's turn, execute player 2's strategy.
        if player_1_turn:
            decks = strategy_player_1(decks)
        else:
            decks = strategy_player_2(decks)

        # Print a message for easy debugging
        print "After Player", "1" if player_1_turn else "2", "'s turn", decks

        # Now that the turn has ended, update the state to reflect the fact that it is
        #  now the opposite player's turn.
        player_1_turn = not player_1_turn

    # If the game halted during player 1's turn, player 1 won. However, player_1_turn will be false because the loop
    #  inverts the player. The same is true of player 2.
    #  In other words, a player whose turn starts when decks = [0, 0] loses because the previous player took the last
    #  card.
    return not player_1_turn


# Test the above functions based on the predetermined results of paper test cases.
def test():
    # Only perfect strategy has been implemented. With perfect strategy, player 2 should always win regardless
    #  of player 1's strategy (good or bad)
    # Test the play_game function by checking that a range of n values return false (representing a player_2 win)

    # Test a game of 1-card piles and perfect strategy
    if play_game(1, strategy_perfect, strategy_perfect):
        print "Error:\tPlayer 1 won game won when it shouldn't have."
    else:
        print "Pass:\tPlayer 2 won a game where n=1"

    # Test a game of 2-card piles and perfect strategy
    if play_game(2, strategy_perfect, strategy_perfect):
        print "Error:\tPlayer 1 won game won when it shouldn't have."
    else:
        print "Pass:\tPlayer 2 won a game where n=2"

    # Test a game of 3-card piles and perfect strategy
    if play_game(3, strategy_perfect, strategy_perfect):
        print "Error:\tPlayer 1 won game won when it shouldn't have."
    else:
        print "Pass:\tPlayer 2 won a game where n=3"

    # Test a game of 746-card piles and perfect strategy
    if play_game(746, strategy_perfect, strategy_perfect):
        print "Error:\tPlayer 1 won game won when it shouldn't have."
    else:
        print "Pass:\tPlayer 2 won a game where n=746"

    # Test a game of 1024-card piles and perfect strategy
    if play_game(1024, strategy_perfect, strategy_perfect):
        print "Error:\tPlayer 1 won game won when it shouldn't have."
    else:
        print "Pass:\tPlayer 2 won a game where n=1024"


# If somebody actually runs this file, call the test() function.
if __name__ == "__main__":
    # Test the algorithm before letting Humans play with it
    print "-"*38+"Test"+"-"*38
    test()
    print "-"*36+"End Test"+"-"*36

    # Let a human play against the machine in a game where n=2000
    player_1_won = play_game(2000, strategy_human, strategy_perfect)

    if player_1_won:
        print "The human beat the machine. This will never happen."
    else:
        print "The machine beat the human. What a surprise."
