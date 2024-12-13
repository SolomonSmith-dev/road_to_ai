import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Game loop
while True:
    try:
        # Get the user's guess
        guess = int(input("Guess a number between 1 and 10: "))
        
        # Check if the guess is within the valid range
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10!")
            continue  # Skip the rest of the loop and ask the user to guess again
        
        # Provide feedback based on the guess
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
            break  # Exit the loop when the correct number is guessed
    except ValueError:
        # If the user enters a non-integer, this block will run
        print("Invalid input! Please enter a number between 1 and 10.")
    continue  # Skip the rest of the loop and ask the user to guess again