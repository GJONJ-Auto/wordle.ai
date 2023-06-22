import random

wordle_list = [""] #This will be where we import the wordle list. Probably should import JSON file.

#Check if the word is valid (User input -> wordle list)
def is_valid(word):
    ok = True
    if len(word) == 5 and word in wordle_list:
        return
    else:
        ok = False
    return ok
# This function checks to see if the word that the ai guessed has any correct letters/incorrect.
# NOTE: This function does not know if the letters are guessed correctly but not in the correct spot
# Need to add functionalility that checks that
def check_guess(guess, target_word):
    correct_letters = []
    incorrect_letters = []
    for letter in range(len(guess)):
        if guess[letter] == target_word[letter]:
            correct_letters.append(guess[letter])
        elif guess[i] in target_word:
            incorrect_letters.append[letter]
    return correct_letters, incorrect_letters

# Heursitic search goes here
def heuristic_search():
    return