def recipe(lemons, sugar, ice):
    lemonAmount = {"lemons", 20}
    sugarAmount = {"sugar",20}
    iceAmount = {"ice",20}

    while not lemonAmount["lemons"] < 10 and lemonAmount["lemons"] > 0:
        lemonAmount["lemons"] = int(input("How many lemons do you what in your lemonade (Per Cup of Lemonade)\n"))
        if lemonAmount["lemons"] > 5:
                print("Thats too many!")
        if lemonAmount["lemons"] < 0:
            print("Thats not enough!")
        if lemonAmount["lemons"] > lemons:
            print("You dont have enough lemons for that.")

    while not sugarAmount["sugar"] <= 2 and sugarAmount["sugar"] > 0:
        sugarAmount["sugar"] = int(input("How many cups of sugar do you what in your lemonade (Per Cup of Lemonade)\n"))
        if sugarAmount["sugar"] > 2:
            print("Thats too much!")
        if sugarAmount["sugar"] < 0:
            print("Thats not enough!")
        if sugarAmount["sugar"] > sugar:
            print("You dont have enough sugar for that.")   

    while not iceAmount["ice"] < 20 and iceAmount["ice"] > 0:
        iceAmount["ice"] = int(input("How much ice do you what in your lemonade (Per Cup of Lemonade)\n"))
        if iceAmount["ice"] > 20:
            print("Thats too many!")
        if iceAmount["ice"] < 0:
            print("Thats not enough!")
        if iceAmount["ice"] > ice:
            print("You dont have enough ice for that.")
    return lemonAmount, sugarAmount, iceAmount
