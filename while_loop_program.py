# Program B: Number Guessing Game
# This program keeps asking the user to guess a number
# until they guess correctly.
# A while loop is used because we don't know
# how many attempts the user will need.

secret_number = 7
guess = None

print("Guess the secret number (between 1 and 10)")

# while loop runs until the correct condition is met
while guess != secret_number:
    guess = int(input("Your guess: "))

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct! You guessed the number.")
