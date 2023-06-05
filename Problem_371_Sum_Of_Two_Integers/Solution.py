# LeetCode Problem 371: Sum Of Two Integers
#
# Given two integers a and b, return the sum of the two integers without
#    using the operators + and -.

#  This test shows how many more bits python uses to store integers than other languages
# import sys
# print(f"0: {sys.getsizeof(0)}, bits: {sys.getsizeof(0) * 8}") # 0: 24, bits: 192
# print(f"1: {sys.getsizeof(1)}, bits: {sys.getsizeof(1) * 8}") # 1: 28, bits: 224
# print(f"-1: {sys.getsizeof(-1)}, bits: {sys.getsizeof(-1) * 8}") # -1: 28, bits: 224
# print(f"0xFFFFFFFF: {sys.getsizeof(shortenBits)}, bits: {sys.getsizeof(shortenBits) * 8}") # 0xFFFFFFFF: 32, bits: 256


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time and space complexity are O(1)

        # 32 bit hexidecimal representation
        shortenBits = 0xFFFFFFFF

        print(f"a: {a}, b: {b}")
        print(
            f"bin(a): {bin(a)}, bin(b): {bin(b)}, bin(shortenBits): {bin(shortenBits)}"
        )

        # Repeatedly loop through the
        # Each time through we'll set the carry (if there is one) to the b value
        # And operator will check for a carry value, as it will only be true if there are two 1's
        # We will have to bit shift

        #
        while b & shortenBits > 0:
            # First calculate whether there is a carry value
            # This compares each bit of a and b with the 'and' operator
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

            print(f"========")
            print(f"a: {a}, b: {b}")
            print(
                f"bin(a): {bin(a)}, bin(b): {bin(b)}, bin(shortenBits): {bin(shortenBits)}"
            )
            print(f"a & shortenBits: {a & shortenBits}")
            print(f"b & shortenBits: {b & shortenBits}")

        print(f"FINAL a: {a}, b: {b}")
        print(f"a & shortenBits: {a & shortenBits}")

        #
        return (a & shortenBits) if b > 0 else a
