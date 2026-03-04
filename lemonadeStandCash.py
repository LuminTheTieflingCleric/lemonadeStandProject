cash = 0

global firstPass
firstPass = True 

if firstPass:
    print("Easy = e, Normal = n, Hard = h")
    difficulty = input("What difficulty do you want to do?\n")
    if difficulty == "e":
            cash = 250
    elif difficulty == "n":
            cash = 150
    elif difficulty == "h":
            cash = 50
    else:
            print("Thats not an option!")
            difficulty = input("What difficulty do you want to do?\n")
    firstPass = False

print(f"chosen difficulty has this for its starter cash: {cash}")