import random

def guess():
    guess = 0
    lives = 3
    level = 1
    char = 5
    response = ''
    print("\nWelcome to the guessing game!")

    # Generate a random number at the start of the game
    random_number = random.randint(1,char)

    while True:
        guess = get_valid_guess(char)
        
        if guess == random_number:
            level += 1
            print("\nYay you got it")
            print(f"The secret number is {random_number}")

            if char > 100:
                lives += 10
                print(" +10 lives")
            elif char >= 50:
                print(" +5 lives")
            elif char > 40:
                lives += 3
                print(" +4 lives")
            elif char > 20:
                lives += 3
                print(" +3 lives")
            else:
                lives += 2
                print(" +2 life")
            char += 5
            print(f"Total lives: {lives}")
            print(f"\nLevel {level}!")

            # Generate a new random number if the guess was correct
            random_number = random.randint(1,char)

        elif guess > random_number:
            lives -= 1
            print("\nToo high, Try again!")
            print(" -1 life")
            print(f"Total lives: {lives}")

        elif guess < random_number:
            lives -= 1
            print("\nToo low, try again!")
            print(" -1 life")
            print(f"Total lives: {lives}")
            
        if lives == 0:
            print("\nGame over!")
            print(f"The secret number is {random_number}")
            response = get_valid_response()
            if response.lower() == "y":
                lives = 3
                char = 5
                level = 1
                random_number = random.randint(1,char)
                # Generate a new random number if the player wants to play again
            elif response.lower() == "n":
                print("Bye have a good day")
                break

def get_valid_guess(char):
    while True:
        try:
            guess = int(input(f"\nGuess a number between 1 and {char}: "))
        except(ValueError):
            print("Please input a number!")
        else:
            return guess

def get_valid_response():
    while True:
        response = input("\nDo you want to play again? (Y/N): ")
        if response.lower() in ["y", "n"]:
            return response
        else:
            print("Please enter Y/N")

guess()
