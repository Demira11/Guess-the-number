import random

def guess_number():
    # Generate a random number between 0 and 100
    target_number = random.randint(0, 100)

    while True:
        # Ask the user to guess the number
        user_guess = int(input("Guess a number between 0 and 100!: "))

        # Check if the guess is correct
        if user_guess == target_number:
            print("Winner!")
            play_again = input("Would you like to play again? (y or n) ").lower()
            
            # If the user wants to play again, generate a new random number
            if play_again == 'y':
                target_number = random.randint(0, 100)
            else:
                print("Thanks for playing!")
                break
        else:
            print("Incorrect. Try again.")

# Start the game
guess_number()
