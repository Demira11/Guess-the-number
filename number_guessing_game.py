import random

def guess_number():
    
    target_number = random.randint(0, 100)

    while True:
        
        user_guess = int(input("Guess a number between 0 and 100!: "))

        
        if user_guess == target_number:
            print("Winner!")
            play_again = input("Would you like to play again? (y or n) ").lower()
            
            
            if play_again == 'y':
                target_number = random.randint(0, 100)
            else:
                print("Thanks for playing!")
                break
        else:
            print("Incorrect. Try again.")


guess_number()
