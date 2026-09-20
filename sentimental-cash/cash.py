from cs50 import get_float

def main():
    # Prompt the user for a valid non-negative change amount
    while True:
        dollars = get_float("Change: ")
        if dollars >= 0:
            break

    # Convert dollars to cents to avoid floating-point inaccuracies
    cents = int(dollars * 100)

    # Initialize coin counter
    coins = 0

    # Calculate quarters (25¢)
    coins += cents // 25
    cents %= 25

    # Calculate dimes (10¢)
    coins += cents // 10
    cents %= 10

    # Calculate nickels (5¢)
    coins += cents // 5
    cents %= 5

    # Calculate pennies (1¢)
    coins += cents

    # Print total number of coins
    print(coins)

if __name__ == "__main__":
    main()
