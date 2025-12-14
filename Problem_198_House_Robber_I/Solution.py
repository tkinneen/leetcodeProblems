# LeetCode Problem 198: House Robber
#
# You are a professional robber planning to rob houses along a street. Each house
#    has a certain amount of money stashed, the only constraint stopping you from 
#    robbing each of them is that adjacent houses have security systems connected 
#    and it will automatically contact the police if two adjacent houses were broken
#    into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return
#    the maximum amount of money you can rob tonight without alerting the police.

from typing import List

class Solution:
    # Top Down, Vanilla Recursive Solution
    # Time: O(2^n) // Space: O(n)d
    def rob(self, nums: List[int]) -> int:
        
        # Get the last array position of all the houses
        n = len(nums) - 1

        # Helper function to calculate the max profit at a particular house from a 
        #    valid string of robberies
        def rob_from(i):

            # Base cases
            if i == 0:
                return nums[0]
            if i == 1:
                # Use the biggest profit from the first two houses
                return max(nums[0], nums[1])

            # Take the biggest bag: The recursion scheme will tell us the max profit
            #    from one and two houses back. Calculate the profit of the current house
            #    and the last valid house (two back), and if it's less than the max profit
            #    of the last house back, then go with that
            return max(nums[i] + rob_from(i - 2), rob_from(i - 1))

        # Kick off recurcion by passing the final index position of the array
        return rob_from(n)
        
    
    # Top Down Dynamic Programming, Memoization
    # Time: O(n) // Space: O(n)
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Define base cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # Instantiate the memoization dictionary and populate it with base cases
        memo = { 0: nums[0], 1: max(nums[0], nums[1]) }

        # Helper function to calculate the max profit from valid robberies
        def rob_from(i):

            if i in memo:
                # No need to recurse further, just return the already-computed value
                return memo[i]
            else:
                # Add this house's max profit calculation to the memo dict. Take the last
                #    house's profit if it's greater, otherwise add the current house's profit
                #    to the max profit from two houses ago
                memo[i] = max(nums[i] + rob_from(i - 2), rob_from(i - 1))
                return memo[i]

        # Kick off recursion at the end of the array
        return rob_from(n - 1)
    

    # Bottom Up Dynamic Programming, Tabulation 
    # Time: O(n) // Space: O(n)
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Define the base cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # Instantiate the tabulation array with the same number of elements as there are houses
        dp = [0] * n

        # Before looping through the array, populate it with our base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Starting at idx 2, calculate the current max value by taking the larger of the current house
        #    plus two houses back, or else the max profit from the previous house
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        # After all calculations are complete, the final index position holds the max profit
        return dp[n - 1]


    # Bottom Up Dynamic Programming, Constant Space Approach
    # Time: O(n) // Space: O(1)
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Handle base cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Initialize the previous and current vars with the base cases
        previous = nums[0]
        current = max(nums[0], nums[1])

        # Loop through the entire array, starting just after the base cases and
        #    using the previous calculated robberies to calculate the optimal 
        #    current robbery
        for i in range(2, n):
            previous, current = current, max(nums[i] + previous, current)
        
        # The final index position will represent the max profit when casing the entire street
        return current