the_replacements = {
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

measures = [
    'tablespoon',
    'pinch'
]

def cleanIngredientText(txt):
    txt = ' '.join(txt.split())
    for str, rep in the_replacements.items():
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

def precedingWords(token, pos='NOUN', restrictions=[]):
    words = ""

    currToken = token
    while True:
        prevToken = previousToken(currToken)
        if prevToken and prevToken.pos_ == 'NOUN' and prevToken.text not in restrictions:
            words = prevToken.text + " " + words
            currToken = prevToken
        else:
            break
    
    return words


def proceedingWords(token, pos='NOUN', restrictions=[]):
    words = ""

    currToken = token
    while True:
        nxtToken = nextToken(currToken)
        if nxtToken and nxtToken.pos_ == 'NOUN' and nxtToken.text not in restrictions:
            words = nxtToken.text + " " + words
            currToken = nxtToken
        else:
            break

    return words


def containsAnyOf(str, lst):
    for aStr in lst:
        if aStr in str:
            return True
    return False


lst_of_urls = ["https://www.allrecipes.com/recipe/279984/air-fryer-sweet-and-spicy-roasted-carrots/",
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
               "https://www.allrecipes.com/recipe/280718/instant-pot-broccolini-and-potato-salad/"]
