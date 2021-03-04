#CS 337 Project 2: Recipe Parser and Transformer
##Installation:
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
pip install -r requirements.txt
```
##Run code:
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