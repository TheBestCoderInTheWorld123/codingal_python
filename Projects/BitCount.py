def bitNumCountHEHE(num):
    count = 0
    temp = num

    while(num):
        count += 1
        num >>= 1
    print(f"There are {count} number of bits in {temp}")

numbah = abs(int(input("Enter number\n")))
bitNumCountHEHE(numbah)
