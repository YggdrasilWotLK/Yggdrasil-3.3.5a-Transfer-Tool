import re
import os

def extract_money_numbers(filename):
    money_numbers = []

    # Open the file for reading
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Search for the word "money" in the line
            if 'money' in line.lower():
                # Extract numbers from the line using regular expression
                numbers = re.findall(r'\b\d+\b', line)
                # Add extracted numbers to the list
                money_numbers.extend(numbers)

    return money_numbers

# Input and output file paths
input_filename = 'Input/DataStore_Characters.lua'
output_filename = 'Output/Z-Gold.txt'

# Extract money numbers
money_numbers = extract_money_numbers(input_filename)

# Write the extracted numbers to the output file with the prefix
with open(output_filename, 'w') as outfile:
    for number in money_numbers:
        outfile.write(f".modify money {number}\n")

# Print the count of extracted numbers
print(f"Copper extracted: {number}")