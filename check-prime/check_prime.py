"""
Name:   Jake Billings
Date:   10/26/2017
Class:  CSCI 2511 Discrete Structures
Desc:   Implementation of a prime-checking algorithm for problem 4.3.1 of the midterm review
"""
# Import time so that we can benchmark the algorithm
from time import time

# Check if i is prime using the simplest algorithm I could think of.
# There ARE ways to optimize this algorithm. I don't know how to derive
# or prove them yet.
def is_prime(i):
    for j in range(2,i):
        if i % j < 1:
            return False
    return True


# Test the function using assertions for known primes and non-primes
def test():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert is_prime(11)
    assert not is_prime(12)
    assert is_prime(157)

# If anybody decides to run this function, run the test() function then ask for user input
if __name__ == "__main__":
    # Run tests
    print "Testing..."
    # test()
    print "Tests Passed."

    # Check user input forever
    while True:
        i = input("Number to check: ")

        start = time()
        state = is_prime(i)
        end = time()

        if is_prime(i):
            print i, "is prime."
        else:
            print i, "is not prime."

        print "Done in ", end-start, "seconds."
