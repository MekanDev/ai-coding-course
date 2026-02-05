# Decision Maker: Study Method Selector
# This program helps the user choose a study method
# based on subject, available time, and learning style.

# Ask the user questions
subject = input("What subject are you studying? (math / languages / science): ").lower()
time = input("How much time do you have? (short / medium / long): ").lower()
style = input("What is your learning style? (visual / auditory / practical): ").lower()

print("\nRecommended study method:")

# Main decision logic using if / elif / else
if subject == "math":
    # Math-specific logic
    if time == "short":
        print("- Solve a few key practice problems to warm up.")
    elif time == "medium":
        print("- Review formulas and solve mixed exercises.")
    else:
        print("- Do a full practice set and review mistakes carefully.")

elif subject == "languages":
    # Language-specific logic
    if style == "auditory":
        print("- Listen to podcasts or dialogues and repeat aloud.")
    elif style == "visual":
        print("- Learn vocabulary with flashcards and short texts.")
    else:
        print("- Write sentences and practice speaking or writing.")

else:
    # Science or any other subject
    if time == "long" and style == "visual":
        print("- Watch an educational video and make notes with diagrams.")
    elif time == "short":
        print("- Read a summary and highlight key concepts.")
    else:
        print("- Read the textbook and answer review questions.")