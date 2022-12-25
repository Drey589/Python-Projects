"""
Hangman implementation by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random
from words import words
from hangman_visual import lives_visual_dict
import string

# Pick valid random words from the list
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase) # Alphabet is our choices
    used_letters = set()  # what the user has guessed

    lives = 7


    # getting user input
    while len(word_letters) > 0 and lives > 0: # while loop will stop if we guessed the word or if lives == 0
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - - D)
        # For every letter of the word we are guessing 
        # Add to the list if it's in the used_letter
        # else replace with - instead
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        # This prints visuals for every lives left
        print(lives_visual_dict[lives])

        # Prints the words list join with spaces
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        # Adds user_letter to the used letter if it's still not in used_letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # Then checks if it's in word we are guessing
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        # We don't accept if it's alread in the used letter
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        # We don't accept if it's not in the alphabet
        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('\nYAY! You guessed the word', word, '!!\n')




response = ''
if __name__ == '__main__':
    hangman()
while True:
    response = input("Do you want to play again(Y/N) ? ")
    if response.lower() == 'y':
        hangman()
    elif response.lower() == 'n':
        print("Understanble have a nice day!")
        break
    else:
        print("Please input (Y/N)!")
