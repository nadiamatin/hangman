# this project will create a hangman game for users
# it is an extremely simple Python project to get me used to coding
# in Python again as well as to get used to pushing code with Git

import random

def generateRandom():
    words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()
    random_word = random.choice(words)
    return random_word




# main function
def main():
    print("Hello World")  # Press ⌘F8 to toggle the breakpoint.
    print(generateRandom())


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