# LeetCode Problem 322: Coin Change
#
# You are given an integer array coins representing coins of different denominations
#    and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that 
#    amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.

from typing import List

class Solution:

    # Top-down Dynamic Programming Memoization Solution
    # Time: O(coins * amount) // Space: O(amount)
    # Start at the amount and try to get down to our base case of 0
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Perform a tim sort on coins, O(n log n) worst case 
        coins.sort()

        # Initialize the memoization table, a dictionary that contains the base case
        memo = { 0:0 }

        # Helper funtion: Recurses to the base case, bubling up the smallest number
        #   of coins it takes to make the passed-in amount
        def min_coins(amt):

            # If the amount has been previously calculated in the memo table, just return it
            if amt in memo:
                return memo[amt]
            
            # A calculation for this amound is necessary, so initialize the minimum to infinity
            minimum = float('inf')

            # Loop through each available coin
            for coin in coins:

                # Difference between the amount we're trying to make and the current coin
                # Either we recurse to calculate the minimum at this amount, or it's already been memoized
                difference = amt - coin

                # The coin array is sorted, so when the difference is negative all coins after will 
                #    be even more negative. So we can break from the loop here
                if difference < 0:
                    break

                # If the amount of the current coin plus the min coins at the difference index 
                #    is the lowest we've seen so far, update the minimum variable
                minimum = min(minimum, min_coins(difference) + 1)
            
            # All coins have been tested, so set the memo of the current amount to the 
            #    minimum we found
            memo[amt] = minimum
            
            return minimum
        
        # Kick off recursion on the target amount
        result = min_coins(amount)

        # All calculations are finished, so return the calculaetd amount IF we found a possible solution,
        #    otherwise return -1
        if result < float('inf'):
            return result
        else:
            return -1

    # Bottom Up, Dynamic Programming, Tabulation Solution
    # Time: O(coins * amount) // Space: O(amount)
    # This is the preferable interview solution as it does not use recursion
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Perform timsort, time complexity of O(n log n)
        coins.sort()

        # Create a dp array, initializing each position with a 0. The "+1" is so we
        #    also have a zeroth index for the base case. We will work our way from 1 
        #    to "amount", using calculations from pervious iterations to get the
        #    current iteration's minimum number of possible coins
        dp = [0] * (amount + 1)

        # Since 0 is the base case, loop from 1 to the amount
        for i in range(1, amount + 1):

            # Start each iteration at infinity. If it's not possible to get to the amount
            #    with the provided coins minimum will never be set to lower
            minimum = float('inf')
            
            # Inner loop iterates over all available coins
            for coin in coins:
                
                # Take the current amount at i, subtract the current coin, and the difference
                #    will act as an index in our dp array to the min possible coins at that amount
                difference = i - coin
                
                # The coin array is sorted, so when the difference is negative all coins after will 
                #    be even more negative. So we can break from the loop here
                if difference < 0:
                    break
                
                # Use the difference index in the already-calulated portion of our dp array to get 
                #    the min number of coins less our current coin. If our current minimum is lower
                #    than what we've seen so far, update the minimum value
                minimum = min(minimum, dp[difference] + 1)
            
            # All coins for the current amount have been checked, so set the current index to the minimum we saw
            dp[i] = minimum

        # All calculations are finished, so return the calculaetd amount IF we found a possible solution,
        #    otherwise return -1
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1