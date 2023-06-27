import random
import copy

#wordle_list = ["apple", "table", "chair", "taste", "penny", "racer", "found", "laser", "lazed", "slate"] #This will be where we import the wordle list. Probably should import JSON file.

#This function will run through the wordle list file that we grabbed off of the web that confirms
#how many words there are supposed to be and sort them into a list
def read_file_to_list(filename):
    wordle_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  #Assuming each line contains a single word
            wordle_list.append(word)
    return wordle_list

wordle_list = read_file_to_list('wordle_list.txt')

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
def check_guess(guess, target_word, correct_letters, valid_letters, invalid_letters):

    for index, letter in enumerate(guess):
        if guess[index] == target_word[index]:
            correct_letters[index] = letter
        elif letter in target_word:
            valid_letters.append(letter)
        else:
            invalid_letters.append(letter)

def get_guess_results(guess, target_word, target_letters):
    t_l = copy.deepcopy(target_letters)
    # list to record results from guess, indexes correspond to guess letter indexes
    # 0 = letter not in target word or no more instances of letter in target word (grey)
    # 1 = letter in target word at same index (green)
    # 2 = letter in target word but in a different index (yellow)
    guess_results = [0,0,0,0,0]
    
    # check for state 1
    for letter in range(len(guess)):
        if guess[letter] == target_word[letter]:
            guess_results[letter] = 1
            t_l[guess[letter]] -= 1
    
    # check for state 2
    for letter in range(len(guess)):
        if (guess_results[letter] == 0) and (guess[letter] in t_l) and (t_l[guess[letter]] >= 1):
            guess_results[letter] = 2
            t_l[guess[letter]] -= 1
    
    # return results of the guess
    return guess_results

def remove_invalid_words_from_list(word_list, guess_word, guess_results):
    word_list.remove(guess_word)
 
    for letter_index in range(len(guess_word)):
        # remove words from word list that do not have the correct(green) letter at same specified index 
        if guess_results[letter_index] == 1:
            word_list = [word for word in word_list if word[letter_index] == guess_word[letter_index]]
        # remove words from word list that do not contain the letter(yellow) or 
        # or that do contain letter at same specified index 
        if guess_results[letter_index] == 2:
            word_list = [word for word in word_list if guess_word[letter_index] in word 
                         and guess_word[letter_index] != word[letter_index]]
    

    return word_list
    

# Heursitic search goes here
def heuristic_search(check_guess):
    return

# Just to test the play_wordle_ai, this function simply guesses random words
# WILL REMOVE ONCE IMPLEMENTED heurstic_search
def generate_random_word(word_list):
    return random.choice(word_list)

def play_wordle_ai():
    current_word_list = wordle_list

    print("Welcome to Wordle AI!")
    target_word = input("Enter a 5-letter word: ")

    while not is_valid(target_word):
        print("Invalid word. Please try again.")
        target_word = input("Enter a 5-letter word: ")

    #create dictionary to keep track of letter occurences in target word
    target_letters = {}
    for letter in target_word:
        if letter in target_letters:
            target_letters[letter] += 1
        else:
            target_letters[letter] = 1
    
    print("Press 'j' to start round 1: ")
    if input() != 'j':
        return
    # Initialize the lists here
    correct_letters = ['_'] * 5
    valid_letters = []
    invalid_letters = []
    turns = 0
    while turns < 6:
        turns += 1
        print("\nRound", turns)
        #AI guess goes here
        # THIS IS JUST TO TEST

        guess = generate_random_word(current_word_list)

        print("Word guessed: ",guess)
        guess_results = get_guess_results(guess, target_word, target_letters)
        print("guess results: ", guess_results)
        print("word list before: ", current_word_list)
        current_word_list = remove_invalid_words_from_list(current_word_list, guess, guess_results)
        print("word list after:  ", current_word_list)

        if guess == target_word:
            print("\nA.I has solved the word!")
            return
        print("\nPress 'j' to start round " + str(turns + 1) + ":")
        if input() != 'j':
            return
    print("\n A.I ran out of turns!")

# Run
play_wordle_ai()
