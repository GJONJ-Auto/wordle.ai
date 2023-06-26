import json

def convert_to_json(input_file, output_file):
    data = []
    word_id = 1  # Start with word_id = 1
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespace or newline characters
            entry = {'word_id': word_id, 'word': word}
            data.append(entry)
            word_id += 1
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


# Usage example
input_file = 'wordle-nyt-allowed-guesses-update-12546.txt'
output_file = 'wordlelistv2.json'
convert_to_json(input_file, output_file)