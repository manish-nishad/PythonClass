def addition(a,b):
    return a+b
def divide(a,b):
    if b > 0:
        return a/b
    else:
        return "cannot divide by zero its gives vlaue in infinite"
def multiplication (a,b):
    return a*b
def substraction (a,b):
    return a-b 

def calculator() :
    print("calaculate the number's")
    num1= int (input ("Enter the first number : "))
    num2= int (input("Enter the second number : "))

    print("\nchoose a operation")
    print("1. Addition")
    print("2. divide")
    print("3. multiplication")
    print("4. substraction ")

    choice = int (input("choose or enter the operation's(1/2/3/4)"))
    if choice == 1:
        result = addition (num1, num2)
    elif choice == 2:
        result = divide (num1,num2)
    elif choice == 3:
        result =multiplication (num1,num2)
    elif choice == 4:
        result = substraction (num1, num2) 
    else :
        result ="invalid choice "
    
    print ("result : ", result)

calculator()