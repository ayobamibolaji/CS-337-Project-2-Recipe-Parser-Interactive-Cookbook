ordinals = {
    "first": 1,
    "one": 1,
    "second": 2,
    "two": 2,
    "third": 3,
    "three": 3,
    "fourth": 4,
    "four": 4,
    "fifth": 5,
    "five": 5,
    "sixth": 6,
    "six": 6,
    "seventh": 7,
    "seven": 7,
    "eighth": 8,
    "eight": 8,
    "ninth": 9,
    "nine": 9,
    "tenth": 10,
    "ten": 10,
    "last": -1
}

bot_names = [
    "Larry BurnBot",
    "Bot Ramsay",
    "Gusteau Bot",
    "Linguini Bot",
    "your humble recipe guide",
    "RecipeTron",
    "RecipeBot 3000",

]

def parseCommand(cmd):
    main_cmd = ""
    num = False
    query = False

    text = cmd.lower()
    split_text = text.split()

    # Extract any numbers in text (should only be one in the command)
    for word in split_text:
        if word.isdigit() or word in ordinals:
            num = word
    
    # Replace the occurance of 'num' with 'N'
    main_cmd = text.replace(num, "NUMBER") if num else text

    if num:
        if is_int(num):
            num = int(num)
        else:
            num = ordinals[num]

    # Extract query if the command is the "how do I..." command
    # if split_text[0] == "how" and not text == "how do i do that"


    return (main_cmd, num, query)

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False