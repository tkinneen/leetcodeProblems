# LeetCode Problem 242: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false 
#    otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
#    word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Time:  O(2n) -> O(n) as we loop through every character in both arrays
        # Space: O(k), where k is the number of chars in the input. But if we're assuming a 26 char set, it's O(1)

        # If the lengths are different we're already done
        if len(s) != len(t):
            return False

        # This hash map will keep a count of each unique char in our first string
        count = {}

        # Fill the map with the first input string
        for char in s:
            # The get() function will default a value to 0 if it doesn't exist in the map yet
            count[char] = count.get(char, 0) + 1

        # Loop through each char in the second string
        for char in t:
            # If we find a char that doesn't exist, the strings aren't anagrams
            # Also if we find a character and its count is 0, the strings don't match and aren't anagrams
            if char not in count or count[char] == 0:
                return False
            # For each maching character, decrement the count
            count[char] -= 1

        # If we haven't returned above, the two strings are valid anagrams
        return True

    # This is the original, inferior NeetCode implementation
    # The memory complexity would be double becasue we build a hash map for each
    #    string and then compare them
    """def isAnagram(self, s: str, t: str) -> bool:

        # It's automatically not an anagram if string lengths are different
        if len(s) != len(t):
            return False
        
        # We will pack each string into its own hash map, then compare
        sHash, tHash = {}, {}

        # Since we already established strings are the same length, we can pack both maps in one loop
        for i in s:
            # Each character acts as key, and each time that key appears its value count gets incremented 
            # The dictionary 'get' function allows us to initialize a value and not crash if key does not yet exist
            sHash[i] = sHash.get(i, 0) + 1
            tHash[i] = tHash.get(i, 0) + 1
        
        # Check the hashes against each other to know if the letter counts are identical
        return True if tHash == sHash else False
    """
