from bot_helpers import *
from DecomposedText import DecomposedText
from RecipeInfo import RecipeInfo
from tabulate import tabulate
import random
from NLP import mostSimilar
from DecomposedText import DecomposedText
from helpers import proceedingWords

def initiate_bot():
    print(f"\nHello! I am {random.choice(bot_names)}.")
    default()

def default():
    if state["curr_step"] is not None and state["curr_step"] + 1 < len(state["curr_recipe"].Steps):
        ask_next_step()
    else:
        command = input("What would you like to do?\n")
        process_command(command)

def process_command(command):
    parsed_cmd, num, query = parseCommand(command)
    parsed_cmd = mostSimilar(parsed_cmd, [cmd for cmd in commands])[0]
    fun = commands[parsed_cmd] if parsed_cmd in commands else None

    if isinstance(fun, bool) or fun == None:
        print("I'm not sure what you mean...")
        default()
    else:
        fun(num, query)

def initiate_recipe(N, Q):
    # First time recipe
    if state["curr_recipe"] is None:
        get_recipe()
    # Starting a new recipe
    else:
        p_q = input("You want to walk through a different recipe?\n")
        p_q_sim = mostSimilar(p_q, [cmd for cmd in commands])[0]
        ans = commands[p_q_sim] if p_q_sim in commands else None
        if isinstance(ans, bool):
            if ans:
                get_recipe()
            else:
                print("Alright, we'll stick with this one.")
                default()
        else:
            process_command(p_q)

    # Next command
    state["curr_step"] = None
    print(f"Alrighty then, let's work with \"{state['curr_recipe'].name}\".")
    command = input("What do you want to do: go over the ingredients, or go over the recipe steps?\n")
    process_command(command)
    
def get_recipe():
    command = input("Sure thing. Please specify an AllRecipes.com URL:\n").strip()
    if not command.startswith("https://www.allrecipes.com/recipe/"):
        print("Hmmm, that's not a valid AllRecipes.com URL...")
        command = input("What would you like to do?\n")
        process_command(command)
    else:
        try:
            rcp = RecipeInfo(command)
            state["curr_recipe"] = rcp
        except:
            print("Hmm, that URL didn't quite work.")
            command = input("What would you like to do?\n")
            process_command(command)

def show_rcp_ingredients(N, Q):
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        print(f"Alright, here is the ingredients list for \"{rcp.name}\":")
        print(tabulate([[ing.quantity, ing.measurement, ing.name, ing.descriptors, ing.preparation] for ing in rcp.Ingredients],
                       headers=['Quantity', "Measurement", 'Name', "Descriptors", "Preparation"]))
        default()


def show_rcp_methods(N,Q):
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        print(f"Alright, here is the methods list for \"{rcp.name}\":")
        print(tabulate([[method] for method in rcp.primaryMethods],
                       headers=["Primary Methods"]))
        print("\n")
        print(tabulate([[method] for method in rcp.secondaryMethods],
                       headers=["Secondary Methods"]))

        default()


def show_rcp_tools(N,Q):
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        print(f"Alright, here is the tools list for \"{rcp.name}\":")
        print(tabulate([[tool] for tool in rcp.Tools],
                       headers=["Tools"]))
        
        default()



def iterate_rcp_steps(N, Q):
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif state["curr_step"] is not None:
        print("We're going over the steps right now!")
        default()
    else:
        state["curr_step"] = -1
        next_step(N, Q)

