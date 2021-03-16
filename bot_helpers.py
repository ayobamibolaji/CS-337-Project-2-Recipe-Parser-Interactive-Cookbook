ordinals = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
    "seventh": 7,
    "eighth": 8,
    "ninth": 9,
    "tenth": 10
}

def parseCommand(cmd):
    main_cmd = ""
    num = False
    query = False

    text = cmd.lower()
    split_text = text.split()

    # Extract any numbers in text (should only be one in the command)
    for word in split_text:
        if word.isdigit():
            num = int(word)
        elif word in ordinals:
            num = ordinals[word]
    
    # Replace the occurance of 'num' with 'N'
    main_cmd = text.replace(str(num), "N")

    # Extract query if the command is the "how do I..." command
    # if split_text[0] == "how" and not text == "how do i do that"

    return (main_cmd, num, query)
