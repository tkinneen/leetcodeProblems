# LeetCode Problem 371: Sum Of Two Integers
#
# Given two integers a and b, return the sum of the two integers without
#    using the operators + and -.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Because
        shortenBits = 0xFFFFFFFF

        print(f"b: {b}")
        print(f"bin(b): {bin(b)}")
        print(f"shortenBits: {shortenBits}")
        print(f"bin(shortenBits): {bin(shortenBits)}")
        print(f"b & shortenBits: {b & shortenBits}")
        # print("f{}")

        print(f"0 ^ 0: {0 ^ 0}")
        print(f"0 ^ 1: {0 ^ 1}")
        print(f"1 ^ 0: {1 ^ 0}")
        print(f"1 ^ 1: {1 ^ 1}")

        print(f"0 & 0: {0 & 0}")
        print(f"0 & 1: {0 & 1}")
        print(f"1 & 0: {1 & 0}")
        print(f"1 & 1: {1 & 1}")

        print(">>>>>>>>>>>>>>>")

        #
        while (b & shortenBits) > 0:
            #
            carry = (a & b) << 1

            print(f"a: {a}, bin(a): {bin(a)}")
            print(f"b: {b}, bin(b): {bin(b)}")

            print(f"a & b: {a & b}, bin(a & b): {bin(a & b)}")
            a = a ^ b
            print(f"a ^ b: {a ^ b}, bin(a ^ b): {bin(a ^ b)}")

            b = carry
            print("======")
        return (a & shortenBits) if b > 0 else a
