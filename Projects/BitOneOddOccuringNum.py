def OddOccuring(arr):
    res = 0

    for e in arr:
        res = res ^ e
    return res

arr = []
n = int(input("Enter number of array elements\n"))

while(n):
    num = int(input("Enter number\n"))
    arr.append(num)
    n -= 1

print("\nOdd occuring number is", OddOccuring(arr))
