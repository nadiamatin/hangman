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

def generate_random():
    words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()
    random_word = random.choice(words)
    return random_word


def get_spaces(word):
    spaces = ""
    for i in range(len(word)):
        spaces += "_"
    return spaces


def fill_word(spaces, letter, word):
    counter = 0
    newWord = ""
    additions = 0
    for let in word:
        if let == letter:
            newWord += let
            additions += 1
        else:
            newWord += spaces[counter]
        counter += 1
    return [newWord, additions]


def check_letter(word, letter):
    counter = 0
    for let in word:
        if let == letter:
            return counter
        counter += 1
    return -1


# main function
def main():
    randomWord = generate_random()
    word_length = len(randomWord)
    print("The length of your word is " + str(word_length) + " letters. Good luck!")
    wordSpace = get_spaces(randomWord)
    counter = 0
    guessed = []
    guess = ""
    while counter < 6 and word_length != 0:
        print(HANGMAN_PICS[counter])
        print(wordSpace)
        guess = input("Please input a letter:\n")
        while guess in guessed:
            guess = input("Whoops. You've already input that letter. Please try again: \n")
        guessed.append(guess)
        check = check_letter(randomWord, guess)
        if check == -1:
            counter += 1
            if counter == 6:
                print(HANGMAN_PICS[6])
                print("Sorry, you didn't get it this time.")
            else:
                print("Uh oh. Not correct.")
        else:
            info = fill_word(wordSpace, guess, randomWord)
            wordSpace = info[0]
            removed = info[1]
            word_length -= removed
            if word_length != 0:
                print("You got one!")
            else:
                print("Congratulations, you solved it!\n")
    print("The final word was " + randomWord + ".")




# create main function
if __name__ == '__main__':
    main()
