# question 1: Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

number = float(input("Enter your number:"))
square = number ** 2
cube = number ** 3
print("Square of", number, "is:", square)
print("Cube of", number, "is:", cube)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter you first number:"))
num2 = int(input("Enter you second number:"))
if num1 > num2:
    print(num1, "Is Greater than", num2)
elif num1 < num2:
    print(num2, "Is Greater than", num1)
else:
    print(num1,"and", num2, ":Both numbers are equal")



