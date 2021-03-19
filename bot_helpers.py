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
    text = "".join(c for c in text if c not in ('!', '.', ':', "-", ";", "'", "?", ",", "(", ")", '"'))
    split_text = text.split()


    # Extract query if the command is the "how do I..." command
    # if split_text[0] == "how" and not text == "how do i do that"
    if "how do i do that" in text or text == "how":
        return ("how do i do that", num, "how do i do that")
    if "how do i" in text:
        query = text[text.find("how do i") + len("how do i") :].split()
        main_cmd = "how do i QUERY"
        text = "how do i QUERY"

    # Extract any numbers in text (should only be one in the command)
    for word in split_text:
        if word.isdigit() or word in ordinals:
            num = word
    
    # Replace the occurrence of 'num' with 'N'
    main_cmd = text.replace(num, "NUMBER") if num else text

    if num:
        if is_int(num):
            num = int(num)
        else:
            num = ordinals[num]

    return (main_cmd, num, query)

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False