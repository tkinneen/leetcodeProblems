from Solution import Solution

def main():
    
    # 
    testInput1 = [1,1,2]
    testInput2 = [0,0,1,1,1,2,2,3,3,4]

    # Instantiate Solution class
    s = Solution()

    # Run the Solution method on all test cases
    answer = s.removeDuplicates(testInput2)

    print("Answer: " + str(answer))

if __name__ == "__main__":
        main()