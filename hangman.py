import random
from replit import clear

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


hangman_logo = '''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                   '''

###############################################################################

# Step 1
print("WELCOME TO HANGMAN")
print(hangman_logo)

# choose a random word
chosen_word = random.choice(words)

# display _ for every letter in word
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("please pick a letter: ").lower()
    clear()

    if guess in display:
        print("you already guessed this letter. Guess again please.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("wrong. you lost a life. your remaining lives is:", lives)
        print(HANGMANPICS[lives])
        if lives == 0:
            end_of_game = True
            print("you ran out of lives. game over.")

    if "_" not in display:
        end_of_game = True
        print("You win")


