def crypt():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    choice = int(input("1. Encrypt\n2. Decrypt\nEnter 1 or 2: "))

    if(choice == 1):
        ecode = input("Enter code: ")
        ecode = ecode.upper()
        e = int(input("Enter encryption key: "))
        ecreeepat = ""
        for i in ecode:
            ecreeepat += alphabets[alphabets.index(i) + e]

        print(ecreeepat)
    elif(choice == 2):
        dcode = input("Enter code: ")
        dcode = dcode.upper()
        d = int(input("Enter decryption key: "))
        decreeepat = ""
        for i in dcode:
            decreeepat += alphabets[alphabets.index(i) - d]

        print(decreeepat)
    else:
        print("I said 1 or 2 dummy...")

def dyslexia():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    text = input("Enter text: ")
    list1 = ['p', 'b', 'o', 'w', 'u', 'h', 'z', 'i']
    list2 = ['q', 'd', '0', 'm', 'n', 'y', 's', '!']
    empty = ""

    for i in text:
        if(i in list1):
            n = list1.index(i)
            s = list2[n]
        elif(i in list2):
            m = list2.index(i)
            s = list1[m]
        else:
            s = i
        empty += s

    print(empty)

crypt()
dyslexia()