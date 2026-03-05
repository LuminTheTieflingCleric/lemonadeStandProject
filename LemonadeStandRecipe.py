def recipe_function(money, recipe):


    while recipe["lemons"] >= 10 and recipe["lemons"] < 0:
        recipe["lemons"] = int(input("How many lemons do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["lemons"] > 5:
                print("Thats too many!")
        if recipe["lemons"] < 0:
            print("Thats not enough!")
        if recipe["lemons"] > lemons:
            print("You dont have enough lemons for that.")

    while recipe["sugar"] > 2 and recipe["sugar"] < 0:
        recipe["sugar"] = int(input("How many cups of sugar do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["sugar"] > 2:
            print("Thats too much!")
        if recipe["sugar"] < 0:
            print("Thats not enough!")
        if recipe["sugar"] > sugar:
            print("You dont have enough sugar for that.")   

    while recipe["ice"] >= 20 and recipe["ice"] < 0:
        recipe["ice"] = int(input("How much ice do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["ice"] > 20:
            print("Thats too many!")
        if recipe["ice"] < 0:
            print("Thats not enough!")
        if recipe["ice"] > ice:
            print("You dont have enough ice for that.")

