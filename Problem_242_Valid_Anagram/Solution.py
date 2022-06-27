# LeetCode Problem 242: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false 
#    otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
#    word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

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
