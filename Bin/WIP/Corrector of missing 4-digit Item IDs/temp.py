#Authored by mostly nick :)
import re

def filter_items(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    result = []
    for line in data:
        parts = line.split()
        initial_text = " ".join(parts[:5])  # Retain the initial text (assuming fixed format)
        items = parts[5:]
        filtered_items = [item for item in items if re.match(r'^\d{1,4}:\d+$', item)]
        if filtered_items:
            result.append(initial_text + ' ' + ' '.join(filtered_items))
        else:
            result.append(initial_text)  # Retain the line structure even if no valid items

    # Remove lines that contain no numbers
    result = [line for line in result if re.search(r'\d', line)]

    # Replace "Items" with "Missing items"
    result = [line.replace("Items", "Missing items") for line in result]

    with open(output_file, 'w') as file:
        file.write('\n'.join(result))

# Specify the input and output file paths
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function to filter items and write the output
filter_items(input_file, output_file)
