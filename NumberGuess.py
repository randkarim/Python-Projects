import random

def generate_number(min_val, max_val):
    return random.randint(min_val, max_val)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = generate_number(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts} of {max_attempts}")
        
        guess = get_user_guess()
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            return

    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")

def main():
    play_game()
    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            play_game()
        elif play_again == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
