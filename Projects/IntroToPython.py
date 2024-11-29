at = int(input("Give number of rows"))
a = int(at/2)
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(0, a):
    count = alphabets[i]
    # for loop for spaces
    for l in range(a - i, 0, -1):
        print(" ", end = "") 
    for j in range(0, i + 1):
        print(count, end = " ")
    print()

for i in range(a, at + 1):
    count = alphabets[i]
    # for loop for spaces
    for l in range(0, i - a + 1):
        print(" ", end = "") 
    for j in range(at - i, 0, -1):
        print(count, end = " ")
    print()