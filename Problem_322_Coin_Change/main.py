from Solution import Solution

def main():

    # Example 1:
    # Output: 3
    coins = [1,2,5]
    amount = 11

    # Example 2:
    # Output: -1
    # coins = [2]
    # amount = 3

    # Example 3:
    # Output: 0
    # coins = [1]
    # amount = 0

    # Instantiate Solution class
    s = Solution() 

    # Retrieve solution
    answer = s.coinChange(coins,amount)

    print(f"Fewest number of coins to reach the amount of {amount}: {answer}")


if __name__ == "__main__":
	main()