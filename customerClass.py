money = 0


def game_mode():
    global money
    print("Easy = E, Normal = N, Hard = H")
    difficulty = input("What difficulty do you want to do?\n")
    if difficulty == "E":
        money = 250
    elif difficulty == "N":
        money = 150
    elif difficulty == "H":
        money = 50
    else:
        print("Thats not an option!")
        difficulty = input("What difficulty do you want to do?\n")

def customerClass():
    import random
    day = 1
    # customers = ()
    # print("Easy = E, Normal = N, Hard = H, Sandbox = S")
    customerNames = ["Ben","Jeff","Bob","Sarah","William","Charlotte","John","Charles","Carol","Emma","Grace","Liam","Kayla","Jack","Larry","Amy","Rebecca","Timothy","George","Ben",
                    "Jennifer"]
    # 1st slot Name 2nd slot Sweetness prefrence 3rd slot lemon prefrence 4th slot ice prefrence
    # Bigger = they like it more

    customerChartVisuals = []
    customers = []           # Use when using data
    for _ in range(0,150):
        customersTemporary = [customerNames[random.randint(0,20)],random.randint(5,100),random.randint(5,100),random.randint(5,100),random.randint(1,20)] # Make loop later
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
       # Will make compatible with the rest later
            
        for i3 in customerChartVisuals:
            print(*i3)


