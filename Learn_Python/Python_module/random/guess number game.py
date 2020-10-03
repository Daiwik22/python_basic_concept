# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out. 
import random
actual_num=random.randint(1,50)

guess=0
count=0

while guess != actual_num and guess != "exit":
    guess = input("What's your guess?\t")
    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < actual_num:
        print("Too low!")
    elif guess > actual_num:
        print("Too high!")
    else:
        print("Congratulations ! You got it!")
        print("And it only took you", count, "tries!")

print(actual_num)