def next_step(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        if curr_step + 1 == len(rcp.Steps):
            print(f"Step {curr_step + 1} is already the last step!")
            default()
        else:
            curr_step += 1
            state["curr_step"] = curr_step
            next_cmd = input(f"Step {curr_step + 1} is: " + rcp.Steps[curr_step] + '\n')
            process_command(next_cmd)

def ask_next_step():
    p_q = input("Should I continue to the next step?\n")
    p_q_sim = mostSimilar(p_q, [cmd for cmd in commands])[0]
    ans = commands[p_q_sim] if p_q_sim in commands else None
    if isinstance(ans, bool):
        if ans:
            next_step(False, False)
        else:
            command = input("What would you like to do then?\n")
            process_command(command)
    else:
        process_command(p_q)

def previous_step(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        if curr_step == 0:
            print(f"This is the first step!")
            default()
        else:
            curr_step -= 1
            state["curr_step"] = curr_step
            next_cmd = input(f"Step {curr_step + 1} is: " + rcp.Steps[curr_step] + '\n')
            process_command(next_cmd)


def show_step_ingredients(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        ingredients = []
        rcp = state["curr_recipe"]
        text_of_step = rcp.Steps[curr_step].lower()

        for ingredient in rcp.Ingredients:
            if ingredient.name in text_of_step:
                ingredients.append(ingredient.name)

        if ingredients:
            print(tabulate([[ingredient] for ingredient in ingredients],
                           headers=[f"Step {curr_step + 1}'s Ingredients"]))
        else:
            print("There aren't any ingredients in this step!")

        default()

def show_step_tools(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        tools = []
        rcp = state["curr_recipe"]
        text_of_step = rcp.Steps[curr_step].lower()

        for tool in rcp.Tools:
            if tool in text_of_step:
                tools.append(tool)

        # checking common tools in case they're inferred
        # in step, like "bake at 350", tool should be oven
        if "Bake" in text_of_step or "bake" in text_of_step and "oven" not in tools:
            tools.append("oven")
        if "Boil" in text_of_step or "boil" in text_of_step and "pot" not in tools:
            tools.append("pot")
        if "Fry" in text_of_step or "fry" in text_of_step and "pan" not in tools:
            tools.append("pan")
        if "Stir" in text_of_step or "stir" in text_of_step and "ladle" not in tools:
            tools.append("ladle")

        if tools:
            print(tabulate([[tool] for tool in tools],
                           headers=[f"Step {curr_step + 1}'s Tools"]))
        else:
            print("There aren't tools in this step!")

        default()

def show_step_methods(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        pri_methods = []
        sec_methods = []
        rcp = state["curr_recipe"]
        text_of_step = rcp.Steps[curr_step].lower()

        for method in rcp.primaryMethods:
            if method in text_of_step:
                pri_methods.append(method)

        for method in rcp.secondaryMethods:
            if method in text_of_step:
                sec_methods.append(method)

        if pri_methods:
            print(tabulate([[method] for method in pri_methods],
                           headers=[f"Step {curr_step + 1}'s Primary Methods"]))
            print("\n")
        else:
            print("There aren't any primary methods in this step!")

        if sec_methods:
            print(tabulate([[method] for method in sec_methods],
                           headers=[f"Step {curr_step + 1}'s Secondary Methods"]))
        else:
            print("There aren't any secondary methods in this step!")

        default()

def jump_to_step(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else:
        rcp = state["curr_recipe"]
        if not N:
            print("That is not a valid step number...")
            default()
        if N > len(rcp.Steps):
            print(f"There are only {len(rcp.Steps)} steps in this recipe!")
            default()
        elif N == -1:
            curr_step = len(rcp.Steps) -1
            state["curr_step"] = curr_step
            next_cmd = input(f"Step {curr_step + 1} is: " + rcp.Steps[curr_step] + '\n')
            process_command(next_cmd)
        elif N < 1:
            print("There aren't any step numbers less than 1!")
            default()
        else:
            curr_step = N - 1
            state["curr_step"] = curr_step
            next_cmd = input(f"Step {curr_step + 1} is: " + rcp.Steps[curr_step] + '\n')
            process_command(next_cmd)

def rewind_steps(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else: 
        jump_to_step(state["curr_step"] + 1 - N, Q)

def forward_steps(N, Q):
    curr_step = state["curr_step"]
    if state["curr_recipe"] is None:
        print("We're not working with any recipe yet!")
        default()
    elif curr_step is None:
        print("We're not going over the steps yet!")
        default()
    else: 
        jump_to_step(state["curr_step"] + 1 + N, Q)

def repeat_step(N, Q):
    jump_to_step(state["curr_step"] + 1, Q)

def specific_query(N, Q):
    Q.insert(0, "how")
    Q.insert(1, "to")
    google_url = "https://www.google.com/search?q=" + "+".join(Q)
    youtube_url = "https://www.youtube.com/results?search_query=" + "+".join(Q)
    print("No worries. I found these links for you:")
    print(google_url)
    print(youtube_url)
    default()

def vague_query(N, Q):
    if state["curr_recipe"] is None:
        next_cmd = input("Can you rephrase that?")
        process_command(next_cmd)
    elif state["curr_step"] is None:
        next_cmd = input("I'm not sure I understand. Would you like to go over the steps?")
        process_command(next_cmd)
    else:
        rcp = state["curr_recipe"]
        step = rcp.Steps[state["curr_step"]]
        doc = DecomposedText(step)
        #doc.show()
        root = doc.getRoot()
        ingredients = []
        for ingredient in rcp.Ingredients:
            if ingredient.name in step:
                ingredients.append(ingredient.name)
        tools = []
        for tool in rcp.Tools:
            if tool in step:
                tools.append(tool)
        #print(root)
        query = ["how", "to", root.text.lower()]
        if len(ingredients) > 0:
            query.append("using")
            ingredients = ",+".join(ingredients)
            query.append(ingredients)
        elif len(ingredients) == 0 and len(tools) > 0:
            query.append("using")
            tools = ",+".join(tools)
            query.append(tools)
        else:
            Text = DecomposedText(state["curr_recipe"].Steps[state["curr_step"]].lower())
            root = Text.getRoot()
            Q = root.text + " " + proceedingWords(root, pos=["NOUN", "VERB", "ADV", "DET", "CCONJ", "ADP", "PART", "ADJ"])
            Q = ("how to " + Q).split()
            google_url = "https://www.google.com/search?q=" + "+".join(Q)
            youtube_url = "https://www.youtube.com/results?search_query=" + "+".join(Q)
            print("No worries. I found these links for you:")
            print(google_url)
            print(youtube_url)
            default()
        query = [x.replace(" ", "+") for x in query]
        google_url = "https://www.google.com/search?q=" + "+".join(query)
        youtube_url = "https://www.youtube.com/results?search_query=" + "+".join(query)
        print("No worries. I found these links for you:")
        print(google_url)
        print(youtube_url)
        default()


def quit_bot(N, Q):
    print("Alrighty, goodbye!")
    quit()

def thanks(N, Q):
    print("No problem!")
    default()



state = {
    "curr_recipe": None,
    "curr_step": None
}

commands = {
    "walk through a recipe": initiate_recipe,
    "go over ingredients list": show_rcp_ingredients,
    "go over steps": iterate_rcp_steps,
    "go over list of tools": show_rcp_tools,
    "go over list of methods": show_rcp_methods,
    "thanks": thanks,
    "what ingredients are used in this step": show_step_ingredients,
    "what tools are used in this step": show_step_tools,
    "what methods are used in this step": show_step_methods,
    "yes": True,
    "yes please": True,
    "no": False,
    "no thank": False,
    "go to the previous step": previous_step,
    "go to the next step": next_step,
    "go back NUMBER steps": rewind_steps,
    "go forward NUMBER steps": forward_steps,
    "take me to the NUMBER step": jump_to_step, 
    "take me to step NUMBER": jump_to_step,
    "repeat the step": repeat_step,
    "how do i do that": vague_query,
    "how do i QUERY": specific_query,
    "that will be all": quit_bot,
    "goodbye": quit_bot,
    "exit": quit_bot,
    "quit": quit_bot
}

initiate_bot()


