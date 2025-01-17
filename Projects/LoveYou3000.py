def palindrome(num):
    temp = num
    result = 0

    while(num > 0):
        digit = num % 10
        result = result * 10 + digit
        num = num // 10

    if(temp == result):
        print(temp)

def sieve(num):
    prime = [True for i in range(num + 1)]

    p = 2
    while(p * p <= num):
        if(prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        
        p += 1
    
    for p in range(2, num + 1):
        if(prime[p]):
            palindrome(p)

num = int(input("Enter number:\n"))
print(f"\nAll palindrome prime numbers till {num}")
print("--------------------------------")
sieve(num)
