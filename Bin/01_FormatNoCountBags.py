#Authored by mostly nick :)
import re
import os

# Regex pattern to match numbers of 3-, 4-, or 5-digits
number_pattern = r'\b\d{3,5}\b'

# Input and output file paths
input_file = '1-BagsNoCount.txt'
output_file = 'Output/BagsWithoutCounts.txt'
recipient_file = 'References/Recipient.txt'  # Path to recipient file

# Function to extract numbers from a line
def extract_numbers(line):
    return re.findall(number_pattern, line)

# Function to read player_name from recipient file
def read_player_name(file_path):
    with open(file_path, 'r') as f:
        return f.readline().strip()

# Check if input file exists
if os.path.exists(input_file):
    # Get player_name from recipient file
    player_name = read_player_name(recipient_file)

    # Open input and output files
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Initialize a list to store all extracted numbers
        all_numbers = []

        # Iterate through each line in the input file
        for line in f_in:
            # Check if the line contains "Hitem" or "interface"
            if 'Hitem' in line or 'interface' in line:
                continue  # Skip the line if it contains these words
            
            # Extract numbers from the line
            numbers = extract_numbers(line)
            
            # Add extracted numbers to all_numbers list
            all_numbers.extend(numbers)

        # Ensure all_numbers contains unique numbers in the order they first appeared
        unique_numbers = []
        seen = set()
        for number in all_numbers:
            if number not in seen:
                unique_numbers.append(number)
                seen.add(number)

        # Split unique_numbers into batches of up to 12 numbers
        for i in range(0, len(unique_numbers), 12):
            batch = unique_numbers[i:i+12]
            # Format the output line with .send items {player_name} "Items" "Items"
            output_line = f'.send items {player_name} "Items" "Items" {" ".join(batch)}\n'
            f_out.write(output_line)

    # Delete the input file after processing
    os.remove(input_file)