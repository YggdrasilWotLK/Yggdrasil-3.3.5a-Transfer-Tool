#Authored by mostly nick :)
import re

# Define the input and output file paths
input_file_path = 'Input/DataStore_Talents.lua'
output_file_path = 'GlyphSpellID.txt'

# Define a regular expression pattern to match 5-digit numbers preceded by a |
pattern = re.compile(r'\|(\d{5})\b')

# Initialize a list to store the extracted 5-digit numbers
five_digit_numbers = []

# Read the input file
with open(input_file_path, 'r') as file:
    content = file.read()

    # Find all 5-digit numbers in the file content preceded by |
    matches = pattern.findall(content)
    five_digit_numbers.extend(matches)

# Write the extracted 5-digit numbers to the output file
with open(output_file_path, 'w') as file:
    for number in five_digit_numbers:
        file.write(number + '\n')

#print(f'Extracted {len(five_digit_numbers)} 5-digit numbers preceded by | and wrote them to {output_file_path}.')
