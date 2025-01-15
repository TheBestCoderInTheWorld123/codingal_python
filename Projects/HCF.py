num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if(num1 > num2):
    big_num = num1
    smoll_num = num2
else:
    big_num = num2
    smoll_num = num1

while(smoll_num):
    temp = smoll_num
    smoll_num = big_num % smoll_num
    big_num = temp

print(f"HCF of {num1} and {num2} is", big_num)
