# LeetCode Problem 191: Number Of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' 
#    bits it has (also known as the Hamming weight).
#
# Note that in some languages, such as Java, there is no unsigned integer type. 
#    In this case, the input will be given as a signed integer type. It should
#    not affect your implementation, as the integer's internal binary representation 
#    is the same, whether it is signed or unsigned.
#
# In Java, the compiler represents the signed integers using 2's complement notation. 
#    Therefore, in Example 3, the input represents the signed integer. -3.

class Solution:
    def hammingWeightLogicalAnd(self, n: int) -> int:

        # Time complexity of both of these solutions is O(32) as the problem specifies 
        #    we will always use a 32 bit integer. This reduces to O(1), a constant time solution
        # The logical and solution will be insignificantly faster, as it will only loop for as many 
        #    iterations as there are 1 bits
        
        numOfOneBits = 0

        # Loop until 1 bits no longer exist
        while n:
            print(f"n: {bin(n)}")
            print(f"(n - 1): {bin((n - 1))}")
            
            print(f"n before logical and: {n}")

            # This operation takes something like this:
            # 11111111111111111111000000000000
            # which after subtracting 1 becomes this:
            # 11111111111111111110111111111111
            # Because logical & zeros out nonmatching bits, n becomes:
            # 11111111111111111110000000000000, and we do it over and over
            # Using this method, 0 bits in between 1 bits are irrelevant, because 
            #    subrtracting 1 and &'ing them together will eliminate them
            n = n & (n - 1)

            # Each time we perform a subtraction/logical &, we increment the bit count
            numOfOneBits += 1

        return numOfOneBits

    # Modulous solution
    def hammingWeightModulus(self, n: int) -> int:

        numOfOneBits = 0

        # With this method we will have to loop for as long as 1's exist in the integar
        while n:

            # Using modulus operator, we can tell if the least significant bit is a 1, which 
            #    we can use to accumulate our OneBits count
            numOfOneBits += n % 2

            print(f"n: {n}")
            print(f"binary n: {bin(n)}")
            print(f"n % 2: {n % 2}")
            print("======")

            # We then bit shift n by a single bit, then examine the new least significant bit 
            #    until none remain
            n = n >> 1
        
        return numOfOneBits