import random
day = 1
# customers = ()
# print("Easy = E, Normal = N, Hard = H, Sandbox = S")
customerNames = ["Ben","Jeff","Bob","Sarah","William","Charlotte","John","Charles","Carol","Emma","Grace","Liam","Kayla","Jack","Larry","Amy","Rebecca","Timothy","George","Ben",
                 "Jennifer"]
# 1st slot Name 2nd slot Sweetness prefrence 3rd slot lemon prefrence 4th slot ice prefrence
# Bigger = they like it more

customerChartVisuals = []
customers = []
for i2 in range(0,150):
    customersTemporary = ([customerNames[random.randint(0,20)],random.randint(5,100),random.randint(5,100),random.randint(5,100)]) # Make loop later
            #  ,[customerNames[random.randint(0,20)],random.randint(5,30),random.randint(80,100),random.randint(5,20)]
            #  ,[customerNames[random.randint(0,20)],random.randint(40,60),random.randint(30,45),random.randint(50,70)]," "," ")


    
    catergorize = ["Name = ","Sweetness = ","Tartness = ","Coldness = "]
    filler = []

    
    for i in range(0,4):
        filler.append(catergorize[i]+ str(customersTemporary[i]))
        # customerChartVisuals = filler
        customers.append(customersTemporary)
        if i % 4 == 0:
            customerChartVisuals.append(filler)
while True:        # Will make compatible with the rest later

    filler = input("Would you like to view customer data?")     # Here "filler" = answer for the question
    if filler == "yes":
        for i3 in customerChartVisuals:
            print(*i3)

    elif filler == "no":
        print("Ok")
    else:
        print("Thats not an option")

