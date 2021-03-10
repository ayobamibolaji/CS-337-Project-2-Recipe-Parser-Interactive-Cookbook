QUANTITIES = {
    "½": "0.5",
    "¼": "0.25",
    "¾": "0.75",
    "⅓": "0.333",
    "⅔": "0.666",
    "⅛": "0.125",
    "⅜": "0.375",
    "⅝": "0.625",
    "⅞": "0.875"
}

MEASURES = [
    'tablespoon',
    'teaspoon',
    'pinch',
    'quart',
    'liter',
    'cup',
    'gallon',
    'clove',
    'dash',
    'cubes',
    'pound',
    'loaf',
    'package',
    'strips',
    'oz',
    'clove',
    'pound',
    'lbs',
    'ounce',
    'serving',
    'slice',
    'can',
    'drops'
]

FATS = [
    "butter",
    "margarine",
    "shortening",
    "oil",
    "lard"
]

COMMON_INGREDIENTS = [
    "all-purpose flour",
    "food coloring",
    "milk chocolate",
    "dark chocolate",
    "sweet potato",
    "turkey bacon",
    "asparagus"
]

COMMON_DESCRIPTORS = [
    "skinless",
    "skim",
    "Brown Sugar"
]

COMMON_PREPARATIONS = [
    "riced",
    "ground",
    "cut",
    "refried"
]

COLORS = [
]

MEAT_SUBSTITUTES = {
    'beef broth': 'mushroom broth',
    'chicken broth': 'vegetable broth',
    'ground beef': 'tempeh',
    'beef': 'jackfruit',
    'steak': 'jackfruit',
    'chicken': 'seitan',
    'pork': 'seitan',
    'bacon': 'tempeh',
    'sirloin': 'jackfruit',
    'liver': 'tofu',
    'veal': 'jackfruit',
    'lamb': 'jackfruit',
    'duck': 'seitan',
    'poultry': 'seitan',
    'loin': 'jackfruit',
    'oyster': 'mushrooms',
    'salmon': 'mushrooms',
    'fillet': 'tofu',
    'shrimp': 'mushrooms',
    'crab': 'tofu',
    'tuna': 'tofu',
    'scallop': 'mushrooms',
    'lobster': 'tofu',
    'fish': 'tofu',
    'cod': 'tofu',
    'escargot': 'tofu',
    'goat': 'seitan',
    'mutton': 'seitan',
    'sausage': 'beyond sausage',
    'frog': 'tofu',
    'toad': 'tofu',
    'meat': 'tofu',
    'hamburger': 'veggie burger',
    'french fries': 'salad',
    'ham':'tofu',
    'Worcestershire sauce': 'balsamic vinegar'
}


VEGGIE_SUBSTITUTES = {
    'tofu': 'pork',
    'mushroom broth': 'beef broth',
    'vegetable broth': 'chicken broth',
    'seitan': 'chicken',
    'mushroom': 'salmon',
    'jackfruit': 'beef',
    'tempeh': 'ground beef',
    'butter': 'lard',
    'veggie burger': 'hamburger'
}

ASIAN_SIDES = {
    'rice': 'jasmine rice',
    'white rice': 'jasmine rice',
    'potatoes': 'jasmine rice',
    'potato': 'jasmine rice',
    'pasta': 'jasmine rice',
    'noodle': 'jasmine rice',
    'noodles': 'jasmine rice',
    'spaghetti': 'jasmine rice',
    'fettuccine': 'jasmine rice',
    'penne': 'jasmine rice',
    'rigatoni': 'jasmine rice',
    'macaroni': 'jasmine rice',
    'corn': 'jasmine rice',
}

TURKISH_SIDES = {
    'rice': 'bulgur pilaf',
    'white rice': 'bulgur pilaf',
    'potatoes': 'bulgur pilaf',
    'potato': 'bulgur pilaf',
    'pasta': 'bulgur pilaf',
    'noodle': 'bulgur pilaf',
    'noodles': 'bulgur pilaf',
    'spaghetti': 'bulgur pilaf',
    'fettuccine': 'bulgur pilaf',
    'penne': 'bulgur pilaf',
    'rigatoni': 'bulgur pilaf',
    'macaroni': 'bulgur pilaf',
    'corn': 'bulgur pilaf',
}

