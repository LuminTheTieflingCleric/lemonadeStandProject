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
price = "You havent assigned a price yet"
while gameLoop:
    day = 1
    print(f"1 - Shop/Decide Difficulty, 2 - Change Recipe, 3 - Change Price, 4 - Start day #{day}, 5 - Settings, 6 - Quit")
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
            print("filler")
        elif option == 5:
            settings = True
            while settings:
                print("1 - View Customer Data, 2 - View Price, 3 - View Inventory, 4 - Go Back")
                option = int(input("What would you like to do?\n"))
                if option == 1:
                    customerClass()
                if option == 2:
                    print(price)
                if option == 3:
                    print(f"Lemons = {round(lemons)}\nIce = {round(ice)}\nSugar = {round(sugar, 1)}")
                if option == 4:
                    settings = False
        elif option == 6:
            gameLoop = False
        else:
            print("Please select valid option...\n")

