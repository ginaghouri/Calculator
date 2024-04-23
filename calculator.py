# Task 3: Exception Handling 1
# The code is given below
# When we try to divide a number by 0, it crashes the program and gives ZeroDivisonError
# We want to make sure that when a ZeroDivisionError occurs, the program does not crash
# And it should instead output "You cannot divide numbers by 0".
# So modify or add code to make it display "You cannot divide numbers by 0" in case such an error occurs
# Hint: Use exception handling
# You can look at slides to solve this problem

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
    try: 
        print (int (number1) / int (number2))
    except ZeroDivisionError:
        print("You cannot divide by 0, please enter another number!") #4 spaces added 10