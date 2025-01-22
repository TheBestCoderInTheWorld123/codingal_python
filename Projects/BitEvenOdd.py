num = int(input("Enter number\n"))

def isEven(num):
    if(abs(num) ^ 1 == abs(num) + 1):
            print(f"{num} is even")
    else:
        print(f"{num} is an odd fella")    

isEven(num)
