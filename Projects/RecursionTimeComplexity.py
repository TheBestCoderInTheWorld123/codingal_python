def OOo(n):
    if(n <= 0):
        print("NO.")
        return
    else:
        print(n)
        OOo(int(n/2))
        OOo(int(n/2))

OOo(1)
OOo(10000)
