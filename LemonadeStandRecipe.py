def recipe():
    from lemonadeStandShop import lemons, sugar, ice
    lemonAmount = 20
    sugarAmount = 20
    iceAmount = 20


    while not lemonAmount < 10 and lemonAmount > 0:
        lemonAmount = int(input("How many lemons do you what in your lemonade (Per Cup of Lemonade)\n"))
        if lemonAmount > 5:
                print("Thats to many!")
        if lemonAmount < 0:
            print("Thats not enough!")
        if lemonAmount > lemons:
            print("You dont have enough lemons for that.")


    while not sugarAmount <= 2 and sugarAmount > 0:
        sugarAmount = int(input("How many cups of sugar do you what in your lemonade (Per Cup of Lemonade)\n"))
        if sugarAmount > 2:
            print("Thats to much!")
        if sugarAmount < 0:
            print("Thats not enough!")
        if sugarAmount > sugar:
            print("You dont have enough sugar for that.")
        


    while not iceAmount < 20 and iceAmount > 0:
        iceAmount = int(input("How much ice do you what in your lemonade (Per Cup of Lemonade)\n"))
        if iceAmount > 20:
            print("Thats to many!")
        if iceAmount < 0:
            print("Thats not enough!")
        if iceAmount > ice:
            print("You dont have enough ice for that.")
