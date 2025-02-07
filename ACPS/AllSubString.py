import math

def SubString(set, size):
    PowerSetSize = (int) (math.pow(2, size))
    outer = 0
    inner = 0

    for outer in range(0, PowerSetSize):
        for inner in range(0, size):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")

hehe = input("Enter string\n")
SubString(hehe, len(hehe))
