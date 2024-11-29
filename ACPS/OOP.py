class robot:
    is_human =  "no"

    def __init__(self, name, development_lvl):
        self.name = name
        self.development_lvl = development_lvl
    
    def language(self):
        a = int(input("What language do you yap in?\n1. English\n2. Urdu\n3. Yapperish\n"))
        if(a == 1):
            print("Hi! my name is", self.name, "and it took", self.development_lvl, "years to make me hehe")
        if(a == 2):
            print("You should learn english weirdo BUT \nmera naam", self.name, "hai aur mujhe bananay mein", self.development_lvl, "saal lagay")
        if(a == 3):
            print("You should learn english weirdo BUT\n efi uahdw si", self.name, "ans iwhd fneu", self.development_lvl, "hwjad ot akfueje em eheh")

    def hehe(self):
        print(self.name, " is ", self.development_lvl, "years old")

woah = robot("Waow", 8)
woah.language()