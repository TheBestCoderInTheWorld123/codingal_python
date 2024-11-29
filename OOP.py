class hoomans:
    is_human =  "yes"

    def __init__(self, name, wrinkle_lvl, is_annoying):
        self.name = name
        self.wrinkle_lvl = wrinkle_lvl
        self.is_annoying = is_annoying
    
    def eheh(self, gross):
        if gross:
            print(self.name, "is gross")
        else:
            print("not gross")

    def hehe(self):
        print(self.name, " is ", self.wrinkle_lvl, " and is annoying? ", self.is_annoying)

hooman1 = hoomans("Bob", 18, "is!")
hooman2 = hoomans("Rob", 16, "no")

hooman1.hehe()
hooman1.eheh(True)
hooman2.hehe()
hooman2.eheh(True)
