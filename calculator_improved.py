# Task: Improving the calculator
# The calculator needs more features, currently it only performs addition.
# When we run the program we should see something like this:
# Which operation do you want to perform? (/, -, +, *): *
# Enter the first number: 5
# Enter the second number: 9
# Result: 45

# Another example
# Which operation do you want to perform? (/, -, +, *): /
# Enter the first number: 100
# Enter the second number: 2
# Result: 50

# Some hint steps:
# Take input from the user and ask for an operator +, -, * or / 
# Perform that operation based on the entered operator
# You will have to use if-else conditions to check which operator the user has entered,
# and perform the operation based on that
# rest of the program, it's very similar to the last program

# Write you code here:

number1 = input ('Enter the first number:')
number2 = input ('Enter the second number:')
operation= input ('Which operation do you want to perform?Enter +,-,* or /:')
if operation == "+":
   print (int (number1) + int (number2)) 
elif operation == "-":
   print (int (number1)- int (number2))
elif operation == "*":
   print (int (number1) * int (number2))
elif operation == "/":
   print (int (number1) / int (number2))

   