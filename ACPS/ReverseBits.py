def ReverseBits(number):
    result = 0
    while(number):
        result = (result << 1) + (number & 1)
        number >>= 1 
    return result

num = int(input("Enter number\n"))
print(f"Reverse of {num} is", ReverseBits(num))
