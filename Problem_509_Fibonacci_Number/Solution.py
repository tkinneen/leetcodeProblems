# LeetCode Problem 509: Fibonacci Number
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
#    Fibonacci sequence, such that each number is the sum of the two preceding 
#    ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:

    # Bottom Up, Variable Constant Space Solution
    # This is the optimal solution for an interview
    # Time O(n) // Space O(1) (don't have to maintain arrays or recurse)
    def fib(self, n: int) -> int:

        # Define base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Initialize variables 
        previous = 0
        current = 1

        # Since base cases are handled above, begin calculations at 2
        for _ in range(2, n + 1):
            # At each step, the current value is shifted to the previous value, 
            #    then perform current's updated calculation
            previous, current = current, previous + current
        
        # Return the last-calculated value after the loop completes
        return current

    # Memoization Solution
    # Time O(n) // Space O(n)
    """def fib(self, n: int) -> int:
        
        # Create a dictionary, initialized with base case values where we will
        #    cache the calculated result of each function call for fast retrieval
        #    in subsequent calculations
        memo = {0:0, 1:1}

        # We recurse into this helper function twice for each new calculation, but
        #    because we cache calculations, we need to do it significantly less than
        #    a pure recursive solution, which would be to the order of O(2^n)
        def f(x):
            
            # Skip recursion and return and return the pre-calculated value
            if x in memo:
                return memo[x]
            else:
                # Recurse to calculate a new number and set it in our dictionary cache 
                memo[x] = f(x - 1) + f(x - 1)
                return memo[x]
        
        # Kick off recursion
        return f(n)
    
    # Bottom Up, Tabulation Solution: (Basically creating a table, eliminates recursion)
    # Time O(n) // Space O(n); Technically same complexity, but is often considered
    #    superior because it avoids recursion
    def fib(self, n: int) -> int:
        
        # Define base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Generate a tabulation array where we will cache each number's calculation
        # Each number from 0 - n has an index position for its calculation
        dp = [0] * (n + 1)
        
        # Add base casses (for clarity, adding 0 is redundant)
        dp[0] = 0
        dp[1] = 1

        # Start at 2 since the base cases have already been handled above
        for i in range(2, n+ 1):
            # Perform the calculation specified in the problem description, adding
            #    the result to our tabulation array
            dp[i] = dp[i - 2] + dp[i - 1]
        
        # Return the last-performed calculation after the loop exits
        return dp[n]
    """