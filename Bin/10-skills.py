#Authored by mostly nick :)
import re

def extract_data(input_file, output_file):
    # Open input file for reading
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    extracted_data = []

    # Define regex pattern to match lines with two numbers
    pattern = r'\["(.+)"\] = "(\d+)\|(\d+)",'

    # Iterate through each line
    for line in lines:
        # Check if the line matches the pattern
        match = re.match(pattern, line.strip())
        if match:
            # Extract the data
            bracketed_word = match.group(1)
            first_number = match.group(2)
            second_number = match.group(3)
            extracted_data.append((bracketed_word, first_number, second_number))

    # Write the extracted data to the output file
    with open(output_file, "w") as output_f:
        for data in extracted_data:
            output_f.write(f"{data[0]}, {data[1]}, {data[2]}\n")

# Paths to input and output files
input_file = "Input/DataStore_Skills.lua"
output_file = "10-skills.txt"

# Call the function to extract data and write to the output file
extract_data(input_file, output_file)