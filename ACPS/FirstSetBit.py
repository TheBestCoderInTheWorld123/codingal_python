def rightMostBitOOoOoO(number):
    if(number <= 0):
        print("No breaking my code!")
    
    bit = 1
    while(number & 1 == 0):
        number >>= 1
        bit += 1
    
    print(f"First set bit is at position {bit}")

num = int(input("Enter number\n"))

rightMostBitOOoOoO(num)
