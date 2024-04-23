# Task: Creating a simple calculator
# Description: The calculator takes 2 numbers from the user and shows their sum as the output
# Example Program Behaviour:
# Enter the first number: 5
# Enter the second number: 10
# The sum is: 15

# Steps:
# 1. Take an integer input from the user and store it in a variable / container called 'number1'
# 2. Take another integer input from the user and store it in a variable / container called 'number2'
# 3. Add 'number1' and 'number2' together, and store the result in a new variable called 'number3'

# Note: You might need to convert the user input into an integer before storing it, otherwise it will treat it as a string

# Write your code here:

number1 = input ('Enter the first number:')
number2 = input ('Enter the second number:')
number3 = int (number1) + int (number2)
print (number3)