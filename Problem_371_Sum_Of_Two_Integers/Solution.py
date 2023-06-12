# LeetCode Problem 371: Sum Of Two Integers
#
# Given two integers a and b, return the sum of the two integers without
#    using the operators + and -.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time and space complexity are O(1)

        # hexidecimal representation of 32 bits
        shortenBits = 0xFFFFFFFF

        print(f"initial input, a: {a}, b: {b}")

        # For positive numbers, loop until the carry is 0
        # Negative numbers can make this loop endlessly, so the shortenBits
        #    value will negate itself once b reaches its 33rd bit:
        #    100000000000000000000000000000000 & 11111111111111111111111111111111
        while b & shortenBits > 0:
            AandShort = a & shortenBits
            BandShort = b & shortenBits

            print(f"a & shortenBits: {AandShort}")
            print(f"bin of a & shortenBits: {bin(AandShort)}")
            print(f"b & shortenBits: {BandShort}")
            print(f"bin of b & shortenBits: {bin(BandShort)}")
            print(f"shortenBits: {shortenBits}")
            print(f"bin of shortenBits: {bin(shortenBits)}")

            #print(f"b & shortenBits (top of loop): {bin(b) & bin(shortenBits)}")            
            # First calculate whether there is a carry value
            # This compares each bit of a and b using the 'and' operator
            # This will ONLY evaluate to 1 if both bits are 1
            # As long as there is a carry, we will continue to loop
            # All carries must be bit shifted one position to the left
            carry = (a & b) << 1
            print(f"carry: {carry}")
            print(f"bin(carry): {bin(carry)}")

            # The Xor operator will perform the non-carry addition
            # Xor will evaluate two bits, and return a 1 ONLY if
            #    the bits being evaluarted are different
            a = a ^ b
            print(f"a: {a}")
            print(f"bin(a): {bin(a)}")


            # Now set b to the carry value, and next iteration we will
            #    xor the current result of a with the carry. If that results
            #    in a carry, we will loop again until the carry is 0
            b = carry
            
            
            print(f"a & shortenBits (bottom of loop): {a & shortenBits}")
            anded = a & shortenBits
            print(f"bin(a & shortenBits): {bin(anded)}")
            print(f"bin(a): {bin(a)}")
            print(f"bin(shortenBits: {bin(shortenBits)}")
            print(f"a & shortenBits (very end): {bin(anded)}, {bin(a)}, {bin(shortenBits)}")
            print("========================")


        # Again, negative values can cause the b carry to shift endlessly
        #    If that happens return a and'ed with bit shortener, otherwise return a
        print(f"a & shortenBits (very end): {a & shortenBits}")
        anded = a & shortenBits
        print(anded)
        print(bin(a))
        print(bin(shortenBits))
        print(f"a & shortenBits (very end): {bin(anded)}, {bin(a)}, {bin(shortenBits)}")

        return (a & shortenBits) if b > 0 else a
