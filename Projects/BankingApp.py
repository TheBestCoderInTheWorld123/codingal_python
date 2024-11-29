import random

accounts = {}

def open_acc():
    name = input("Enter account holder's name: ")
    id_proof = input("Enter ID proof number: ")
    opening_bal = int(input("Enter opening balance: "))
    if(opening_bal < 0):
        print("Opening balance cannot be negative(you r too broke then)")
    acc_num = random.randint(1000000000, 9999999999)

    acc = {'name' : name,
           'acc_num' : acc_num,
           'id_proof' : id_proof,
           'bal' : opening_bal}
    accounts.update({acc_num : acc})
    
    print(f"Account created! Your account number is {acc_num}")

def view_bal():
    acc_num = int(input("Enter your account number: "))
    if(acc_num != accounts['acc_num']):
        print("Invalid Account Number")

    print(f"Account Holder: {accounts[acc_num]['name']}")

def make_transaction():
    acc_num = int(input("Enter your account number: "))
    if(acc_num != accounts['acc_num']):
        print("Invalid Account Number")
    else:
        print("1. Debit\n2. Credit")
        a = int(input("Choose transaction type: "))

        if(a == 1):
            while True:
                amount = int(input("Enter debit amount: "))
                if(amount < 0):
                    print("Amount cannot be negative")
                elif(amount > accounts[acc_num]['bal']):
                    print("Insufficient Balance")
                else:
                    accounts[acc_num]['bal'] -= amount
                    print("Debit succesful")
                    break
        elif(a == 2):
            while True:
                amount = int(input("Enter credit amount: "))
                if(amount < 0):
                    print("Amount cannot be negative")
                else:
                    accounts[acc_num]['bal'] -= amount
                    print("Credit succesful")
                    break
def update_acc():
    acc_num = int(input("Enter your account number: "))
    if(acc_num != accounts['acc_num']):
        print("Invalid Account Number")
    else:
        print("1. Update account holder name\n2.Delete account")
        a = int(input("Choose option: "))

        if(a == 1):
            while True:
                print(f"Current account name: {accounts[acc_num]['name']}")
                b = input("Are you sure you want to change your account holder name? y/n: ")
                if(b == 'n'):
                    break
                else:
                    new_name = input("Enter new account holder name: ")
                    accounts['bal'] = new_name
open_acc()
view_bal()