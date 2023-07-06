import random
import copy
from node import Node

#wordle_list = ["apple", "table", "chair", "taste", "penny", "racer", "found", "laser", "lazed", "slate"] #This will be where we import the wordle list. Probably should import JSON file.

#This function will run through the wordle list file that we grabbed off of the web that confirms
#how many words there are supposed to be and sort them into a list
def read_file_to_list(filename):
    wordle_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  #Assuming each line contains a single word
            wordle_list.append(Node(word=word))
    return wordle_list

wordle_list = read_file_to_list('wordle_list.txt')

#Check if the word is valid (User input -> wordle list)
def is_valid(word):
    if len(word) != 5:
        return False
    for node in wordle_list:
        if node.word == word:
            return True
    return False

#letter dictionary ranking based on how often users choose them
letter_values = {
    'a': 24, 'b': 9, 'c': 12, 
    'd': 16, 'e': 25, 'f': 6, 
    'g': 10, 'h': 11, 'i': 21, 
    'j': 3, 'k': 8, 'l': 20, 
    'm': 14, 'n': 18, 'o': 23, 
    'p': 13, 'q': 1, 'r': 22, 
    's': 26, 't': 19, 'u': 17, 
    'v': 5, 'w': 7, 'x': 2, 
    'y': 15, 'z': 4
}

#function to calculate the value of a word by numerical letter ranking
def calculate_word_value(word, letter_values):
    value = 0
    prev_letters = []
    for letter in word:
        if letter in letter_values:
            if letter in prev_letters:
                value += letter_values[letter]/2
            else:
                value += letter_values[letter]
                prev_letters.append(letter)
    return value

def add_values_to_word_list(word_list):
    for index in range(len(word_list)):
        word_list[index].value = calculate_word_value(word_list[index].word, letter_values)
    return word_list


#this will read the words from the text file and word_values will be the dictionary
#holding the numerical values calculated for each word
word_file = 'wordle_list.txt'
word_values = {}

with open(word_file, 'r') as file:
    for line in file:
        word = line.strip() #runs through the list word for word
        word_value = calculate_word_value(word, letter_values) 
        word_values[word] = word_value #runs the calculation function and stores words/values
        

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
    word_list = remove_word_from_list(word_list, guess_word)

    for letter_index in range(len(guess_word)):
        # remove words from word list that do not have the correct(green) letter at same specified index 
        if guess_results[letter_index] == 1:
            word_list = [word for word in word_list if word.word[letter_index] == guess_word[letter_index]]
        # remove words from word list that do not contain the letter(yellow)
        # or that do contain letter at same specified index 
        elif guess_results[letter_index] == 2:
            word_list = [word for word in word_list if guess_word[letter_index] in word.word 
                         and guess_word[letter_index] != word.word[letter_index]]
        # guess result == 0, remove words from word list that have too many occurrences of letter(grey)
        else:
            # find number of allowed occurrences of the letter before narrowing down word list
            allowed_occurrences = 0
            chr_occr = find_char_occurences(guess_word, guess_word[letter_index])
            for chr_idx in chr_occr:
                if guess_results[chr_idx] == 1 or guess_results[chr_idx] == 2:
                    allowed_occurrences += 1
            
            word_list = [word for word in word_list if 
                         len(find_char_occurences(word.word, guess_word[letter_index])) <= allowed_occurrences]
    return word_list


def remove_word_from_list(word_list, guess_word):
    new_word_list = []
    for node in word_list:
        if node.word != guess_word:
            new_word_list.append(node)
    return new_word_list

# sorts list of words by value in descending order
def sort_word_list_by_value(word_list):
    sorted_list = sorted(word_list, key=lambda x: x.value, reverse=True)
    return sorted_list

# get list of indexes of occurances of a character in a string
def find_char_occurences(node, chr):
    return [index for index, x in enumerate(node) if chr == x]

# create dictionary to keep track of letter occurences in target word
def get_target_letters(target_word):
    target_letters = {}
    for letter in target_word:
        if letter in target_letters:
            target_letters[letter] += 1
        else:
            target_letters[letter] = 1
    return target_letters

# gets average guesses used by both guessing methods using random samples from wordle list
def compare_guessing_methods(sample_size):
    target_indexes = random.sample(range(len(wordle_list)), sample_size)
    current_target = ""
    random_guesses = 0
    heuristic_search_guesses = 0
    for i in target_indexes:
        current_target = wordle_list[i].word
        random_guesses += auto_solve_wordle(current_target, False, "1")
        heuristic_search_guesses += auto_solve_wordle(current_target, False, "2")
    print("Random Guessing: average guesses used per word was: ", random_guesses/sample_size)
    print("Best First Search Guessing: average guesses used per word was: ", heuristic_search_guesses/sample_size)
    return
    
# Heursitic search goes here
def heuristic_search(check_guess):
    return

# Just to test the play_wordle_ai, this function simply guesses random words
# WILL REMOVE ONCE IMPLEMENTED heurstic_search
def generate_random_word(word_list):
    return random.choice(word_list).word

# automatically selects guesses until target word is found, returns number of turns used
def auto_solve_wordle(target, show_guesses, guess_type):
    current_word_list = copy.deepcopy(wordle_list)
    current_word_list = add_values_to_word_list(current_word_list)
    target_letters = get_target_letters(target)
    target_found = False
    turns = 1
    guess = ""
    guess_results = []

    while not target_found:
          if guess_type == "1":
              guess = generate_random_word(current_word_list)
          elif guess_type == "2":
               current_word_list = sort_word_list_by_value(current_word_list)
               guess = current_word_list[0].word

          guess_results = get_guess_results(guess, target, target_letters)
          if show_guesses:
              print('turn {} guess: {}      Results: {}'.format(turns, guess, guess_results))
          
          if guess == target:
              target_found = True
              if show_guesses:
                  print("Target word found!")
          else:
              current_word_list = remove_invalid_words_from_list(current_word_list, guess, guess_results)
              if turns == 6:
                  if show_guesses:
                    print("Ran out of guesses!")
                  break
              turns += 1
    return turns

def play_wordle_ai():
    again = 'y'
    while again != 'n':
        print("\nWelcome to Wordle AI!")
        print("\nMENU")
        print("-----------------------------------------------------------------")
        print("1: Solve wordle using random guessing")
        print("2: Solve wordle using best-first search guessing")
        print("3: Compare guessing methods from 100 random words")
        print("-----------------------------------------------------------------")
        choice = input ("\nEnter your choice: ")

        if choice == "1" or choice == "2":
            target_word = input("Enter a 5-letter word: ")
            while not is_valid(target_word):
                print("Invalid word. Please try again.")
                target_word = input("Enter a 5-letter word: ")
            auto_solve_wordle(target_word, True, choice)
        elif choice == "3":
            compare_guessing_methods(100)
        else:
            pass
        
        again = input("\nPress 'y' to play again or 'n' to quit: ")
    return
    
# Run
play_wordle_ai()
