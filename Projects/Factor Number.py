num = int(input("GIMME NUMS(one only)\n"))
if(num <= 0):
    print("GET OUT OF HERE PLEASE!!!")
else:
    print(f"Factors of {num} are:")
    for i in range(1, num + 1):
        if(num % i == 0):
            print(i)
