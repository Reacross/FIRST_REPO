def format_ingredients(items):
    recipe = ""
    count = len(items)
    if count == 1:
        recipe = items[0]
    else:
        for i in range(count):
            item = items[i]
            if i == count - 1:
                recipe += " and "
            elif i > 0: 
                recipe += ", "  
            recipe += item             
    return recipe 