num = int(input("GIMME NUMS(one only)\n"))

digis = len(str(num))
result = 0
temp = num

while(temp > 0):
    digit = temp % 10
    result += digit ** digis
    temp //= 10

if(num == result):
    print(f"{num} has strong arms.")
else:
    print(f"{num} has weak noodle arms.")
