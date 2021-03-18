from bot_helpers import *
from RecipeInfo import RecipeInfo
from tabulate import tabulate
import random
from NLP import mostSimilar

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
        p_q = mostSimilar(p_q, [cmd for cmd in commands])[0]
        ans = commands[p_q] if p_q in commands else None
        if isinstance(ans, bool):
            if ans:
                get_recipe()
            else:
                print("Alright, we'll stick with this one.")
                default()

    # Next command
    state["curr_step"] = None
    print(f"Alrighty then, let's work with \"{state['curr_recipe'].name}\".")
    command = input("What do you want to do: go over the ingredients, or go over the recipe steps?\n")
    process_command(command)
    
def get_recipe():
    command = input("Sure thing. Please specify an AllRecipes.com URL:\n")
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
    p_q = mostSimilar(p_q, [cmd for cmd in commands])[0]
    ans = commands[p_q] if p_q in commands else None
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

def quit_bot(N, Q):
    print("Alrighty, goodbye!")
    quit()



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
    # "what ingredients are used in this step": show_step_ingredients,
    # "what tools are used in this step": show_step_tools,
    # "what methods are used in this step": show_step_methods,
    "yes": True,
    "no": False,
    "go to the previous step": previous_step,
    "go to the next step": next_step,
    "go back NUMBER steps": rewind_steps,
    "go forward NUMBER steps": forward_steps,
    "take me to the NUMBER step": jump_to_step, 
    "take me to step NUMBER": jump_to_step,
    # "how do i do that": vague_query,
    # "how do i QUERY": specific_query,
    "that will be all": quit_bot,
    "goodbye": quit_bot
}

initiate_bot()
