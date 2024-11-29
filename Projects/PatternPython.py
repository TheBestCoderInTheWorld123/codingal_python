at = int(input("Give number of rows"))
a = int(at/2)
# alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(" ", end = "")
for i in range(0, a):
    for l in range(a - i + 1, 0, -1):
        print(" ", end = "")
        if(l == 1):
          print("x", end = " ")
    for m in range(-1, i - 1):
        print(" ", end = " ")
        if(m == i - 2):
            print("x", end = " ")
    print()

for i in range(0, a + 1):
    for l in range(0, i + 1):
        print(" ", end = "")
        if(l == i):
          print("x", end = " ")
    for m in range(a - i, 0, -1):
        print(" ", end = " ")
        if(m == 1):
            print("x", end = " ")
    print()