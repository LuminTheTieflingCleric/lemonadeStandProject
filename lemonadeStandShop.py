#from customerClass import game_mode
# game_mode()
firstPass = True
def shop(money, inventory):
    global firstPass
    if firstPass:
        print("Easy = E, Normal = N, Hard = H")
        difficulty = input("What difficulty do you want to do?\n")
        if difficulty.lower() == "e":
            money = 250
        elif difficulty.lower() == "n":
            money = 150
        elif difficulty.lower() == "h":
            money = 50
        else:
            print("Thats not an option!")
            difficulty = input("What difficulty do you want to do?\n")
        firstPass = False

    buyAmount = float(0)
    

    openShop = input("Would you like to buy lemons, sugar, or ice?\n")   # openShop = what to buy
    if openShop == "lemons":                                       # Lemon (10x)
        print("1 pack of 10 Lemons is $1.00 ($1.10 including tax)")
        buyAmount = float(input("How many packs would you like to buy?\n"))
        if buyAmount * 1.10 >= money:
            print("You dont have enough for that many.")
        else:
            money -= buyAmount * 1.10
            inventory["lemons"] += buyAmount * 10
            money = round(money, 1)
            print("You have $"+str(money)+"0 left and", int(inventory["lemons"]),"lemons.")

    if openShop == "sugar":                                        # Sugar (Per Cup)(5x)
        print("5 cups of Sugar is $1.00 ($1.10 including tax)")
        buyAmount = float(input("How many cups would you like to buy?\n"))
        if buyAmount * 1.10 >= money:
            print("You dont have enough money for that much.")
        else:
            money -= buyAmount * 1.10
            inventory["sugar"] += buyAmount * 5
            money = round(money, 1)
            print("You have $"+str(money)+"0 left and", int(inventory["sugar"]),"cups of sugar.")
                
    if openShop == "ice":                                          # Ice (12x)(10x)
        print("10 dozen of ice is $1.00 ($1.10 including tax)")
        buyAmount = float(input("How many dozens of ice would you like to buy?\n"))
        if buyAmount * 1.10 >= money:
            print("You dont have that enough money for that much.")
        else:
            money -= buyAmount * 1.10
            inventory["ice"] += buyAmount * 12 * 10
            money = round(money, 1)
            print("You have $"+str(money)+"0 left and", int(inventory["ice"]),"peices of ice.")
    return money
