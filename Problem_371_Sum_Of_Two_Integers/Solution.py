# LeetCode Problem 371: Sum Of Two Integers
#
# Given two integers a and b, return the sum of the two integers without
#    using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # Time and space complexity are O(1)

        # Since the two's complement representation of -1 in binary is a 
        #    large environment-dependent collection of 1 bits, we can 
        #    use a bitmask and the & operator to "chop off" bits past the
        #    size specified in the problem description.
        shortenBitsMask = 0xFFFFFFFF # Hex representation of 32 bits

        # Loop until there is no longer a carry
        # For certain numbers, when the 33rd bit is reached, this will become 0:
        #    100000000000000000000000000000000 & 011111111111111111111111111111111
        while b & shortenBitsMask > 0:

            # Calculate whether there's a carry value
            # The & operator compares each bit of a and b one at a time
            # This will ONLY evaluate to 1 if both bits are 1
            # All carries must be bit-shifted one position to the left
            carry = (a & b) << 1

            # The Xor operator will perform the non-carry addition
            # Xor will evaluate two bits, returning a 1 ONLY if
            #    the bits being evaluarted are different
            a = a ^ b

            # We've performed both the carry and additon operations. Now set b 
            #    to the carry value and we will loop again. If the carry is nonzero,  
            #    perform the exact same operations on the carry bit sequence
            #    and the addition bit sequence from the last iteration. This may
            #    also result in a carry, so continue to loop until the carry is 0
            b = carry

        # We've exited the loop, meaning the carry is 0 once it's been shortened.
        #    We can return a if b is 0, but if it's greater than 0 we need to first
        #    use the bitshortener on a before returning
        return (a & shortenBitsMask) if b > 0 else a
