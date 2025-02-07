def divide(deadend, advisor):
    sign = (-1 if((deadend < 0) ^ (advisor < 0)) else 1)

    a = deadend
    b = advisor

    deadend = abs(deadend)
    advisor = abs(advisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if(temp + (advisor << i) <= deadend):
            temp += advisor << i
            quotient |= 1 << i
        if(sign == -1):
            quotient = -quotient

    print(f"{a} divided by {b} is {quotient}")
    
a = int(input("Enter a for a/b\n"))
b = int(input("Enter b for a/b\n"))

divide(a, b)
