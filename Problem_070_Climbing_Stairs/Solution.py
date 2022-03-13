# LeetCode Problem 070: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
#    you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # A recursive, DFS solution would work, but would result in exponential time complexity.
        # Below is a dynamic programming solution in O(n) time and O(1) space complexity.
        # We work the problem backwards, storing the solutions of the previous 2 steps to deduce 
        #    the solution for the next step.  This technique is an example of memoization. 
        
        # Retain the previous 2 steps' solutions
        # The final step has one solution becasue you're already standing on it, any step would overshoot.
        # The penultimate step you can only use one step, as two would overshot. 
        prevStep1, prevStep2 = 1, 1

        # Loop for the total number of steps
        for i in range(n - 1):
            
            # Save the previous step so we can calculate the new value in prevStep1
            tmp = prevStep1
            prevStep1 = prevStep1 + prevStep2
            # Shift prevStep2 to prevStep1's original value
            prevStep2 = tmp
        
        # Return the final number of calculated steps
        return prevStep1