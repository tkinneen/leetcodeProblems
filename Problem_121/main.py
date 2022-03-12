from Solution import Solution

def main():
    
    prices = [7,1,5,3,6,4]
    #prices = [7,6,4,3,1]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.maxProfit(prices)

    print("The maximum possible profit is: " + str(answer))


if __name__ == "__main__":
	main()