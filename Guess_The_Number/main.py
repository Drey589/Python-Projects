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
        guess = int(input(f"\nGuess a number between 1 and {char}: "))
        
        if guess == random_number:
            level += 1
            char += 5
            print("\nYay you got it")
            print(f"The secret number is {random_number}")

            if level >= 50:
                lives += 5
                print(" +5 lives")
                print(f"Total lives: {lives}")
            elif level >= 30:
                lives += 3
                print(" +3 lives")
                print(f"Total lives: {lives}")
            elif level >= 10:
                lives += 2
                print(" +2 lives")
                print(f"Total lives: {lives}")
            else:
                lives += 1
                print(" +1 life")
                print(f"Total lives: {lives}")
            print(f"\nLevel {level}!")

            # Generate a new random number if the guess was correct
            random_number = random.randint(1,char)

            continue

        elif guess > random_number:
            lives -= 1
            print("\nToo high, Try again!")
            print(" -1 life")
            print(f"Total lives: {lives}")


        elif guess < random_number:
            lives -= 1
            print("\nToo low, try again!")
            print("\nToo high, Try again!")
            print(" -1 life")
            print(f"Total lives: {lives}")
            
        if lives == 0:
            print("\nGame over!")
            print(f"The secret number is {random_number}")
            while True:
                response = input("\nDo you want to play again? (Y/N): ")
                if response not in (['Y','y','N','n']):
                    print("Please enter Y/N")
                else:
                    break

            if response.lower() == "y":
                lives = 3
                char = 5
                level = 1
                random_number = random.randint(1,char)
                # Generate a new random number if the player wants to play again


                continue
            elif response.lower() == "n":
                print("Bye have a good day")
                break

guess()
