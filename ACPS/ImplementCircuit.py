a = int(input("Enter value of A\n"))
b = int(input("Enter value of B\n"))
c = int(input("Enter value of C\n"))

first_q_input = a & b

b_or_c = b | c
b_and_c = b & c

second_q_input = b_or_c & b_and_c

q = first_q_input | second_q_input

print(f"\nA: {a}\nB: {b}\nC: {c}\n\nQ: {q}")
