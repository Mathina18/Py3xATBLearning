num1 = int(input("Enter the value for length1:"))
num2 = int(input("Enter the value for length2:"))
num3 = int(input("Enter the value for length3:"))

if (num1 == num2) and (num2 == num3) and (num3 == num1):
    print("This triangle is equatorial")
elif (num1 == num2) or (num1 == num3) or (num2 == num3):
    print("This triangle is Isosceles")
else:
    print("This triangle is Scalene")