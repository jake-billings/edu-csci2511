"""
Name:   Jake Billings
Date:   10/12/2017
Class:  CSCI 2511 Discrete Structures
Desc:   Implementation of brute-force solution to a problem a simple combinatorics problem
Status: Runs on Python on my Mac

How many ways can one pick two adjacent squares of a chessboard?
"""


# Count the number of possible combinations be iterating each grid square left to right
#  top to bottom. If a square is not on an edge, it can be adjacent to any square where coordinates
#  differ by only one. At an edge, it can be adjacent to squares not on that edge. In a corner,
#  it can be adjacent to two squares not outside the board.
#  This function counts all permutations to create a set containing all adjacent squares in both directions.
#  It then removes duplicate adjacency relations.
def count_adjacent_squares_brute_force(width=8, height=8):
    # Store all edges; or adjacency relationships
    pairs = []

    # Declare some variables to make further calculations more clear
    x_min = 0
    y_min = 0

    x_max = width - 1
    y_max = height - 1

    # Generate all adjacency relationships/edges
    for x in range(0, width):
        for y in range(0, height):
            if x > x_min:
                pairs.append(((x-1, y), (x, y)))
            if x < x_max:
                pairs.append(((x+1, y), (x, y)))
            if y > y_min:
                pairs.append(((x, y-1), (x, y)))
            if y < y_max:
                pairs.append(((x, y+1), (x, y)))

    # Establish a variable so we can count how manuy duplicates we have
    #  It turns out that it is equal to the length of pairs after duplicate removal.
    #  Specifically, half of all edges are duplicates.
    count_duplicates = 0

    # Remove all duplicate edges by checking if two edge relationships are have swapped coordinates
    #  If so, they are equivalent and can be removed.
    for pair_a in pairs:
        for pair_b in pairs:
            if pair_a[0] == pair_b[1] and pair_a[1] == pair_b[0]:
                # If the pairs have been duplicated, remove the ladder one
                pairs.remove(pair_b)
                count_duplicates += 1

    return len(pairs)


# Count the number of possible combinations be iterating each grid square left to right
#  top to bottom. If a square is not on an edge, it can be adjacent to any square where coordinates
#  differ by only one. Count the number of squares efficiently by using a derived formula.
def count_adjacent_squares_efficiently(width):
    return width * (width-1) * 2


# Test a few cases to make sure we know our functions work
def test():
    # If you have no squares, you have no adjacency
    assert count_adjacent_squares_brute_force(0,0) == 0
    assert count_adjacent_squares_efficiently(0) == 0

    # If you have one square, you have no adjacency
    assert count_adjacent_squares_brute_force(1,1) == 0
    assert count_adjacent_squares_efficiently(1) == 0

    # If you have four squares, you have four adjacencies
    assert count_adjacent_squares_brute_force(2,2) == 4
    assert count_adjacent_squares_efficiently(2) == 4

    # This is the specific problem from class
    assert count_adjacent_squares_brute_force(8,8) == 112
    assert count_adjacent_squares_efficiently(8) == 112

    # Since we don't know all the values to test, at least check the two functions match for 0 <= n < 20.
    for i in range(0, 20):
        assert count_adjacent_squares_efficiently(i) == count_adjacent_squares_brute_force(i,i)


# If somebody decides to run this file, run test() to validate the code
if __name__ == "__main__":
    # Run tests
    test()

    # Print a message stating all test cases passed
    print "All test cases passed."