def recipe():
    lemonAmount = 0
    sugarAmount = 0
    iceAmount = 0


    while not lemonAmount < 5 and lemonAmount > 0:
        try:
            lemonAmount = int(input("How many lemons do you what in your lemonade (Per Cup of Lemonade)"))
        except ValueError:
            print("Please select a valid option")
        if lemonAmount > 5:
            print("Thats to many!")
        if lemonAmount < 0:
            print("Thats not enough!")


    while not sugarAmount <= 2 and sugarAmount > 0:
        try:
            sugarAmount = int(input("How many cups of sugar do you what in your lemonade (Per Cup of Lemonade)"))
        except ValueError:
            print("Please select a valid option")
        if sugarAmount > 2:
            print("Thats to much!")
        if sugarAmount < 0:
            print("Thats not enough!")


    while not iceAmount < 20 and iceAmount > 0:
        try:
            iceAmount = int(input("How much ice do you what in your lemonade (Per Cup of Lemonade)"))
        except ValueError:
            print("Please select a valid option")
        if iceAmount > 20:
            print("Thats to many!")
        if iceAmount < 0:
            print("Thats not enough!")