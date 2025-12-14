# LeetCode Problem 070: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
#    you climb to the top?

class Solution:

    # Bottom Up Constant Space Approach - Best Answer for Interviews
    # Time: O(n) // Space: O(1) 
    # Still loop through and calculate every step, but just keep variables
    #    that track the last two numbers since there are only two possible
    #    choices at any given step
    def climbStairs(self, n: int) -> int:
        
        # Define base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # These variables will allow us to leverage earlier calculations when
        #    performing the current calculation
        previous, current = 1, 2

        # Start directly after our base cases, working sequentially up to n, 
        #    caching only the last two steps and using them to calculate the
        #    solution for the current step
        for _ in range(2, n):
            # This works because when python handles multi-assignment, it caches
            #    the values in a tuple so they don't get overwritten
            previous, current = current, previous + current
        
        return current


    """
    # Bottom Up Dynamic Programming Approach - Tabulation
    # Time: O(n) // Space: O(n) 
    # Loop eliminates the recursive call stack
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Create an array with a length of the total number of stairs
        dp = [0] * n

        # Set the first two elements to our base cases
        dp[0] = 1
        dp[1] = 2

        # Starting at the second element, loop through the entire range of stairs
        # Calculate each step and add it to the tabulation array, using previous 
        #   calculations for the current value
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the value of the final step in the array
        return dp[n-1]


    # Top-down recursive solution with memoization
    # Time: O(n) // Space: O(n) 
    # Recursion is still used, but work is no longer repeated, saving significant time
    # , but still less optimal than a constant space two-variable solution
    def climbStairs(self, n: int) -> int:

        # Initialize the memo map, to which the base cases are added
        memo = {1:1, 2:2}

        #
        def f(n):

            # Check the memo map, and if we've already calculated this step return the cached result
            if n in memo:
                return memo[n]
            else:
                # recurse into the helper function
                memo[n] = f(n - 1) + f(n - 2)
                return memo[n]
        return f(n)
    
    # Top-down recursive solution
    # Time: O(2^n) // Space: O(n) 
    # NOT optimal: each call recurses into 2 sub-calls, so exponential time complexity and much repeated work
    def climbStairs(self, n: int) -> int:
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Because of the constraints of leg length two steps at a time is the maximum number you can take from any step. the sum of all
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


    def climbStairs(self, n: int) -> int:
        # Original NeetCode solution
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
        return prevStep
    """