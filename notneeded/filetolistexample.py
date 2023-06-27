def read_file_to_list(filename):
    wordle_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  # Assuming each line contains a single word
            wordle_list.append(word)
    return wordle_list

wordle_list = read_file_to_list('wordle_list.txt')

print(wordle_list)