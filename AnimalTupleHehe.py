hehe = ((1, "Siebel", "Whale"), (2, "Sannia", "Butterfly"), (3, "Shayan", "Monkey"), (4, "Maam", "Panda"), (5, "Brocolli", "Angel"))

addictHehe = {}
for item in hehe:
    addictHehe[item[0]] = item[1:]

print(addictHehe)

setHehe = set()
for item in hehe:
    setHehe.add(item[2])

print(setHehe)
