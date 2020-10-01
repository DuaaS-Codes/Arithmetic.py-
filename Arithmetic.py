#Author: Duaa
#Date: November 19, 2019
#Arithmetic

int_numberOne = (int)(input("Enter a number: "))
str_operator = (input("Enter an operator: "))
int_numberTwo = (int)(input("Enter a second number: "))

if str_operator == "/" and int_numberOne == 0 or int_numberTwo == 0:
   print("The answer is undefined.")
elif str_operator == "+":
   print("The answer is", int_numberOne + int_numberTwo)
elif str_operator == "-":
   print("The answer is", int_numberOne - int_numberTwo)
elif str_operator == "*":
   print("The answer is", int_numberOne * int_numberTwo)
elif str_operator == "/":
   print("The answer is", int_numberOne // int_numberTwo)
else:
   print("Error: That is not a valid operator. Please try again.")
