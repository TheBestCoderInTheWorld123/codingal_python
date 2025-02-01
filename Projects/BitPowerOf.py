def Powa(x, y):
    result = 1

    while(y > 0):
        if(y % 2 == 0):
            x *= x
            y >>= 1
        else:
            result *= x
            y -= 1
    return result

num1 = int(input("Enter x for x^y\n"))
num2 = int(input("Enter y for x^y\n"))

print(f"\n{num1} after harnessing the power of {num2} is", Powa(num1, num2))
