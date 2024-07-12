n = int(input("Enter the number:"))
a = 0
b = 1
for i in range(0, n):
    if (i<=0):
        fib=i
    else:
        fib = a + b
        a = b
        b = fib
        print("Fibonacci of n is :",fib)
