MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
res_water = resources["water"]
res_milk = resources["milk"]
res_coffee = resources["coffee"]

esp_water = (MENU["espresso"]["ingredients"]["water"])
esp_coffee = (MENU["espresso"]["ingredients"]["coffee"])

lat_water = (MENU["latte"]["ingredients"]["water"])
lat_coffee = (MENU["latte"]["ingredients"]["coffee"])
lat_milk = (MENU["latte"]["ingredients"]["milk"])

cap_water =(MENU["cappuccino"]["ingredients"]["water"])
cap_coffee = (MENU["cappuccino"]["ingredients"]["coffee"])
cap_milk = (MENU["cappuccino"]["ingredients"]["milk"])

def espresso():
    if resources["water"]>= MENU["espresso"]["ingredients"]["water"]:
        if resources["coffee"]>= MENU["espresso"]["ingredients"]["coffee"]:
            # if resources["milk"] >= MENU["espresso"]["ingredients"]["milk"]:
                resources["water"] -= esp_water # This subtracts espresso water from resource
                resources["coffee"] -= esp_coffee  # This subtracts espresso coffee from resource

                print("Espresso Made! Enjoy\n")
                print(f"The remaining resources are: {resources}.\n")

def latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                resources["water"] -= lat_water  # This subtracts latte water from resource
                resources["coffee"] -= lat_coffee  # This subtracts latte coffee from resource
                resources["milk"] -= lat_milk  # This subtracts latte milk from resource
                print("Latte is made! Enjoy\n")
                print(f"The remaining resources are: {resources}.\n")

def cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                resources["water"] -= cap_water  # This subtracts latte water from resource
                resources["coffee"] -= cap_coffee  # This subtracts latte coffee from resource
                resources["milk"] -= cap_milk  # This subtracts latte milk from resource
                print("Cappuccino is made! Enjoy\n")
                print(f"The remaining resources are: {resources}.\n")


print("""                                                 .-.       .-.                                                            ___                                 
                                                /    \    /    \                                                         (   )       .-.                      
 ___ .-. .-.    ___  ___      .--.      .--.    | .`. ;   | .`. ;    .--.     .--.      ___ .-. .-.     .---.    .--.     | | .-.   ( __)  ___ .-.     .--.   
(   )   '   \  (   )(   )    /    \    /    \   | |(___)  | |(___)  /    \   /    \    (   )   '   \   / .-, \  /    \    | |/   \  (''") (   )   \   /    \  
 |  .-.  .-. ;  | |  | |    |  .-. ;  |  .-. ;  | |_      | |_     |  .-. ; |  .-. ;    |  .-.  .-. ; (__) ; | |  .-. ;   |  .-. .   | |   |  .-. .  |  .-. ; 
 | |  | |  | |  | |  | |    |  |(___) | |  | | (   __)   (   __)   |  | | | |  | | |    | |  | |  | |   .'`  | |  |(___)  | |  | |   | |   | |  | |  |  | | | 
 | |  | |  | |  | '  | |    |  |      | |  | |  | |       | |      |  |/  | |  |/  |    | |  | |  | |  / .'| | |  |       | |  | |   | |   | |  | |  |  |/  | 
 | |  | |  | |  '  `-' |    |  | ___  | |  | |  | |       | |      |  ' _.' |  ' _.'    | |  | |  | | | /  | | |  | ___   | |  | |   | |   | |  | |  |  ' _.' 
 | |  | |  | |   `.__. |    |  '(   ) | '  | |  | |       | |      |  .'.-. |  .'.-.    | |  | |  | | ; |  ; | |  '(   )  | |  | |   | |   | |  | |  |  .'.-. 
 | |  | |  | |   ___ | |    '  `-' |  '  `-' /  | |       | |      '  `-' / '  `-' /    | |  | |  | | ' `-'  | '  `-' |   | |  | |   | |   | |  | |  '  `-' / 
(___)(___)(___) (   )' |     `.__,'    `.__.'  (___)     (___)      `.__.'   `.__.'    (___)(___)(___)`.__.'_.  `.__,'   (___)(___) (___) (___)(___)  `.__.'  
                 ; `-' '                                                                                                                                      
                  .__.'                                                                                                                                       """)
