def PowerOfToos(number):
    if(number <= 0):
        print("No breaking my code!")
    if((number & (~(number - 1))) == number):
        return 1
    return 0

num = int(input("Enter number\n"))

if(PowerOfToos(num)):
    print(f"\n{num} has the power of TOOS!")
else:
    print(f"\n{num} does not have the power of TOOS womp womp")
