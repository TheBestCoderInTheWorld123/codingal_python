def swap1(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print(f"a is {a} and b is {b}")

def swap2(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"a is {a} and b is {b}")

swap1_a = int(input("Enter a:\n"))
swap1_b = int(input("Enter b:\n"))

swap2_a = int(input("Enter a:\n"))
swap2_b = int(input("Enter b:\n"))

swap1(swap1_a, swap1_b)
swap2(swap2_a, swap2_b)
