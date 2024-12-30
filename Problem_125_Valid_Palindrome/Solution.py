# LeetCode Problem 125: Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
#    and removing all non-alphanumeric characters, it reads the same forward and backward. 
#    Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Two-pointer solution: start at each end of the string and walk both towards the center
        left, right = 0, len(s) - 1
        while left < right:
            
            # Move left pointer until alphanumeric or until crossing right
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move right pointer until alphanumeric or until crossing left
            while right > left and not s[right].isalnum():
                right -= 1
            
            # Compare characters (problem specifies case-insensitivity)
            if s[left].lower() != s[right].lower():
                return False
            
            # Each loop iteration, walk the pointers toward each other
            left += 1
            right -= 1
        
        return True