money = float(0)
lemons = 0
sugar = 0
ice = 0
buyAmount = float(0)
filler = 1

test = float(input("Give how much money?"))   # Temporary
while money == 0:
    money += test


while filler == 1:

    openShop = input("Would you like to open the shop?")
    if openShop == "yes" or "sure":
        openShop = input("Would you like to buy lemons, sugar, or ice?")   # openShop = what to buy
        if openShop == "lemons":                                       # Lemon (10x)
            print("1 pack of 10 Lemons is $1.00 ($1.10 including tax)")
            buyAmount = float(input("How many packs would you like to buy?"))
            if buyAmount * 1.10 >= money:
                print("You dont have enough for that many.")
            else:
                money -= buyAmount * 1.10
                lemons += buyAmount * 10
                money = round(money, 1)
                print("You have $"+str(money)+"0 left and", int(lemons),"lemons.")

        if openShop == "sugar":                                        # Sugar (Per Cup)(5x)
            print("5 cups of Sugar is $1.00 ($1.10 including tax)")
            buyAmount = float(input("How many cups would you like to buy?"))
            if buyAmount * 1.10 >= money:
                print("You dont have enough money for that much.")
            else:
                money -= buyAmount * 1.10
                sugar += buyAmount * 5
                money = round(money, 1)
                print("You have $"+str(money)+"0 left and", int(sugar),"cups of sugar.")
                
        if openShop == "ice":                                          # Ice (12x)(10x)
            print("10 dozen of ice is $1.00 ($1.10 including tax)")
            buyAmount = float(input("How many dozens of ice would you like to buy?"))
            if buyAmount * 1.10 >= money:
                print("You dont have that enough money for that much.")
            else:
                money -= buyAmount * 1.10
                ice += buyAmount * 12 * 10
                money = round(money, 1)
                print("You have $"+str(money)+"0 left and", int(ice),"peices of ice.")
    
    elif openShop == "no":
        print("Ok")
    else:
        print("Thats not an option.")
    filler += 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TEMPORARY (TO GET BENCHMARK 2 TURNED IN
customers = 150
price = 2 # Temporary
for _ in range(customers):
    money += price
    customers -= 1
print(money)