TURKISH_SPICES = {
    'chives': 'dried allium',
    'cloves': 'mint',
    'ginger': 'galangal',
    'onion': 'turkish sumac onion',
    'cilantro': 'cumin',
    'asparagus': 'dried allium',
    'oregano': 'cumin',
    'shredded cabbage': 'cumin',
    'lemon': 'sumac',
    'lime': 'sumac',
    'nutmeg': 'thyme',
    'rosemary': 'thyme',
    'basil': 'cumin',
    'saffron': 'turmeric',
    'mustard': 'turmeric',
    'paprika': 'red pepper flakes',
    'cinnamon': 'cumin',
    'vanilla': 'bay leaf',
    'seed': 'red pepper flakes',
    'seeds': 'red pepper flakes'
}

ASIAN_SPICES = {
    'chives': ('chinese garlic chives', 1, (lambda ing: 'chives' in ing.name)),
    'garlic': ('chinese garlic chives', 1, (lambda ing: 'garlic' in ing.name)),
    'cloves': ('baharat', 1, (lambda ing: 'cloves' in ing.name)),
    'ginger': ('galangal', 1, (lambda ing: 'ginger' in ing.name)),
    'onion': ('scallion', 1, (lambda ing: 'onion' in ing.name)),
    'cilantro': ('golden needles', 1, (lambda ing: 'cilantro' in ing.name)),
    'asparagus': ('golden needles', 1, (lambda ing: 'asparagus' in ing.name)),
    'oregano': ('golden needles', 1, (lambda ing: 'oregano' in ing.name)),
    'cabbage': ('golden needles', 1, (lambda ing: 'cabbage' in ing.name and 'shredded' in ing.preparations)),
    'lemon': ('kaffir lime leaves', 1, (lambda ing: 'lemon' in ing.name)),
    'thyme': ('kaffir lime leaves', 1, (lambda ing: 'thyme' in ing.name)),
    'lime': ('kaffir lime leaves', 1, (lambda ing: 'lime' in ing.name)),
    'nutmeg': ('kaffir lime leaves', 1, (lambda ing: 'nutmeg' in ing.name)),
    'rosemary': ('kaffir lime leaves', 1, (lambda ing: 'rosemary' in ing.name)),
    'basil': ('thai basil', 1, (lambda ing: 'basil' in ing.name)),
    'saffron': ('turmeric', 1, (lambda ing: 'saffron' in ing.name)),
    'mustard': ('turmeric', 1, (lambda ing: 'mustard' in ing.name)),
    'paprika': ('turmeric', 1, (lambda ing: 'paprika' in ing.name)),
    'cinnamon': ('zeylanicum', 1, (lambda ing: 'cinnamon' in ing.name)),
    'vanilla': ('pandan', 1, (lambda ing: 'vanilla' in ing.name)),
    'seed': ('coriander seeds', 1, (lambda ing: 'seed' in ing.name and 'coriander' not in ing.name and 'anise' not in ing.name))
}

UNHEALTHY_SUBSTITUTES = {
    # unhealthyIng: (new Ingredient(), quantMultiplier, lambda function)
    'sugar': ("Splenda", 0.5, (lambda ing: "sugar" in ing.name and "brown" not in ing.descriptors)),
    'chicken': ("skinless chicken", 1, (lambda ing: "chicken" in ing.name)),
    'butter': ('avocado', .8, (lambda ing: "avocado" in ing.name)),
    'beef': ("ground turkey", 1, (lambda ing: "ground beef" in ing.name)),
    'rice': ("riced cauliflower", 1, (lambda ing: "rice" in ing.name and "white" in ing.descriptors)),
    "potato": ("sweet potato", 1, (lambda ing: "potato" in ing.name and "sweet" not in ing.name)),
    "yogurt": ("Greek yogurt", 1, (lambda ing: "yogurt" in ing.name and "Greek" not in ing.name)),
    "bacon": ("turkey bacon", 1, (lambda ing: 'bacon' in ing.name and 'turkey' not in ing.name)),
    "milk chocolate": ("dark chocolate", 1, (lambda ing: "milk chocolate" in ing.name)),
    "milk": ("skim milk", 1, (lambda ing: "milk" in ing.name and "milk chocolate" not in ing.name)),
    "sugar": ("Brown Sugar Splenda Blend", 0.5, (lambda ing: "sugar" in ing.name and "brown" in ing.descriptors)),
    'cream': ('Greek yogurt', 1, (lambda ing: "cream" in ing.name and "sour" in ing.descriptors)),
    'flour': ('whole wheat flour', 1, (lambda ing: "flour" in ing.name and "all-purpose" in ing.descriptors)),
    'flour tortilla': ('corn tortilla', 1, (lambda ing: "flour tortilla" in ing.name))
}


