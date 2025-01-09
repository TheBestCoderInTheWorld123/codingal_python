def sum(n):
    return n*(n + 1)/2

def summarray(a):
    sum = 0
    for i in a:
        sum = sum + 1
    
    return sum

a = [3, 4, 9, 2]
print(summarray(a))

def woah(n):
    if(n <= 0):
        return 0
    return n + woah(n - 1)

print(woah(10))
