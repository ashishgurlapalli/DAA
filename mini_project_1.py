import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range (an integer): "))
            upper_bound = int(input("Enter the upper bound of the range (an integer): "))
            if lower_bound >= upper_bound:
                print("Upper bound must be greater than lower bound. Please try again.")
                continue
            secret_number = random.randint(lower_bound, upper_bound)
            attempts = 0
            print(f"The guessed number is between {lower_bound} and {upper_bound}.")
            while True:
                try:
                    guess = int(input(f"Enter your guess (between {lower_bound} and {upper_bound}): "))
                    attempts += 1
                    if guess < lower_bound or guess > upper_bound:
                        print(f"Please enter a number within the range {lower_bound} and {upper_bound}.")
                        continue
                    if guess < secret_number:
                        print("Too low! Try guessing a higher number.")
                    elif guess > secret_number:
                        print("Too high! Try guessing a lower number.")
                    else:
                        print(f"Congratulations! You guessed the number {secret_number} correctly!")
                        print(f"It took you {attempts} attempts to guess the correct number.")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for playing!")
                break
        except ValueError:
            print("Invalid input. Please enter valid integers for the range.")

if __name__ == "__main__":
    guess_number()
