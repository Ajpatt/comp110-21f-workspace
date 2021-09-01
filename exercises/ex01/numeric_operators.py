"""Numeric operators."""
__author__ = "730388679"
num1: int = int(input("Pick an integer: "))
num2: int = int(input("Pick an integer: "))
answer = num1 ** num2
answer2 = num1 / num2
answer3 = num1 // num2
answer4 = num1 % num2
print("Left-hand side: " + str(num1))
print("Right-hand side: " + str(num2))
print(str(num1) + " ** " + str(num2) + " is " + str(answer))
print(str(num1) + " / " + str(num2) + " is " + str(answer2))
print(str(num1) + " // " + str(num2) + " is " + str(answer3))
print(str(num1) + " % " + str(num2) + " is " + str(answer4))