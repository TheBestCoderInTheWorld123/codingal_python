def Constant(n, m):
    count = 1
    pdct = n*m

    print("\nTime complexity is Constant and the number of iterations are", count)
    print(f"Product of {n} and {m} is {pdct}")

def On(n, m):
    count = 0
    pdct = 0

    for i in range(1,m+1):
        count += 1
        pdct += n
    
    print("\nTime complexity is O(n) and the number of iterations are", count)
    print(f"Product of {n} and {m} is {pdct}")

def On2(n, m):
    count = 0
    pdct = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            count += 1
            pdct += 1

    print("\nTime complexity is O(n^2) and the number of iterations are", count)
    print(f"Product of {n} and {m} is {pdct}")

Constant(3, 100)
On(3, 100)
On2(3, 100)
