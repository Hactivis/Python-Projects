import random

print("Hi Welcome to the game, This is a muber guessing game.\nYou got 7 chances to guess the number, Let's start the game")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Please Enter your Guess:"))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you foumd it right !! in the {guess_counter} attempt ")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"oops sorry,The number is {number_to_guess} better luck next time")

    elif my_guess > number_to_guess:
        print("Guess is higher")
    elif my_guess > number_to_guess:
        print("Your guess is to high")
    elif my_guess < number_to_guess:
        print("Your guess is lesser")