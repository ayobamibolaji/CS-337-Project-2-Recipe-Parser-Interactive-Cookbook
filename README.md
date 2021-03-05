# CS 337 Project 2: Recipe Parser and Transformer
## Installation:
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
pip install -r requirements.txt
```
## Run code:
```
python main.py custom
```
This allows you to input a recipe url and a transformation.
An example is below:
```
python main.py custom
https://www.allrecipes.com/recipe/268026/instant-pot-corned-beef/
Welcome. Please enter an AllRecipes url for us to parse.
Got it! Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
1
Name: Instant Pot® Corned Beef

Ingredients:
Name: water	Quantity: 2.0	Measurement: cups
Name: fluid ounce	Quantity: 1.0	Measurement: can
Name: garlic	Quantity: 4.0	Measurement: cloves	Preparation:minced
Name: beef brisket	Quantity: 1.0	Measurement: corned

Steps:
Combine water, beer, and garlic in a multi-functional pressure cooker (such as Instant Pot&reg;)
Place trivet inside
Place brisket on the trivet and sprinkle spice packet on top
Close and lock the lid
Select high pressure according to manufacturer's instructions; set timer for 90 minutes
Allow 10 to 15 minutes for pressure to build
Release pressure carefully using the quick-release method according to manufacturer's instructions, about 5 minutes
Unlock and remove the lid
Transfer brisket to a baking sheet, cover with aluminum foil, and let rest for 15 minutes

Methods:
Combine, Place trivet, Place brisket, Close, Select, Allow, Release, Unlock, Transfer

Tools:
```
You can also run main without an argument to run 50 sample recipes.
You can also run main with the url as the argument. An example is below:
```
python main.py https://www.allrecipes.com/recipe/261472/easy-maple-bacon-monkey-bread/
We received your recipe!
Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
2) Double the quantity
3) Halve the quantity
4) Make it healthier
4
Name: Modified Easy Maple Bacon Monkey Bread

Ingredients:
Name: cooking spray	Quantity: None	Measurement: spray
Name: Splenda	Quantity: 0.375	Measurement: cup	Descriptors: white
Name: pudding mix	Quantity: 2.0	Measurement: tablespoons	Descriptors: caramel, instant	Preparation:uncooked
Name: ground cinnamon	Quantity: 2.0	Measurement: teaspoons
Name: biscuit dough	Quantity: 2.0	Measurement: cans	Preparation:refrigerated, separated
Name: bacon strips	Quantity: 12.0	Measurement: slices	Preparation:cooked
Name: butter	Quantity: 0.5	Measurement: cup
Name: Splenda	Quantity: 0.375	Measurement: cup	Descriptors: brown	Preparation:packed
Name: maple syrup	Quantity: 0.5	Measurement: cup
Name: salt	Quantity: 1.0	Measurement: pinch

Steps:
Preheat the oven to 350 degrees F (175 degrees C)
Coat the inside of a 9-inch fluted tube pan with cooking spray
Mix white Splenda, pudding mix, and cinnamon together in a 1-gallon resealable plastic bag
Add the quartered biscuits and shake until well coated
Toss in the bacon and shake well to distribute
Transfer biscuits to the prepared tube pan
Save the Splenda-cinnamon mixture left in the bottom of the bag
Melt butter in a small saucepan over medium heat
Stir in dark brown Splenda, maple syrup, and salt
Bring mixture to a boil and carefully stir until it begins to foam, about 1 minute
Pour the saved Splenda-cinnamon mixture into the saucepan and stir until dissolved, 2 to 3 minutes
Pour the melted Splenda mixture over the biscuits in the tube pan
Bake in the preheated oven until the biscuits are puffed up and cooked through, 50 to 55 minutes
Cool in the pan for 10 minutes before inverting onto a serving plate

Methods:
Preheat, Coat, Mix, Add, Toss, Transfer, Save, Melt, Stir, Bring, Pour, Pour, Bake, Cool

Tools:
```
