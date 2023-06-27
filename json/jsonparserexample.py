import json

def parse_json_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error parsing JSON file: {file_path}")

# Example usage
file_path = "wordlelistv2.json"
parsed_data = parse_json_file(file_path)
if parsed_data:
    print(parsed_data)