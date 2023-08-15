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
        

        result = 0

        #testInput = 0b00000010100101000001111010011100 # Output:    964176192 (00111001011110000010100101000000)
        #testInput = 0b11111111111111111111111111111101 # Output:   3221225471 (10111111111111111111111111111111)
        
        #testInput = 0b00110000000000000000000000000000 # Output:    964176192 (00111001011110000010100101000000)


        # Time complexity: O()
        # Memory complexity: O()

        # We're working with a 32-bit int, so loop through indexes 0-31
        for i in range(32):
            print(f"i: {i}, 31 - i: {31-i}")
            print(f"n: {n}")

            print(f"n >> i: {n >> i}")
            binary = n >> i
            print(f"n >> i binary: {bin(binary)}")

            print(f"(n >> i) & 1: {(n >> i) & 1}")

            # Shift n by the number of bits of the current loop iteration.
            #    After shifting, we can check if the current (least-significant) 
            #    bit is 0 or 1 by logical and'ing with 1. This will ONLY yeild 1 
            #    if the least-significant bit is also 1
            bit = (n >> i) & 1
            print(f"bit: {bit}")

            # Now that we have the bit value, we need to insert it in its new place 
            #    at the reverse end of the bit array. This is accomplished by 
            #    subtracting the current loop iteration from the total number of 
            #    bits, then shifting the new bit to the left by that number of 
            #    positions, then finally performing a logical or operation on the current number in that position.
            #    Since the result array was initialized to 0, logical or'ing the current bit will yeild taking the current number of bits in the array and subtracting 
            #    the current loop iteration. As the loop starts at 0, this will 
            #    yeild a value 
            result = result | (bit << (31 - i))

            #print(f"bit << (31 - i): {bit << (31 - i)}")
            #print(f"result | (bit << (31 - i)): {result}")
            print(f"result at the bottom of the loop: {result}")
            print(f"binary result at the bottom of the loop: {bin(result)}")

            print(f"+++++++++++++++++++++++++++")


        return result