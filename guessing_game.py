import random

RESET = "\033[0m"

secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess > secret:
            print(f"\033[36mLess {RESET}\n")
        elif guess < secret:
            print(f"\033[36mMore {RESET}\n")
        else:
            print(f"\n\033[33mYou are right!. The guessed number is {secret} and you got it for {attempts} attempts {RESET}")
            break

    except ValueError:
        print(f"\033[31mType only integer! {RESET}\n")