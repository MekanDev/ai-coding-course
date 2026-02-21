from datetime import datetime

# Get today's date
today = datetime.now().strftime("%B %d, %Y")

print("=== Personal Time Capsule 2026 ===")

# Ask questions
name = input("Your full name: ")
age = input("Your current age: ")
favorite_song = input("Your favorite song right now: ")
biggest_goal = input("Your biggest goal for this year: ")
best_friend = input("Your best friend's name: ")
favorite_hobby = input("Your favorite hobby: ")
current_mood = input("How do you feel about your life right now? ")


width = 44  # внутренняя ширина рамки

title = "TIME CAPSULE - 2026"
created_line = f"Created: {today}"


# Create formatted output
content = f"""
{"╔" + "═" * width + "╗"}
║{title:^{width}}║
║{created_line:^{width}}║
{"╚" + "═" * width + "╝"}


Name: {name}
Current Age: {age}

🎵 Favorite Song:
{favorite_song}

🎯 Biggest Goal:
{biggest_goal}

👤 Best Friend:
{best_friend}

🎮 Favorite Hobby:
{favorite_hobby}

💭 Current Mood:
{current_mood}

════════════════════════════════════════════════════
This file was created to remember who I was in 2026.
════════════════════════════════════════════════════
"""

# Save to file
with open("time_capsule_2026.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Time capsule saved successfully!")