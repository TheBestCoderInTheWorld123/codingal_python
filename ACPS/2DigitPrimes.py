from math import sqrt

print("2 digit numbers that are in their prime:")
for l in range(10, 100):
    for i in range(2, int(sqrt(l)) + 1):
        if(l % i == 0):
            break
    else:
        print(l)
