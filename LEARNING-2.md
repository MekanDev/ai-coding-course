# Learning Log - Week goal

## What I Learned
- How to create a weekly goals tracker using Python
- How to store user input (goals) in a list
- How to write and format data into a `.txt` file
- How to use checkboxes (`[ ]`, `[x]`) to track task completion
- How to update an existing file instead of overwriting everything
- How to count completed tasks and show progress
- How to use the `random` module to display motivational quotes
- How to structure a simple Python project with functions

## What I Asked ChatGPT
- How to add random motivational quotes
- How to update goal completion status
- How to improve the appearance of a `.txt` file

# Learning Report – Calculator with Memory

## Project Overview
I built a calculator program that:
- Takes two numbers from the user
- Performs addition, subtraction, multiplication, and division
- Displays results in a formatted way
- Saves calculation history to a file with timestamps

---

## What I Learned

### Working with Numbers
I learned how to:
- Convert input into numbers using `float()`
- Perform basic arithmetic operations
- Format numbers to 2 decimal places using `:.2f`

---

### File Handling (Append Mode)
I learned how to:
- Open a file in append mode using `"a"`
- Add new content without overwriting old data
- Structure saved data clearly with separators

---

### Timestamps
I used:
- `datetime.now()` to get current date and time
- `strftime()` to format timestamps properly

This helped me understand how programs track history.

---

### Error Handling
I handled division by zero safely using an `if` condition.
This prevented runtime errors.

---

## Biggest Challenge
The hardest part was formatting the output neatly and making sure the history file appends correctly instead of overwriting.

---

## Key Takeaway
This project helped me understand:
- Variables and arithmetic operations
- File persistence
- Formatting output professionally
- How real applications save user activity



# Learning Report – Personal Time Capsule 2026

## Project Overview
I built a program that asks questions about my current life and saves the answers into a beautifully formatted text file called `time_capsule_2026.txt`.

---

## What I Learned

### User Input
I learned how to:
- Ask multiple questions using `input()`
- Store answers in variables
- Organize personal data clearly

---

### f-Strings and Formatting
I used f-strings to:
- Insert variables into text
- Create clean, readable sections
- Design borders and structured output

This helped me understand how to format text professionally.

---

### Working with Dates
I used:
- `datetime.now()` to get today’s date
- `strftime()` to format it nicely (e.g., Feb 2, 2026)

This showed me how programs can record when something was created.

---

### File Writing
I learned how to:
- Open a file using `with open()`
- Write formatted text to a file
- Use UTF-8 encoding for special characters (box borders)

---

## Biggest Challenge
The hardest part was aligning the text properly and making the output look clean inside the borders.

---

## Key Takeaway
This project helped me practice:
- Input handling
- File writing
- Text formatting
- Using dates in Python

It made me understand how programs can preserve information for the future.