power_on = True
print(resources)

total_coin_in = 0
insert_coin = 0
esp_cost = 1.50
lat_cost = 2.50
cap_cost = 3.00
accepted_coins = [.05,.10,.25,1.00]
while power_on:
    coin_inserted = False
    while not coin_inserted:
        try:
            coffee_type = input("What would you like?\n Type ES for Espresso.\n Type LT for Latte.\n Type Cap for a Cappuccino.\n :>").lower()
            if coffee_type == "es":
                coins_in = 0
                print(f"{coins_in:.2f} is being returned")
                while coins_in < esp_cost:
                    try:
                        coin = float(input("Coins accepted are: $0.05, $0.10, $0.25.\nAn Espresso is $1.50.\n:>").lower())
                        if coin in accepted_coins:
                            coins_in += coin
                            print(f"Total inserted: ${coins_in:.2f}.")
                        else:
                            print("Invalid coin. Try again.")
                    except ValueError:
                        print("Please enter a valid number.\n")

                if coins_in > esp_cost:
                    change = coins_in - esp_cost
                    print(f"Your change is ${change:.2f}.")
                total_coin_in += coins_in
                print("Your coffee is being made\n")
                print("Enjoy your Espresso.\n")
                espresso()

            elif coffee_type == "lt":
                coins_in = 0
                print(f"{coins_in:.2f} is being returned")
                while coins_in < lat_cost:
                    try:
                        coin = float(input("Coins accepted are: $0.05, $0.10, $0.25.\nA Latte is $2.50.\n:>").lower())
                        if coin in accepted_coins:
                            coins_in += coin
                            print(f"Total inserted: ${coins_in:.2f}.")
                        else:
                            print("Invalid coin. Try again.")
                    except ValueError:
                        print("Please enter a valid number.\n")

                if coins_in > lat_cost:
                    change = coins_in - lat_cost
                    print(f"Your change is ${change:.2f}.")
                total_coin_in += coins_in
                print("Your coffee is being made\n")
                print("Enjoy your Latte.\n")
                latte()

            elif coffee_type == "cap":
                coins_in = 0
                print(f"{coins_in:.2f} is being returned")
                while coins_in < cap_cost:
                    try:
                        coin = float(input("Coins accepted are: $0.05, $0.10, $0.25.\nA Cappuccino is $3.00.\n:>").lower())
                        if coin in accepted_coins:
                            coins_in += coin
                            print(f"Total inserted: ${coins_in:.2f}.")
                        else:
                            print("Invalid coin. Try again.")
                    except ValueError:
                        print("Please enter a valid number.\n")

                if coins_in > cap_cost:
                    change = coins_in - cap_cost
                    print(f"Your change is ${change:.2f}.")
                total_coin_in += coins_in
                print("Your coffee is being made\n")
                print("Enjoy your Cappuccino.\n")
                cappuccino()
                coin_inserted = False
            else:
                print("Invalid. Try again.")
        except ValueError:
            print("Please enter a valid number.\n")



        #     elif insert_coin == 2.5:
        #         coin_inserted = True
        #         print("You purchased a Latte.\n")
        #         latte()
        #
        #     elif insert_coin == 3.0:
        #         coin_inserted = True
        #         print("You purchased a Cappuccino.\n")
        #         cappuccino()
        #
        #     else:
        #         print("Invalid amount. Try again\n")
#         except ValueError:
#             print("Please enter a valid number.\n")
# power_on = False



# money = 0
#     while money <= 1.5:
#         coin = float(input("insert .05, .10 .25"))
#         if coin in [.05, .10, .25]:
#             money += coin
#             print(money)
#             if money > 1.5:
#                 money -= 1.5
#                 print(f"{money:.2f} is being returned")
#         else:
#             print("Invalid coin. Try again.")
#
#     print("Your coffee is being made")
#



        #

        #
        # elif user_input == "resources":
        #     print(resources)
        #
        # else:
        #     print("That was an invalid choice!")


# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# coin_inserted = True
# while coin_inserted:
# TODO: 3. Print report.

# TODO: 4. Check resources sufficient?

# TODO: 5. Process coins.

# TODO: 6. Check transaction successful
