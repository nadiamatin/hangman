# this project will create a hangman game for users
# it is an extremely simple Python project to get me used to coding
# in Python again as well as to get used to pushing code with Git

import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def generateRandom():
    words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()
    random_word = random.choice(words)
    return random_word

def displayHangman():

    for pic in HANGMAN_PICS:
        print(pic)

def getSpaces(word):
    spaces = ""
    for i in range(len(word)):
        spaces += "_"
    return spaces


# main function
def main():
    random_word = generateRandom()
    print("The length of your word is " + str(len(random_word)) + " letters. Good luck!")
    word_space = getSpaces(random_word)
    print(word_space)
    displayHangman()
#     show first hangman with number of letters displayed
# prompt user for a letter
# if correct, give letter
# if incorrect, say incorrect and push forward the hangman


# create main function
if __name__ == '__main__':
    main()


# TODO: display the length of the word to the user
# TODO: correct_guesses is less than the length of the word
# TODO: prompt the user to guess a letter
# TODO: if the guess is correct increment correct_guesses by 1
# TODO: if the guess is incorrect increment incorrect_guesses by 1
# TODO: and draw the next part of the hangman
# TODO: if the incorrect_guesses is greater than 8, tell the user
# TODO: they lost and exit the program
# TODO: if correct_guesses is equal to the length of the word, tell the user they won