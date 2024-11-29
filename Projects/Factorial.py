def factorial(num):
    if(num == 0):
        return 0
    elif(num < 0):
        print("Invalid input")
    elif(num == 1):
        return 1
    else:
        return num * factorial(num - 1)

def sum(num):
    if(num == 0):
        return 0
    elif(num < 0):
        print("Invalid input")
    elif(num == 1):
        return 1
    else:
        return num + sum(num - 1)

print("1. Factorial\n2. Sum")
choice = int(input("1 or 2: "))

if(choice == 1):
    n = int(input("Enter number you want factorial of: "))
    print(factorial(n))
elif(choice == 2):
    m = int(input("Enter number you want sum of: "))
    print(sum(m))
else:
    print("I said 1 or 2??")