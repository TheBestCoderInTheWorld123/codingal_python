def PowerOfATE(number):
    count = 0

    if(number <= 0):
        print("No breaking my code!")
        return False
    if((number & (~(number - 1))) == number):
        while(number > 1):
            number >>= 1
            count += 1
    if(count % 3 == 0 and count > 0):
        return True
    else:
        return False

num = int(input("Enter number\n"))

if(PowerOfATE(num)):
    print(f"\n{num} ATE!!")
else:
    print(f"\n{num} did not eat...")
