import random

from art import logo

print(logo +
"Welcome to the Number Guessing Game!\n"
"I'm thinking of a number between 1 and 100."
)

valid_difficulties = ["easy", "hard"]

difficulty = ""
while difficulty not in valid_difficulties:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty not in valid_difficulties:
        print("Invalid choice. Please type 'easy' or 'hard'.")

attempts = 5
if difficulty == "easy":
    attempts = 10

print(f"You chose {difficulty} mode! Let the game begin!")
print(f"You have {attempts} attempts remaining to guess the number.")

number_to_guess = random.randint(1,100)

while attempts > 0:
    guess = int(input("Make a guess:"))
    if guess > number_to_guess:
        print("Too high.")
    elif guess < number_to_guess:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number_to_guess}")
        break

    attempts -= 1
    if attempts > 0:
        print(f"Guess again.\n"
              f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You've run out of guesses. The number was {number_to_guess}.")