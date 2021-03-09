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
Welcome. Please enter an AllRecipes url for us to parse.
https://www.allrecipes.com/recipe/21061/bacon-and-cheddar-stuffed-mushrooms/
Got it!
Name: Bacon and Cheddar Stuffed Mushrooms

Ingredients:

  Quantity  Measurement    Name               Descriptors    Preparation
----------  -------------  -----------------  -------------  -------------
      3     slices         bacon
      8                    crimini mushrooms
      1     tablespoon     butter
      1     tablespoon     onion                             chopped
      0.75  cup            Cheddar cheese                    shredded

Steps:
Place bacon in a large, deep skillet
Cook over medium high heat until evenly brown
Drain, dice and set aside
Preheat oven to 400 degrees F (200 degrees C)
Remove mushroom stems
Set aside caps
Chop the stems
In a large saucepan over medium heat, melt the butter
Slowly cook and stir the chopped stems and onion until the onion is soft
Remove from heat
In a medium bowl, stir together the mushroom stem mixture, bacon and 1/2 cup Cheddar
Mix well and scoop the mixture into the mushroom caps
Bake in the preheated oven 15 minutes, or until the cheese has melted
Remove the mushrooms from the oven, and sprinkle with the remaining cheese

Methods:
heat, preheat, stir, mix, bake

Tools:
skillet, oven, saucepan, bowl, cup, scooper

Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
2) Double the quantity
3) Halve the quantity
4) Make it healthier
5) Make it less healthy
6) Make it vegetarian
7) Make it un-vegetarian
8) Convert to Asian cuisine
9) Quit
4
We made the recipe healthier. Here you go!
Name: Healthy Bacon and Cheddar Stuffed Mushrooms

Ingredients:

  Quantity  Measurement    Name               Descriptors    Preparation
----------  -------------  -----------------  -------------  -------------
       2.4  slices         turkey bacon
       6.4                 crimini mushrooms
       0.2  tablespoon     oil                olive
       0.8  tablespoon     onion                             chopped
       0.6  cup            Cheddar cheese                    shredded

Steps:
Place turkey bacon in a large, deep skillet
Cook over medium high heat until evenly brown
Drain, dice and set aside
Preheat oven to 400 degrees F (200 degrees C)
Remove mushroom stems
Set aside caps
Chop the stems
In a large saucepan over medium heat, melt the oil
Slowly cook and stir the chopped stems and onion until the onion is soft
Remove from heat
In a medium bowl, stir together the mushroom stem mixture, turkey bacon and 1/2 cup Cheddar
Mix well and scoop the mixture into the mushroom caps
Bake in the preheated oven 15 minutes, or until the cheese has melted
Remove the mushrooms from the oven, and sprinkle with the remaining cheese

Methods:
heat, preheat, stir, mix, bake

Tools:
skillet, oven, saucepan, bowl, cup, scooper

Would you like to apply another transformation? If so...
Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
2) Double the quantity
3) Halve the quantity
4) Make it healthier
5) Make it less healthy
6) Make it vegetarian
7) Make it un-vegetarian
8) Convert to Asian cuisine
9) Quit
9
Goodbye.
```
You can also run main without an argument to run 50 sample recipes.

You can also run main with the url as the argument. An example is below:
```
python main.py https://www.allrecipes.com/recipe/92462/slow-cooker-texas-pulled-pork/
We received your recipe!
Name: Slow Cooker Texas Pulled Pork

Ingredients:

  Quantity  Measurement    Name                  Descriptors    Preparation
----------  -------------  --------------------  -------------  -------------
      1     teaspoon       vegetable oil
      1                    pork shoulder roast
      1     cup            barbeque sauce
      0.5   cup            apple cider vinegar
      0.5   cup            chicken broth
      0.25  cup            brown sugar           light
      1     tablespoon     mustard               yellow         prepared
      1     tablespoon     Worcestershire sauce
      1     tablespoon     chili powder
      1                    onion                 extra, large   chopped
      2                    cloves garlic         large          crushed
      1.5   teaspoons      thyme
      8                    hamburger buns
      2     tablespoons    butter

Steps:
Pour the vegetable oil into the bottom of a slow cooker
Place the pork roast into the slow cooker; pour in the barbecue sauce, apple cider vinegar, and chicken broth
Stir in the brown sugar, yellow mustard, Worcestershire sauce, chili powder, onion, garlic, and thyme
Cover and cook on High until the roast shreds easily with a fork, 5 to 6 hours
Remove the roast from the slow cooker, and shred the meat using two forks
Return the shredded pork to the slow cooker, and stir the meat into the juices
Spread the inside of both halves of hamburger buns with butter
Toast the buns, butter side down, in a skillet over medium heat until golden brown
Spoon pork into the toasted buns

Methods:
roast, stir, heat, cook with slow cooker

Tools:
slow cooker, skillet, spoon

Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
2) Double the quantity
3) Halve the quantity
4) Make it healthier
5) Make it less healthy
6) Make it vegetarian
7) Make it un-vegetarian
8) Convert to Asian cuisine
9) Quit
6
We made the recipe vegetarian. Here you go!
Name: Vegetarian Slow Cooker Texas Pulled Pork

Ingredients:

  Quantity  Measurement    Name                 Descriptors    Preparation
----------  -------------  -------------------  -------------  -------------
      1     teaspoon       vegetable oil
      1                    seitan
      1     cup            barbeque sauce
      0.5   cup            apple cider vinegar
      0.5   cup            vegetable broth
      0.25  cup            brown sugar          light
      1     tablespoon     mustard              yellow         prepared
      1     tablespoon     balsamic vinegar
      1     tablespoon     chili powder
      1                    onion                extra, large   chopped
      2                    cloves garlic        large          crushed
      1.5   teaspoons      thyme
      8                    veggie burger
      2     tablespoons    butter

Steps:
Pour the vegetable oil into the bottom of a slow cooker
Place the seitan roast into the slow cooker; pour in the barbecue sauce, apple cider vinegar, and vegetable broth
Stir in the brown sugar, yellow mustard, balsamic vinegar, chili powder, onion, garlic, and thyme
Cover and cook on High until the roast shreds easily with a fork, 5 to 6 hours
Remove the roast from the slow cooker, and shred the meat using two forks
Return the shredded seitan to the slow cooker, and stir the meat into the juices
Spread the inside of both halves of veggie burger buns with butter
Toast the buns, butter side down, in a skillet over medium heat until golden brown
Spoon seitan into the toasted buns

Methods:
roast, stir, heat, cook with slow cooker

Tools:
slow cooker, skillet, spoon

Would you like to apply another transformation? If so...
Please enter the integer from the list below corresponding to a transformation to apply to the recipe.
1) Identity transformation (no transformation)
2) Double the quantity
3) Halve the quantity
4) Make it healthier
5) Make it less healthy
6) Make it vegetarian
7) Make it un-vegetarian
8) Convert to Asian cuisine
9) Quit
9
Goodbye.
```
