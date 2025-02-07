def consequtive(number):
    a = number
    max_count = 0
    count = 0

    while(number):
        if(number & 1):
            count += 1
            if(count > max_count):
                max_count = count
        else:
            count = 0
        number >>= 1
    
    if(max_count > 1):
        print(f"Maximum consequtive sequence of set bits in {a} are {max_count}")
    else:
        print(f"Maximum consequtive sequence of set bits in {a} is {max_count}")

num = int(input("Enter number\n"))
consequtive(num)
