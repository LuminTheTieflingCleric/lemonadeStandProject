from lemonadeStandCustomers import customerClass, mode, money
from lemonadeStandShop import shop
from lemonadeStandRecipe import recipe
gameLoop = True
mode()

while gameLoop:
    day = 1
    print(f"1 - Shop, 2 - Change Recipe, 3 - Change Price, 4 - Start day {day}")
    option = input("What would you like to do?")
    if option == 1:
        shop()
    if option == 2:
        recipe()
