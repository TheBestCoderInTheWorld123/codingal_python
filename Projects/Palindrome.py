num = int(input("Enter the number hehe:\n"))

temp = num
result = 0

while(num > 0):
    digit = num % 10
    result = result * 10 + digit
    num = num // 10

if(temp == result):
    print(f"{temp} does fly plain drones")
else:
    print(f"{temp} does not fly plain drones")
