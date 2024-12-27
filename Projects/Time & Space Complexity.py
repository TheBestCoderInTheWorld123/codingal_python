def fun1(n):
    count = 1
    
    print("\nNumber of iterations in function 1 is", count)
    return n*(n+1)/2

def fun2(n):
    sum = 0
    count = 0
    for i in range(n+1):
        count = count + 1
        sum = sum + i
    
    print("\nNumber of iterations in function 2 is", count)
    return sum

def fun3(n):
    sum = 0
    count = 0
    for i in range(n+1):
        count = count + 1
        for j in range(i):
            sum = sum + 1
            count = count + 1
    print("\nNumber of iterations in function 3 is", count)
    return sum

print("Sum of function 1 is", fun1(5))
print("Sum of function 2 is", fun2(5))
print("Sum of function 3 is", fun3(5))
