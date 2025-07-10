logo = """ .-._                           ___                  ,----.                           _,---.                  ,----.    ,-,--.    ,-,--.  
/==/ \  .-._ .--.-. .-.-..-._ .'=.'\    _..---.   ,-.--` , \  .-.,.---.           _.='.'-,  \ .--.-. .-.-. ,-.--` , \ ,-.'-  _\ ,-.'-  _\ 
|==|, \/ /, /==/ -|/=/  /==/ \|==|  | .' .'.-. \ |==|-  _.-` /==/  `   \         /==.'-     //==/ -|/=/  ||==|-  _.-`/==/_ ,_.'/==/_ ,_.' 
|==|-  \|  ||==| ,||=| -|==|,|  / - |/==/- '=' / |==|   `.-.|==|-, .=., |       /==/ -   .-' |==| ,||=| -||==|   `.-.\==\  \   \==\  \    
|==| ,  | -||==|- | =/  |==|  \/  , ||==|-,   ' /==/_ ,    /|==|   '='  /       |==|_   /_,-.|==|- | =/  /==/_ ,    / \==\ -\   \==\ -\   
|==| -   _ ||==|,  \/ - |==|- ,   _ ||==|  .=. \|==|    .-' |==|- ,   .'        |==|  , \_.' )==|,  \/ - |==|    .-'  _\==\ ,\  _\==\ ,\  
|==|  /\ , ||==|-   ,   /==| _ /\   |/==/- '=' ,|==|_  ,`-._|==|_  . ,'.        \==\-  ,    (|==|-   ,   /==|_  ,`-._/==/\/ _ |/==/\/ _ | 
/==/, | |- |/==/ , _  .'/==/  / / , /==|   -   //==/ ,     //==/  /\ ,  )        /==/ _  ,  //==/ , _  .'/==/ ,     /\==\ - , /\==\ - , / 
`--`./  `--``--`..---'  `--`./  `--``-._`.___,' `--`-----`` `--`-`--`--'         `--`------' `--`..---'  `--`-----``  `--`---'  `--`---'  """


import random

guess_list = list(range(1, 101))

print("Welcome to Number Guess!\n")


def easy_game(guess_num):

    easy_lives = 9
    while easy_lives > 0:
        guess = int(input("Guess a number between 1 and 100? >"))

        if guess < guess_num:
            easy_lives -= 1
            print(f"Guess HIGHER. That's not it. You have {easy_lives} lives left.")
            print()

        elif guess > guess_num:
            easy_lives -= 1
            print(f"Guess LOWER. That's not it. You have {easy_lives} lives left.")
            print()

        else:
            print(f"You win {guess_num} was the number.")
            return
    print(f"YOU LOSE. You have {easy_lives} lives left. The number was {guess_num}.")


def hard_game(guess_num):
    hard_lives = 4
    while hard_lives > 0:
        guess = int(input("Guess a number between 1 and 100? >"))

        if guess < guess_num:
            hard_lives -= 1
            print(f"Guess HIGHER. That's not it. You have {hard_lives} lives left.")
            print()

        elif guess > guess_num:
            hard_lives -= 1
            print(f"Guess LOWER. That's not it. You have {hard_lives} lives left.")
            print()

        else:
            print(f"You win {guess_num} was the number.")
            return

    print(f"YOU LOSE. You have {hard_lives} lives left. The number was {guess_num}.")

play_game = True
while play_game:

    yes_or_no = input("Would you like to play? type Yes or No. >").lower()
    print()
    if yes_or_no == "no":
        print("Thank you for playing")
        play_game = False

    elif yes_or_no == "yes":
        easy_or_hard = input("What is your difficulty? Type (E) for Easy or (H) for Hard. >").lower()
        guess_num = random.choice(guess_list)
        print()
        if easy_or_hard == "e":
            easy_game(guess_num)

        elif easy_or_hard == "h":
            hard_game(guess_num)

        else:
            print("Invalid Key. Type E or H")
            print()
    else:
        print("Invalid Key. Type Yes or No")
        print()
# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
