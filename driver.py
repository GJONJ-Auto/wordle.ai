import random

wordle_list = ["apple", "table", "chair"] #This will be where we import the wordle list. Probably should import JSON file.

#Check if the word is valid (User input -> wordle list)
def is_valid(word):
    ok = True
    if len(word) == 5 and word in wordle_list:
        return ok
    else:
        ok = False
    return ok
# This function checks to see if the word that the ai guessed has any correct letters/incorrect.
# NOTE: Incorrect letters is letters that are in the word but not in the correct place.
def check_guess(guess, target_word):
    correct_letters = ['_'] * len(guess)
    valid_letters = []
    invalid_letters =[]

    for index, letter in enumerate(guess):
        if guess[index] == target_word[index]:
            correct_letters[index] = letter
        elif letter in target_word:
            valid_letters.append(letter)
        else:
            invalid_letters.append(letter)
    return correct_letters, valid_letters, invalid_letters

# Heursitic search goes here
def heuristic_search(check_guess):
    return

# Just to test the play_wordle_ai, this function simply guesses random words
# WILL REMOVE ONCE IMPLEMENTED heurstic_search
def generate_random_word():
    return random.choice(wordle_list)

def play_wordle_ai():
    print("Welcome to Wodle AI!")
    target_word = input("Enter a 5-letter word: ")

    while not is_valid(target_word):
        print("Invalid word. Please try again.")
        target_word = input("Enter a 5-letter word: ")
    
    print("Press 'j' to start round 1: ")
    if input() != 'j':
        return
    
    turns = 0
    while turns < 6:
        turns += 1
        print("\nRound", turns)
        #AI guess goes here
        # THIS IS JUST TO TEST
        guess = input()

        print("Word guessed: ",guess)
        correct_letters, valid_letters, invalid_letters = check_guess(guess, target_word)

        print("Letters in the correct spot:", ', '.join(correct_letters))
        print("Letters valid:", ', '.join(valid_letters))
        # Here is where we check to see if the ai guessed not letters correctly i.e letters that 
        # do not appear at all in the word.
        print("Invalid letters:", ', '.join(invalid_letters))

        if guess == target_word:
            print("\nA.I has solved the word!")
            return
        print("\nPress 'j' to startt round " + str(turns + 1) + ":")
        if input() != 'j':
            return
    print("\n A.I ran out of turns!")

# Run
play_wordle_ai()
