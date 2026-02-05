import random

def get_computer_choice():
    """
    Randomly selects and returns one of the choices:
    rock, paper, or scissors.
    """
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    """
    Asks the player for input until a valid choice is given.
    Uses a while loop to repeat until the condition is met.
    """
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def determine_winner(player, computer):
    """
    Determines the winner of a round.
    Returns 'player', 'computer', or 'tie'.
    Uses if / elif / else logic.
    """
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"


def play_round():
    """
    Plays one round of the game.
    Calls other functions and returns the winner.
    """
    player = get_player_choice()
    computer = get_computer_choice()

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    winner = determine_winner(player, computer)
    return winner


def play_game():
    """
    Manages multiple rounds, keeps score,
    and prints the final result.
    """
    player_score = 0
    computer_score = 0

    rounds = int(input("How many rounds do you want to play? "))

    for i in range(rounds):
        print(f"\n--- Round {i + 1} ---")
        winner = play_round()

        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")

    print("\n--- Final Score ---")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print("You win the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("The game ends in a tie!")



# The main program is clean and only calls one function
play_game()


# -----------------------------
# Reflection
# -----------------------------

# 1. Why did you split it into these specific functions?
# I split the program into functions so that each one
# has a single clear responsibility, such as getting input,
# deciding a winner, or managing the game flow.

# 2. What's one function that took multiple tries to get right?
# The determine_winner() function took multiple tries because
# I had to carefully cover all possible win and loss cases.

# 3. How did using functions make your code better?
# Using functions made the code easier to read, debug,
# and modify compared to writing everything in one block.

# 4. What AI prompt helped you organize your code?
# "Help me split a Rock Paper Scissors game into clean,
# well-documented Python functions."
