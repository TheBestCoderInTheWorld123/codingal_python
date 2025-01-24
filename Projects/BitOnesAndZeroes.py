def bitNum(n):
    ones = 0
    zeroes = 0

    while(n):
        if(n & 1 == 1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    
    print(f"\nOnes: {ones}\nZeroes: {zeroes}")

num = int(input("Enter numberino\n"))
bitNum(num)
