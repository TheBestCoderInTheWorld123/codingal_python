user = {'hello':'helloo', 'hehe':'eheh'}

def acc():
    username = input("Enter Username ")
    if(username in user):
        print("Username already belongs to our land BE MORE CREATIVE")
        return
    
    password = input("Enter Password ")
    if(password in user.values()):
        print("This password already belongs to our land BE MORE CREATIVE")
        return
    
    user[username] = password
    print("Account created. Welcome to our land.")

acc()
print(user)
