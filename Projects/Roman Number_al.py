romeral = str(input("GIMME ROMERAL:\n"))

roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def romeral_haha(num):
    result = 0
    for i in range(0, len(num) - 1):
        if(roman[num[i]] < roman[num[i + 1]]):
            result -= roman[num[i]]
        else:
            result += roman[num[i]]
    return result + roman[num[-1]]
    
print(romeral_haha(romeral))
