import json

def convert_to_json(input_file, output_file):
    data = []
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespace or newline characters
            entry = {'word': word}
            data.append(entry)
       
    
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


# Usage example
input_file = 'wordle_list.txt'
output_file = 'wordlelistv1.json'
convert_to_json(input_file, output_file)