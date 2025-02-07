def fibonacci(number):
    fib = [0, 1]

    for i in range(2, number):
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)
    
    for i in fib:
        print(i)

num = int(input("Enter num\n"))
if(num <= 0):
    print("NO BREAKING MY CODE!!")
else:
    print("Fibonacci Sequence:\n", fibonacci(num))
