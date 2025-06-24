#Im done with Black Jack!!
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hands2 = random.choices(cards,k=2)
hands1 = random.choices(cards,k=1)
YN = ["y","n"]
user = []
user_score = 0
com = []
com_score = 0
com_choice = random.choice(YN)
play = True
greeting = input("Welcome to Black Jack! Would you like to play? Type Y for yes or N for No >").lower()

if greeting == "n":
    print("Game Ended")

else:
    while play == True:
        deal = input("Would you like a card? type Y for Yes or N for No. >").lower()

        if deal == "y":
            user.extend(hands2)
            user_score = sum(user)
            com.extend(hands1)
            print(f" You have {user}. Your score is {user_score}\n")
            print(f"The dealers first hand is{com}.")
        else:
            print("Game Ended")
        break


    deal = input("Would you like a card? type Y for Yes or N for No. >").lower()
    if deal == "y":
        user.extend(hands1)
        user_score = sum(user)
        if user_score > 21:
            print("You lose!")
            print(f"You have {user}. Your score is {user_score}\n")

    elif deal == "n":
        print(f"You have {user}. Your score is {user_score}\n")
        print(f"The dealers first hand is{com}.")



    if deal == "n":
        nope = True
        while nope:
            com.extend(hands1)
            com_score = sum(com)
            if com_score > 21:
                nope = False
                print("You Win!")
            elif com_choice == "y":
                com.extend(hands1)
                com_score = sum(com)
                if com_score > 21:
                    nope = False
                    print("You Win!")
            elif com_choice == "n":
                if com_score > user_score:
                    nope = False
                    print(f"You lose. Deal has {com_score} and chose to stay.")
                if com_score == user_score:
                    print(f"Its a Draw. Deal has {com_score} and chose to stay.")
                    nope = False
                if com_score < user_score:
                    nope = False
                    print(f"You win. Deal has {com_score} and chose to stay.")
                nope = False
            nope = False
        nope = False

    print("Game has ended")
