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

def check_guess(guess, target_word):
    correct_letters = []
    incorrect_letters = []
    for letter in range(len(guess)):
        if guess[letter] == target_word[letter]:
            correct_letters.append(guess[letter])
        elif guess[i] in target_word:
            incorrect_letters.append[letter]
    return correct_letters, incorrect_letters