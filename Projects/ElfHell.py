counter = 0
def elfHell(n):
    global counter
    if(n > 1):
        counter += 1
        if(n % 2 == 0):
            n = int(n/2)
            elfHell(n)
            elfHell(n)
        else:
            n = int((n + 1)/2)
            elfHell(n - 1)
            elfHell(n)
    return counter

gifts = int(input("How many gifts do you have? "))
print(f"Number of elves needed to distribute {gifts} gifts are {elfHell(gifts)}")