# LeetCode Problem 412: Fizz Buzz
#
# Given an integer n, return a string array answer(1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i(as a string) if none of the above conditions are true.

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # Time and space complexity are O(n)

        result = []

        # Start at 1, then check every number up to n
        for current in range(1, n + 1):
            if current % 3 == 0 and current % 5 == 0:
                result.append("FizzBuzz")
            elif current % 3 == 0:
                result.append("Fizz")
            elif current % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(current))

        return result.append(result)
