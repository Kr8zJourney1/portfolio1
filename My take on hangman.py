####Hangman helped with understanding method and ways to look at while loops*********
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"You have {[lives]} out of 6 lives left.")

    guess = input("Guess a letter: ").lower()


    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print(f"You chose {guess}. That letter is not in the word. You lose a life" )

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"YOU LOSE!! The correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
