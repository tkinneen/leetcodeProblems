from Solution import Solution

def main():
    
    testInput1 = [7,1,5,3,6,4]
    testInput2 = [1,2,3,4,5]
    testInput3 = [7,6,4,3,1]

    # Instantiate Solution class
    s = Solution()

    # Run the Solution method on all test cases
    answer = s.maxProfit(testInput1)

    print("Answer: " + str(answer))

if __name__ == "__main__":
        main()