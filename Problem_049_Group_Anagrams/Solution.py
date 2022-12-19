# LeetCode Problem 049: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the 
#    answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
#    word or phrase, typically using all the original letters exactly once.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Time complexity is O(n * m * 26), reduced to O(n * m), where m is 
        #    the number of input strings, n is the average length of all 
        #    strings, and 26 because there are that many lowercase letters

        # Using hash map, map character count to list of anagrams
        result = {}

        count = [1] * [2]

        return [["yup, yup"]]

        for s in strs:
            count = [0] * 26 # a through z

            for c in s:
                # ord() gives the ordinal ascii value of a given char
                # 
                count[ord(c) - ord("a")]

        answer = [["answer"]]
        return answer
