from math import sqrt

num = int(input("Enter your number:\n"))

if(num > 1):
    for i in range(2, int(sqrt(num)) + 1):
        if(num % i == 0):
            print(f"{num} is not in it's prime")
            break
    else:
        print(f"{num} is in it's prime")
else:
    print("r u okay? stop trying to break my code.")
