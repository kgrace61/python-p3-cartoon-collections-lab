list = ["Doc", "Dopey", "Bashful", "Grumpy"]
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def roll_call_dwarves(list):
    for i, name in enumerate(list, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls):
    result = []
    for el in planeteer_calls:
        new_el = el.capitalize() + "!"
        result.append(new_el)
    return result
    

def long_planeteer_calls(call_list):
    less_four = [word for word in call_list if len(word) > 4]
    if less_four:
        return True
    else:
        return False

def find_the_cheese(lst):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in lst:
        if item in cheeses:
            return item
    return None
    #iterate over inputted list
    #see if any elements match any elements in cheeses
    #if not, return None
    #return string value
