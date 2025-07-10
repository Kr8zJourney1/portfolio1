print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
step_one = input("""You are in a cave and you see two holes. 
Do you jump in the left or right hole? 
Type left or right.\n""").lower()



if step_one == "left":
    print("You jumped...")

    step_two = input("""...in to water. You see light.
Would you swim toward light or would you dive to see whats underwater?
Type light or dive.\n""").lower()

    if step_two == "light":
        print("You swim toward the light and...")

        step_three = input("""you see and swim on to shore. 
There are twhre statues on a chest high piller.
One is a lion, one Bear, and the other is a monkey. 
Type Monkey, Bear or Lion\n""").lower()


        if step_three == "monkey":
            print("""YOU WIN!!! A door opened and leads you to a room of treasure with millions of tons of GOLD!!! "
Now.... how are you going to carry all that GOLD :)  """)
        else:
            print("Game Over!!! You were impailed by spikes.")

    else:print("GAME OVER!!! Upon diving you kicked awake A syren and was eatten")

# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
