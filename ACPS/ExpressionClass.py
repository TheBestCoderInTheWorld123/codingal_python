class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sum(self):
        sum = self.num1 + self.num2 + self.num3
        print(f"{self.num1} + {self.num2} + {self.num3} is equal to {sum}")

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))

obj = Expression(num1, num2, num3)
obj.sum()
