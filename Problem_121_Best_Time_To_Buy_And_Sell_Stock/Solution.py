# LeetCode Problem 121: Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given
#    stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one
#    stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you
#    cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n) - Memory complexity: O(1) (as we're only using pointers)

        # This is called a "two pointer" solution
        leftPtr, rightPtr = 0, 1
        maxProfit = 0

        # Continue looping while rightPtr has not exceeded the list bounds
        while rightPtr < len(prices):
            # Left is "buy" price, right is "sell" price. Sell price needs to be higher then buy.
            if prices[leftPtr] < prices[rightPtr]:
                # Calculate the profit from this transaction
                curProfit = prices[rightPtr] - prices[leftPtr]

                # Update the maxProfit variable if the latest profit exceeds the current max
                maxProfit = max(curProfit, maxProfit)
            else:
                # If the "buy" price is higher than the "sell" price, shift the left pointer to the right's current position
                leftPtr = rightPtr

            # Step the right pointer to the next value regardless
            rightPtr += 1

        # Return the max possible profit, even if it remains at 0
        return maxProfit
