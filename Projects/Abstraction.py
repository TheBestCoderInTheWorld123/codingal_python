class Food:
    def recipe(self):
        pass

class Garlic_Pasta(Food):
    def recipe(self):
        print("\nIngredients:\n2 teaspoons olive oil\n4 garlic cloves, minced\n2 tablespoons butter\n3 cups chicken broth, or more as needed\n½ teaspoon ground black pepper\n¼ teaspoon salt\n½ pound spaghetti\n1 cup grated Parmesan cheese\n¾ cup heavy cream\n1 ½ tablespoons dried parsley")
        print("\nDirections:\nStep 1. Gather all ingredients.\nStep 2. Heat olive oil in a medium pan over medium heat. Add garlic and stir until fragrant, 1 to 2 minutes. Add butter and stir constantly until melted.\nStep 3. Pour in 3 cups chicken broth; add pepper and salt. Bring to a boil. Add spaghetti and cook, stirring occasionally, until tender yet firm to the bite, about 12 minutes. Add more chicken broth if pasta starts to stick to the pan.\nStep 4. Add Parmesan cheese, cream, and parsley and mix until thoroughly combined. Serve immediately.")
    
class Fried_Rice(Food):
    def recipe(self):
        print("\nIngredients:\n⅔ cup chopped baby carrots\n½ cup frozen green peas\n2 tablespoons vegetable oil\n1 clove garlic, minced, or to taste (Optional)\n2 large eggs\n3 cups leftover cooked and chilled white rice\n1 tablespoon soy sauce, or more to taste\n2 teaspoons sesame oil, or to taste")
        print("\nDirections:\nStep 1. Assemble ingredients.\nStep 2. Place carrots in a small saucepan and cover with water. Bring to a low boil and cook for 3 to 5 minutes. Stir in peas, then immediately drain in a colander.\nStep 3. Heat a wok over high heat. Pour in vegetable oil, then stir in carrots, peas, and garlic; cook for about 30 seconds. Add eggs; stir quickly to scramble eggs with vegetables.\nStep 4. Stir in cooked rice. Add soy sauce and toss rice to coat. Drizzle with sesame oil and toss again.\nStep 5. Serve hot and enjoy!")
    
class Zaatar_Chicken_Wings(Food):
    def recipe(self):
        print("\nIngredients:\n\nZaatar:\n2 tablespoons dried thyme\n1 1/2 teaspoons marjoram\n1 rounded tablespoon sumac\n1 tablespoon toasted sesame seeds\n1 tablespoon ground cumin\n1 teaspoon freshly ground black pepper\n1/4 teaspoon cayenne pepper\n\nWings:\n3 1/2 pounds whole chicken wings, cut into flat and drum sections\n1 tablespoon kosher salt\n1/2 teaspoon garlic powder\n1 large egg white\n2 tablespoons honey\n1/2 lemon, juiced\n2 tablespoons olive oil\n2 tablespoons chopped parsley (optional)\n2 teaspoons sumac, for dusting (optional)")
        print("\nDirections:\nStep 1. For za'atar, grind thyme with a mortar and pestle, or using a spice grinder. Add marjoram and grind fine; place thyme and marjoram in a small bowl.\nStep 2. Add sumac, sesame seeds, cumin, black pepper, and cayenne, and stir thoroughly. Store in an airtight container until needed.\nStep 3. For wings, cut whole wings into flat and drum sections, and add to a bowl. Add salt and garlic powder, and mix thoroughly. Cover; refrigerate for at least 2 or up to 24 hours.\nStep 4. Preheat the oven to 400 degrees F (200 degrees C). Line a sheet pan with parchment.\nStep 5. Whisk egg white, honey, and lemon juice together in a small bowl until foamy. Pour over wings and stir thoroughly. Add za’atar, and toss until evenly coated. Arrange wings, evenly spaced, on the prepared pan.\nStep 6. Bake in the preheated oven until bottoms of wings start to brown, about 20 minutes. Remove from the oven; turn wings over.\nStep 7. Continue baking until wings are well browned, and meat easily pulls off the bone, 20 to 30 minutes more.\nStep 8. Rest wings for 5 to 10 minutes before serving. Place on a serving tray, drizzle with olive oil, and top with parsley. Sprinkle with additional sumac or za’atar if desired. For a sweeter, stickier version, drizzle with a little more honey.")

gp = Garlic_Pasta()
fr = Fried_Rice()
zcw = Zaatar_Chicken_Wings()

print("What recipe do you want?\n1. Garlic Pasta\n2. Fried Rice\n3. Za'atar Chicken Wings")
ch = int(input())
if(ch == 1):
    print("Garlic Pasta")
    gp.recipe()
elif(ch == 2):
    print("Fried Rice")
    fr.recipe()
elif(ch == 3):
    print("Za'atar Chicken Wings")
    zcw.recipe()
else:
    print("Boiled Water")
    print("take water. boil it. dunk it on your head.")
