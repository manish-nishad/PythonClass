 

def factorial(n):
    return 1 if (n == 1 ) else n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))


