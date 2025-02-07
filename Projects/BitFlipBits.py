def Flips(num1, num2):
    flips = 0
    a = num1
    b = num2

    while(num1 > 0 or num2 < 0):
        temp1 = (num1 & 1)
        temp2 = (num2 & 1)

        if(temp1 != temp2):
            flips += 1

        num1 >>= 1
        num2 >>= 1
    if(flips > 1):
        print(f"{flips} flips are required to make {a} and {b} equal")
    elif(flips == 1):
        print(f"{flips} flip is required to make {a} and {b} equal")
    else:
        print(f"{a} and {b} ARE equal")

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))

Flips(num1, num2)
