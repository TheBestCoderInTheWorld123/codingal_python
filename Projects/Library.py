class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}
    
    def DisplayBooks(self):
        print(f"Library OoO's Books:\n{self.name}")
        for book in self.bookList:
            print(book)
    
    def BorrowBook(self, user, book):
        if(book not in self.bookList):
            print("We don't own that book.")
        elif(book not in self.lendDict.keys()):
            self.lendDict.update({book:user})
            print("You may take the book now.")
        else:
            print("Book is already in use")

    def AddBook(self, book):
        if(book in self.bookList):
            print("We already own this book.")
        else:
            self.bookList.append(book)
            print("Book added.")
    
    def ReturnBook(self, book):
        if(book not in self.lendDict.keys() and book not in self.bookList):
            print("We don't own this book.")
        else:
            self.lendDict.pop(book)
            print("Book returned.")

books = Library(["A Good Girl's Guide to Murder", "Little Prince", "Five Feet Apart", "Harry Potter", "Wonderstruck", "Blowing Smoke", "Blue Hair", "Risk"], "OoO")

while(True):
    print("\nWelcome to Library OoO. Enter your choice to continue.")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    print("0. Exit")
    choice = input()
    if(choice not in ['1', '2', '3', '4', '0']):
        print("Enter a valid input.")
    else:
        choice = int(choice)
    
    if(choice == 1):
        books.DisplayBooks()
    
    elif(choice == 2):
        book = input("Enter the name of the book you want to borrow.\n")
        user = input("Enter your name.\n")
        books.BorrowBook(user, book)
    
    elif(choice == 3):
        book = input("Enter the name of the book you want to add.\n")
        books.AddBook(book)
    
    elif(choice == 4):
        book = input("Enter the name of the book you want to return.\n")
        books.ReturnBook(book)
    
    elif(choice == 0):
        exit()

    else:
        print("Enter a valid choice cmon")
