def recipe_function(money, recipe):

    try:
        recipe["lemons"] = int(input("How many lemons do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["lemons"] > 10:
                print("Thats too many!")
                recipe["lemons"] = 0
        if recipe["lemons"] < 0:
            print("Thats not enough!")
        # if recipe["lemons"] > inventory["lemons"]:
        #     print("You dont have enough lemons for that.")

        recipe["sugar"] = int(input("How many cups of sugar do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["sugar"] > 10:
            print("Thats too much!")
            recipe["sugar"] = 0
        if recipe["sugar"] < 0:
            print("Thats not enough!")
        # if recipe["sugar"] > sugar:
        #     print("You dont have enough sugar for that.")   

        recipe["ice"] = int(input("How much ice do you what in your lemonade (Per Cup of Lemonade)\n"))
        if recipe["ice"] > 20:
            print("Thats too many!")
            recipe["ice"] = 0
        if recipe["ice"] < 0:
            print("Thats not enough!")
        # if recipe["ice"] > ice:
        #     print("You dont have enough ice for that.")
    except ValueError:
         print("Thats not an option!")

