from customerClass import customerClass, money
from lemonadeStandShop import shop
from LemonadeStandRecipe import recipe

settings = False
gameLoop = True
money = 0
option = 0
lemons = 0
sugar = 0
ice = 0
day = 0
endless = False
price = "You haven't assigned a price yet"
while gameLoop:
    print("1 - Shop/Decide Difficulty, 2 - Change Recipe, 3 - Change Price, 4 - Start day, 5 - Settings, 6 - Quit")
    try:
        option = int(input("What would you like to do?\n"))
    except ValueError:
        print("Please select a valid option...")
    else:
        if option == 1:
            money, lemons, sugar, ice = shop(money, lemons, sugar, ice)
        elif option == 2:
            recipe(lemons, sugar, ice)
        elif option == 3:
            try:
                price = float(input("What do you want to have the customers pay for your lemonade?"))
                if price > 20:
                    print("Thats too much!") 
                if price < 0.01:
                    print("Thats too little!")
            except ValueError:
                print("Please select a valid option...\n")
        elif option == 4:    
            if price == "You haven't assigned a price yet":
                print(price)
                gameLoop = gameLoop
            else:
                day += 1
                if day == 7:
                    endless = input("You have reached day 7 would you like to continue and proceed playing endless?")
                    if endless == "yes" or "y" or "sure"or "Sure" or "Yes" or "Y":
                        gameLoop = gameLoop
                    elif endless == "no" or "n" or "nope" or "Nope" or "N" or "No":
                        gameLoop = False
                    else:
                        print("Please select a valid option...\n")
                print("filler")

        elif option == 5:
            settings = True
            while settings:
                print("1 - View Price, 2 - View Inventory, 3 - Go Back") # 4 - View Recipe,
                option = input("What would you like to do?\n")
                if option == "1":
                    print(price)
                elif option == "2":
                    print(f"Lemons = {round(lemons)}\nIce = {round(ice)}\nSugar = {round(sugar, 1)}")
                # if option == "4":
                #     print(f"Lemons per Cup = {lemonAmount}\nIce per Cup = {iceAmount}\nSugar per Cup = {sugarAmount}")
                elif option == "3":
                    settings = False
                else:
                    print("Please select valid option...\n")
        elif option == 6:
            gameLoop = False
        else:
            print("Please select valid option...\n")

