# LeetCode Problem 371: Sum Of Two Integers
#
# Given two integers a and b, return the sum of the two integers without
#    using the operators + and -.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time and space complexity are O(1)

        # hexidecimal representation of 32 bits
        shortenBits = 0xFFFFFFFF

        # For positive numbers, loop until the carry is 0
        # Negative numbers can make this loop endlessly, so the shortenBits
        #    value will negate itself once b reaches its 33rd bit:
        #    100000000000000000000000000000000 & 11111111111111111111111111111111
        while b & shortenBits > 0:
            # First calculate whether there is a carry value
            # This compares each bit of a and b using the 'and' operator
            # This will ONLY evaluate to 1 if both bits are 1
            # As long as there is a carry, we will continue to loop
            # All carries must be bit shifted one position to the left
            carry = (a & b) << 1

            # The Xor operator will perform the non-carry addition
            # Xor will evaluate two bits, and return a 1 ONLY if
            #    the bits being evaluarted are different
            a = a ^ b

            # Now set b to the carry value, and next iteration we will
            #    xor the current result of a with the carry. If that results
            #    in a carry, we will loop again until the carry is 0
            b = carry

        # Again, negative values can cause the b carry to shift endlessly
        #    If that happens return a and'ed with bit shortener, otherwise return a
        return (a & shortenBits) if b > 0 else a
