# Decision Maker — Study Method Selector

## 📌 Project Description
This Python program helps users decide **how to study effectively** based on their answers to several questions.  
It uses `if`, `elif`, and `else` statements to analyze user input and give a personalized study recommendation.


## ❓ What does your program decide?
The program decides **which study method is best** for the user by asking:
- What subject they are studying
- How much time they have
- What learning style they prefer

Based on these answers, it recommends an appropriate way to study.


## 🔍 What’s one interesting if/elif/else you used?
One interesting condition checks **two factors at the same time**:

```python
if time == "long" and style == "visual":




# Program A: Multiplication Table Generator
This program prints the multiplication table "for" a given number. A for loop is used because we know in advance how many times the code should repeat (from 1 to 10).

# Program B: Number Guessing Game
This program keeps asking the user to guess a number until they guess correctly.A "while" loop is used because we dont know how many attempts the user will need.

# Reflection:

## 1. When is a for loop better than a while loop?
A for loop is better when you know exactly how many times the loop should run, such as counting or iterating over a range.

## 2. What's one bug you ran into and how did you fix it?
A common bug was forgetting to update the variable inside the while loop, which caused an infinite loop.
I fixed it by making sure the user's guess was updated every iteration.




# Function Builder

## Reflection

### 1. Why did you split it into these specific functions?
- I split the program into functions so that each one has a single clear responsibility, such as getting input, deciding a winner, or managing the game flow.

### 2. What's one function that took multiple tries to get right?
- The determine_winner() function took multiple tries because I had to carefully cover all possible win and loss cases.

### 3. How did using functions make your code better?
- Using functions made the code easier to read, debug, and modify compared to writing everything in one block.

### 4. What AI prompt helped you organize your code?
- "Help me split a Rock Paper Scissors game into clean, well-documented Python functions."