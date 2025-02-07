import math

def printPowerSet(set, size):
    PowerSetSize = (int) (math.pow(2, size))
    outer = 0
    inner = 0

    for outer in range(0, PowerSetSize):
        for inner in range(0, size):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")

size = int(input("Enter array size\n"))
set = []
for i in range(0, size):
    num = int(input("Enter element\n"))
    set.append(num)

printPowerSet(set, len(set))
