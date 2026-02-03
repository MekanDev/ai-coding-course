import random
from datetime import datetime
import os

FILE_NAME = "weekly_goals.txt"

QUOTES = [
    "Small steps every day lead to big results.",
    "Discipline is choosing what you want most over what you want now.",
    "Your future is created by what you do today.",
    "Consistency beats motivation.",
    "Progress, not perfection."
]


def get_goals():
    print("Enter 3–5 goals for this week:\n")
    goals = []
    while len(goals) < 5:
        goal = input(f"Goal {len(goals) + 1}: ").strip()
        if goal:
            goals.append(goal)
        if len(goals) >= 3:
            if input("Add another goal? (y/n): ").lower() != "y":
                break
    return goals


def save_goals(goals):
    quote = random.choice(QUOTES)
    date_str = datetime.now().strftime("%B %d, %Y")

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("        WEEKLY GOALS TRACKER\n")
        f.write("=" * 40 + "\n")
        f.write(f"Week of: {date_str}\n\n")
        f.write(f"💡 Motivation:\n“{quote}”\n\n")
        f.write("Goals:\n")
        for i, goal in enumerate(goals, 1):
            f.write(f"  {i}. [ ] {goal}\n")
        f.write("\nProgress:\n")
        f.write("Completed: 0 / " + str(len(goals)) + "\n")

    print("\nGoals saved successfully.\n")


def load_goals():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return f.readlines()


def update_goal():
    if not os.path.exists(FILE_NAME):
        print("No goals file found.")
        return

    lines = load_goals()

    goals = []
    for line in lines:
        if "[ ]" in line or "[x]" in line:
            goals.append(line)

    print("\nYour goals:\n")
    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal.strip()}")

    choice = input("\nEnter goal number to mark as completed: ")
    if not choice.isdigit():
        return

    index = int(choice) - 1
    if index < 0 or index >= len(goals):
        return

    old = goals[index]
    new = old.replace("[ ]", "[x]")

    updated_lines = []
    completed = 0
    total = 0

    for line in lines:
        if line == old:
            line = new
        if "[x]" in line:
            completed += 1
        if "[ ]" in line or "[x]" in line:
            total += 1
        updated_lines.append(line)

    for i, line in enumerate(updated_lines):
        if line.startswith("Completed:"):
            updated_lines[i] = f"Completed: {completed} / {total}\n"

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("\nGoal marked as completed.\n")


def main():
    print("1. Create new weekly goals")
    print("2. Update goal completion")

    choice = input("\nChoose an option (1/2): ")

    if choice == "1":
        goals = get_goals()
        save_goals(goals)
    elif choice == "2":
        update_goal()


if __name__ == "__main__":
    main()