# LeetCode Problem 190: Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
# In some languages, such as Java, there is no unsigned integer type. In this case, 
#    both input and output will be given as a signed integer type. They should not 
#    affect your implementation, as the integer's internal binary representation is 
#    the same, whether it is signed or unsigned.
#
# In Java, the compiler represents the signed integers using 2's complement notation. 
#    Therefore, in Example 2 above, the input represents the signed integer -3 and 
#    the output represents the signed integer -1073741825.

class Solution:
    def reverseBits(self, n: int) -> int:

        # Initialize the result to 0; we can still shift bits to the left
        result = 0

        # Time complexity: O(1) (un-amortized: O(32) // Memory complexity: O(1)

        # Loop through every bit in n, one bit at a time
        for i in range(32):
            
            # Each loop iteration we shift n by our current range value, then check 
            #    the least-significant bit by logical &'ing with the bitmask of 0001. 
            #    This will yeild a 1 ONLY if the least-signficant bit is also a 1 
            bit = (n >> i) & 1

            # We now have our current bit value and need to insert it in its new 
            #    place at the reverse end of the bit array. This is accomplished by 
            #    subtracting the current loop iteration from the total number of 
            #    bits, then shifting the new bit to the left by that number of 
            #    positions. Finally, perform a logical or operation on the current
            #    state of result. The or will ONLY yeild a 0 in the result if the 
            #    bit value is 0, which is exactly what we want: to update our 0-initialized 
            #    array with 1 if the bit value is 1  
            result = result | (bit << (31 - i))

        return result