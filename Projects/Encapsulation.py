class Computer:
    def __init__(self):
        self.__maxPrice = 900
    
    def sell(self):
        print("\nSelling Price: {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price
    
c = Computer()
c.sell()

c.__maxPrice = 1000
c.sell()

c.setMaxPrice(2000)
c.sell()
