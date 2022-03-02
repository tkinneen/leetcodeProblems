# LeetCode Problem 003: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without 
#    repeating characters.

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substringMap = {}
        longestSubstring = 0
        windowEnd = 0

        # Loop through each char in test string
        for i, num in enumerate(s):

            # Starts at current loop index, keeps extending until a repeat char occurs
            windowEnd = i
            mapCount = 0

            # Loop through each string in current window, adding each unique char to map
            while windowEnd < len(s):
                
                # Ensure current char has 0 matches in the map
                mapCount = Counter(substringMap.get(s[windowEnd]))
                if len(mapCount) != 1:
                    current = s[windowEnd]
                    substringMap[current] = current
                    windowEnd += 1
                # As soon as a character in the current window repeats, break out of the interior loop
                else:
                    break

            # If the current map size is longer than the previous longest substring, update the total count
            if (len(substringMap) > longestSubstring):
                longestSubstring = len(substringMap)
            
            # Clear the hash map and reset the end position\
            substringMap.clear()
            windowEnd = 0

        # Return longest string of un-repeated chars
        return longestSubstring
