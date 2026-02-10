day = 1
def mode():
    global money
    global gameMode
    money = 0
    gameMode = 0
    while gameMode == 0:
        print(gameMode)
        print("Easy - E, Normal - N, Hard - H\n") 
        gameMode = input("What gamemode would you like to play?\n")
        if gameMode == "E":            # This is the only way I could get this to work, or not was not working :[
             money = 250
             break
        elif gameMode == "N":
             money = 150
             break
        elif gameMode == "H":
             money = 50
             break
        else:
            print("Please select a valid option.\n")
            gameMode = 0
    
    print(f"Your starting money is ${money}")
    
# mode()

import random
# day = 1
# customers = ()
# print("Easy = E, Normal = N, Hard = H, Sandbox = S")
def customerClass():
    price = 0
    while type(price) != int:
            try:
                price = int(input("How much do you want the customers to have to pay for your lemonade?"))
            except ValueError:
                print("Please select a valid option")
                

    global customers
    customerNames = ["Ben","Jeff","Bob","Sarah","William","Charlotte","John","Charles","Carol","Emma","Grace","Liam","Kayla","Jack","Larry","Amy","Rebecca","Timothy","George","Ben",
                    "Jennifer"]
    # 1st slot Name 2nd slot Sweetness prefrence 3rd slot lemon prefrence 4th slot ice prefrence
    # Bigger = they like it more

    customerChartVisuals = []
    customers = []
    for i2 in range(0,150):
        customersTemporary = [[customerNames[random.randint(0,20)],random.randint(5,100),random.randint(5,100),random.randint(5,100),random.randint(0,10)]] # Make loop later
                #  ,[customerNames[random.randint(0,20)],random.randint(5,30),random.randint(80,100),random.randint(5,20)]
                #  ,[customerNames[random.randint(0,20)],random.randint(40,60),random.randint(30,45),random.randint(50,70)]," "," ")


        
        catergorize = ["Name = ","Sweetness = ","Tartness = ","Coldness = ","Money = "]
        filler = []

        
        for i in range(0,5):
            filler.append(catergorize[i]+ str(customersTemporary[i]))
            # customerChartVisuals = filler
            customers.append(customersTemporary)
            if i % 5 == 0:
                customerChartVisuals.append(filler)
            
        print("Starting day...")
        if price > catergorize[4]:
            money += 0
           


    filler = input("Would you like to view customer data?")     # Here "filler" = answer for the question
    if filler == "yes":
        for i3 in customerChartVisuals:
            print(*i3)

    elif filler == "no":
        print("Ok")
    else:
        print("Thats not an option")

# customerClass()
# Money ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def customerPayment():
#     price = 0
#     if day == 1:
#         while type(price) != int:
#             try:
#                 price = int(input("How much do you want the customers to have to pay for your lemonade?"))
#             except ValueError:
#                 print("Please select a valid option")

#     startDay = input("Would you like to start the day? (Yes/No)")
#     if startDay == "Yes":
#         print("Starting day...")
#         for _ in range(0, 150):
#             print(customers)
