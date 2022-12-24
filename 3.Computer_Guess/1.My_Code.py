import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print('\nWelcome to "Computer Guess" pick a number from 1 to 10 and the computer will guess it!\n')
    while feedback.lower() != 'c':
        try:
            if low != high:
                guess = random.randint(low, high) # 1: 7; 4: 4;  7: 2
        #   This will happen when theres only 2 number left and the computer wrong
        #   The low and high will be equal 
        #   Ex: The number left will be the current high and low (9,10) the corrrect 9 
        #   if the guess of computer is 10 and we say it's too high
        #   The conditonal statement say high = guess(10) - 1 = 9 low = 9
            else:
                guess = low # could also be high b/c low == high 
                print(f"{guess} is the only option!")
        except(ValueError):
            print(f"{guess} is the only option stop lying!")

        feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)?: ") # 2: h 5: h; 8: h
        # This will update the range of for random guess
        if feedback.lower() == "h":
            high = guess -1 # 3: high = 6; 6: high = 3; 9: high = 2 -1  = 
        elif feedback.lower() == "l":
            low = guess + 1 
    print(f"Yay! The computer guessed your number, {guess}, correctly")

computer_guess(10)