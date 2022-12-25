import random
def play():
    tries = 3
    you = 0
    com = 0
    user = ''
    while tries != 0:
        choice = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scisorr"
        }
        computer = random.choice(['r', 'p','s'])
        user = valid_choice(user)
        print(f"\nYou: {choice[user]}\nComputer: {choice[computer]}\n")
        if user == computer:
            print("It's a tie, again")
            continue

        if is_win(user, computer):
            print(f"{choice[user]} won against {choice[computer]}")
            print(f"+1 points for you")
            you += 1
            tries -= 1

        else:
            print(f"{choice[computer]} won against {choice[user]}")
            print(f"+1 points to computer")
            com += 1
            tries -= 1
        print(f"\nTotal points: You: {you}, Computer: {com}")
    if you > com:
        print("\nYou won!")
    elif com > you: 
        print("\nYou loss")
    else:
        print("\nIt's a tie!")

def valid_choice(user):
    while True:
        user = input("\nWhat's your choice? 'r' for rock, 'p' for paper, 's' for scissors\nChoice: ").lower()
        if user in ['r', 'p', 's']:
            return user
        else:
            print("Please input from the choices!")
    
    



def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

play()