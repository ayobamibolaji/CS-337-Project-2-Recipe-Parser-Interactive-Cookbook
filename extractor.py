import re

# Takes in string, and a regex script, and returns a dictionary with the script labels and their values
def extractFromScript(str, script):
    p = re.compile(script)
    groups = [group for group in p.groupindex]
    match = p.search(str)
    return {grp:match.group(grp) for grp in groups if match.group(grp)}
