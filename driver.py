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