# LeetCode Problem 049: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the
#    answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different
#    word or phrase, typically using all the original letters exactly once.

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Time complexity is O(n * m * 26), reduced to O(m * n), where m is
        #    the number of input strings, n is the average length of all
        #    strings, and 26 because there are that many lowercase letters

        # Use hash map to group anagram strings, using individual char counts as keys
        # Use a defaultdict to prevent KeyError when trying to get an item with a
        #    key that is not curerntly in the dictionary
        result = defaultdict(list)

        # Loop through each string, each time creating a count list with 26 elements,
        #    0-25, corresponding to a-z
        for s in strs:

            # This multiplication fills the list with 26 0's
            count = [0] * 26  # a through z

            # Loop through each character in the current string, using the ordinal
            #    ascii value as the array position and keeping a running count of
            #    each letter
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Because lists can't be used as map keys, convert list to (immutable)
            #    tuple and append the current string
            result[tuple(count)].append(s)

        return result.values()