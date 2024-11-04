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
        a = str(input("Retry? y/n"))
    if(a != 'y' OR a != 'Y' OR a = != 'n' OR a != 'N'):
        print("bro-")
    elif(a == 'Y' or a == 'y'):
        acc_num = int(input("Enter your account number: "))
        if(acc_num != accounts['acc_num']):
            print("Invalid Account Number")

    print(f"Account Holder: {accounts[acc_num]['name']}")

# def make_transaction():
open_acc()
view_bal()
