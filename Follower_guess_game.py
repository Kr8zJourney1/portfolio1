### my take on the followers game. ###
print("Welcome to Who has the greater followers!!!\n")

celeb_list = game_data.data


def followers_game():
    lives = 1
    score_count = 0
    choice_a = random.choice(celeb_list)
    choice_b = random.choice(celeb_list)
    while choice_a == choice_b:
        choice_b = random.choice(celeb_list)

    while lives >= 1:
        compare_a = print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        print(art.vs)
        compare_b = print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}\n")

        guess = (input("Who has more followers? Type A or B >")).lower()

        print("\n" * 30)
        print(art.logo)

        compare_a_follow = (choice_a['follower_count'])
        compare_b_follow = (choice_b['follower_count'])


        correct = "a" if compare_a_follow > compare_b_follow else "b"

        """A different way to look at above is below."""
        # if compare_a_follow > compare_b_follow:
        #     correct = "a"
        # else:
        #     correct ="b"

        if guess == correct:
            score_count += 1
            print(f"You scored 1 point. Your total score is {score_count}.\n")

            choice_b = choice_a if correct == "a" else choice_b
            choice_a = random.choice(celeb_list)
          
          """A different way to look at above is below."""
            # if correct == "a":
            #     choice_b = choice_a
            # else:
            #     choice_b = choice_b

            while choice_a == choice_b:
                choice_a = random.choice(celeb_list)


        else:
            print(f"You lose. Your total score is {score_count}.\n")
            lives = 0


play_yes_or_no = input("Would you like to play? type Yes or No. >").lower()
print()
if play_yes_or_no == "no":
    print("Thank you for playing")
    play_game = False

elif play_yes_or_no == "yes":
    followers_game()

# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
