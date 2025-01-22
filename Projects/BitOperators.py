n1 = int(input("ENTER NUMBER 1\n"))
n2 = int(input("ENTER NUMBER 2\n"))

if(n1 > 0 and n2 > 0):
    print("\nAND")
    print(n1 & n2)

    print("\nNOT")
    print(~n1, ~n2)

    print("\nOR")
    print(n1 | n2)

    print("\nXOR")
    print(n1 ^ n2)

    print("\nLeft Shift")
    print(n1 << n2)

    print("\nRight Shift")
    print(n1 >> n2)
else:
    print("Ma'am stop trying to break my code please.")
