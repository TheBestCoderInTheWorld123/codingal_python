binary = input("Enter your binary number\n")
decimal = 0
len = len(binary)

for i in range(len):
    digit = int(binary[i])
    num = len - i - 1
    decimal += digit * (2 ** num)

print(f"Decimal of {binary} is", decimal)