HEALTHY_SUBSTITUTES = {
    'Splenda': ('sugar', 1.5),
    'skinless chicken': ('chicken', 1),
    'artificial sweetener': ('sugar', 1.5),
    'quinoa': ('white rice', 1.1),
    'brown rice': ('white rice', 1.1),
    'zoodles': ('noodles', 1),
    'turkey bacon': ('bacon', 1.1),
    'dark chocolate': ('milk chocolate', 1.1),
    'whole wheat flour': ('all-purpose flour', 1),
    'corn tortilla': ('flour tortilla', 1)

}

MAIN_METHODS = [
    'bake', 
    'boil', 
    'cook',
    'broil', 
    'fry', 
    'grill',
    'steam',
    'stew',
    'braise',
    'roast', 
    'mix', 
    'heat',
    'simmer',
    'deep fry',
    'sear',
    'poach', 
    'whip', 
    'saute',
    'air fry'

]

NON_SECONDARY_METHODS = [
    'bring',
    'place',
    'use',
    'remove',
    'add',
    'combine',
    'continue',
    'slip',
    'set',
    'return',
    'serve',
    'transfer',
    'take',
    'save',
]

TOOLS = ['corer', 'cutter', 'spoon', 'knife', 'pan', 'whisk',
 'beanpot', 'pot', 'skillet', 'cup', 'mug', 'colander',
 'bowl', 'tray', 'slicer', 'pitter', 'cleaver', 'corkscrew',
 'board', 'poacher', 'separator', 'timer', 'scale',
 'sifter', 'funnel', 'grater', 'strainer', 'chopper',
 'dipper', 'ladle', 'squeezer', 'juicer', 'mandoline',
 'grinder', 'tenderiser', 'thermometer', 'baller',
 'pestle', 'nutcracker', 'glove', 'blender', 'brush',
 'peeler', 'masher', 'ricer', 'pin', 'shaker', 'sieve',
 'scoop', 'spatula', 'tamis', 'tongs', 'zester',
 'scooper', 'processor', 'process', 'blend', 'saute',
 'oven', 'cooker', 'saucepan', 'pressure', 'fryer']


def cleanIngredientText(txt):
    txt = ' '.join(txt.split())
    for str, rep in QUANTITIES.items():
        txt = txt.replace(str, rep)
    
    txt = combineQuantity(txt)
    
    return txt


# This helper combines all numbers in the beginning of an ingredient into one quantity
def combineQuantity(txt):
    quantity = 0.0
    idx = 0
    split_txt = txt.split()
    for token in split_txt:
        try:
            num = float(token)
            quantity += num
            idx += 1
        except ValueError:
            break

    split_txt = ["{:.2f}".format(quantity)] + split_txt[idx:] if idx > 0 else split_txt
    return ' '.join(split_txt)


# Token helpers
def previousToken(token):
    if token.i == 0:
        return False
    else:
        return token.doc[token.i - 1]

def nextToken(token):
    if token.i == len(token.doc) - 1:
        return False
    else:
        return token.doc[token.i + 1]

def precedingWords(token, pos=['NOUN', 'PROPN'], restrictions=[]):
    words = ""

    currToken = token
    while True:
        prevToken = previousToken(currToken)
        if prevToken and prevToken.pos_ in pos and prevToken.text not in restrictions:
            words = prevToken.text + " " + words
            currToken = prevToken
        else:
            break
    
    return words


def proceedingWords(token, pos=['NOUN', 'PROPN'], restrictions=[]):
    words = ""

    currToken = token
    while True:
        nxtToken = nextToken(currToken)
        if nxtToken and nxtToken.pos_ in pos and nxtToken.text not in restrictions:
            words = nxtToken.text + " " + words
            currToken = nxtToken
        else:
            break

    return words

def tokenHasProperties(token, pos="", tag="", dep="", parent="", child=[]):
    if not token: return False
    if pos and token.pos_ != pos: return False
    if tag and token.tag_ != tag: return False
    if dep and token.dep_ != dep: return False
    if parent and token.parent.text != parent: return False
    if child and child not in [child.text for child in token.children]: return False
    return True


def containsAnyOf(str, lst):
    for aStr in lst:
        if aStr in str:
            return True
    return False


