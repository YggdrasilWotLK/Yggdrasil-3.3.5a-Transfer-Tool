#Authored by mostly nick :)
import glob
import re

# Define the input pattern and output file
input_pattern = 'Input/CharSplit/DataStore_Reputations_*.txt'
output_file = '40-ReputationsFiltered.txt'

# Define the regex pattern to match lines with brackets [], = and a number after the =
# The pattern assumes that the number might be surrounded by optional whitespace
line_pattern = re.compile(r'\[\d+\]\s*=\s*\d+')

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over all files matching the input pattern
    for file_path in glob.glob(input_pattern):
        # Open the current input file
        with open(file_path, 'r') as infile:
            # Process each line in the input file
            for line in infile:
                # Check if the line matches the pattern
                if line_pattern.search(line):
                    # Write the matching line to the output file
                    outfile.write(line)
                    

import re

# Define the input and output file names
input_file = '40-ReputationsFiltered.txt'
output_file = '40-ReputationsInput.txt'

# Function to clean a line by removing specific characters and patterns
def clean_line(line):
    # Remove square brackets
    line = line.replace('[', '').replace(']', '')
    # Remove commas
    line = line.replace(',', '')
    # Remove equal signs
    line = line.replace('=', '')
    # Replace double spaces with a single space
    line = re.sub(r'\s{2,}', ' ', line)
    return line

# Open the input file and the output file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Process each line in the input file
    for line in infile:
        cleaned_line = clean_line(line)
        # Write the cleaned line to the output file
        outfile.write(cleaned_line)
