class Lemurs:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"\nI am a Lemur. My name is {self.name} and I am {self.age} years old.")
    
    def quote(self):
        print("I cannot move it move it!")
    
class Alpaca:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"\nI am an Alpaca. My name is {self.name} and I am {self.age} years old.")
    
    def quote(self):
        print("The alpacalypse is near.")
    
class Capybara:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"\nI am a Capybara. My name is {self.name} and I am {self.age} years old.")
    
    def quote(self):
        print("capybara capybara capybara capybara CAPYBAAAAARAA")

lemur1 = Lemurs("King Julien", 12)
alpaca1 = Alpaca("Fredrico", 5)
capybara1 = Capybara("Slay-bara", 8)

for i in (lemur1, alpaca1, capybara1):
    i.info()
    i.quote()