lst_of_urls = ["https://www.allrecipes.com/recipe/184255/quick-savory-cranberry-glazed-pork-loin-roast/",
               "https://www.allrecipes.com/recipe/279984/air-fryer-sweet-and-spicy-roasted-carrots/",
               "https://www.allrecipes.com/recipe/18344/cheese-and-bacon-potato-rounds/",
               "https://www.allrecipes.com/recipe/230695/cheddar-bacon-ranch-pulls/",
               "https://www.allrecipes.com/recipe/21061/bacon-and-cheddar-stuffed-mushrooms/",
               "https://www.allrecipes.com/recipe/81038/worlds-best-bacon-cheese-dip/",
               "https://www.allrecipes.com/recipe/23947/bacon-crackers/",
               "https://www.allrecipes.com/recipe/246256/bacon-jalapeno-popper-puffs/",
               "https://www.allrecipes.com/recipe/230646/bacon-wrapped-tater-tots/",
               "https://www.allrecipes.com/recipe/69919/bacon-wrapped-smokies/",
               "https://www.allrecipes.com/recipe/69084/bacon-cheddar-deviled-eggs/",
               "https://www.allrecipes.com/recipe/240583/cheesy-ham-and-corn-chowder/",
               "https://www.allrecipes.com/recipe/245774/bucatini-allamatriciana/",
               "https://www.allrecipes.com/recipe/262225/instant-pot-baby-back-ribs/",
               "https://www.allrecipes.com/recipe/14746/mushroom-pork-chops/",
               "https://www.allrecipes.com/recipe/139603/slow-cooker-carnitas/",
               "https://www.allrecipes.com/recipe/237501/spam-fries-with-spicy-garlic-sriracha-dipping-sauce/",
               "https://www.allrecipes.com/recipe/247371/pork-loin-roast-with-baby-bellas/",
               "https://www.allrecipes.com/recipe/261472/easy-maple-bacon-monkey-bread/",
               "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
               "https://www.allrecipes.com/recipe/92462/slow-cooker-texas-pulled-pork/",
               "https://www.allrecipes.com/recipe/10656/irish-soda-bread-cookies/",
               "https://www.allrecipes.com/recipe/278882/triple-chocolate-chunk-cookies/",
               "https://www.allrecipes.com/recipe/15324/ginger-touched-oatmeal-peanut-butter-cookies/",
               "https://www.allrecipes.com/recipe/246328/french-macarons/",
               "https://www.allrecipes.com/recipe/277919/salted-chocolate-cookies/",
               "https://www.allrecipes.com/recipe/261865/gluten-free-magic-cookie-bars/",
               "https://www.allrecipes.com/recipe/278832/italian-cookies-with-anise/",
               "https://www.allrecipes.com/recipe/10118/rainbow-cookies/",
               "https://www.allrecipes.com/recipe/242366/easy-chewy-flourless-peanut-butter-cookies/",
               "https://www.allrecipes.com/recipe/260575/chef-johns-almond-biscotti/",
               "https://www.allrecipes.com/recipe/10661/oatmeal-peanut-butter-bars/",
               "https://www.allrecipes.com/recipe/166081/deep-fried-oreos/",
               "https://www.allrecipes.com/recipe/277700/instant-pot-filipino-chicken-adobo/",
               "https://www.allrecipes.com/recipe/281604/simple-instant-pot-mashed-potatoes/",
               "https://www.allrecipes.com/recipe/276655/instant-pot-sweet-and-sour-pork/",
               "https://www.allrecipes.com/recipe/276654/instant-pot-loaded-baked-potato-soup/",
               "https://www.allrecipes.com/recipe/273522/instant-pot-green-chili-chicken-and-rice/",
               "https://www.allrecipes.com/recipe/274921/instant-pot-crispy-chicken-carnitas/",
               "https://www.allrecipes.com/recipe/269030/instant-pot-yankee-pot-roast/",
               "https://www.allrecipes.com/recipe/267986/instant-pot-pan-juice-gravy/",
               "https://www.allrecipes.com/recipe/268026/instant-pot-corned-beef/",
               "https://www.allrecipes.com/recipe/258468/beef-stroganoff-for-instant-pot/",
               "https://www.allrecipes.com/recipe/220869/easy-pressure-cooker-pot-roast/",
               "https://www.allrecipes.com/recipe/261498/instant-pot-garlic-roasted-potatoes/",
               "https://www.allrecipes.com/recipe/263876/best-instant-pot-scalloped-potatoes/",
               "https://www.allrecipes.com/recipe/280269/instant-pot-potato-salad/",
               "https://www.allrecipes.com/recipe/261394/instant-pot-mashed-potatoes/",
               "https://www.allrecipes.com/recipe/269144/instant-pot-sweet-potato-casserole/",
               "https://www.allrecipes.com/recipe/279426/instant-pot-bangers-and-mash/",
               "https://www.allrecipes.com/recipe/280718/instant-pot-broccolini-and-potato-salad/",
               "https://www.allrecipes.com/recipe/16354/easy-meatloaf/"]
