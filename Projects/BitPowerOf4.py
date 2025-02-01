def PowerOfFloors(number):
    count = 0

    if(number <= 0):
        print("No breaking my code!")
    if((number & (~(number - 1))) == number):
        while(number > 1):
            number >>= 1
            count += 1
    if(count % 2 == 0):
        return True
    else:
        return False

num = int(input("Enter number\n"))

if(PowerOfFloors(num)):
    print(f"\n{num} has the power of FLOORS!")
else:
    print(f"\n{num} does not have the power of FLOORS womp womp")
