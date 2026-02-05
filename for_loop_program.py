# Program A: Multiplication Table Generator
# This program prints the multiplication table for a given number.
# A for loop is used because we know in advance
# how many times the code should repeat (from 1 to 10).

number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table for {number}:")

# for loop is best here because the range is fixed
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
