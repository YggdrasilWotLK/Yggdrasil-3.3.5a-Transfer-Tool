import glob
import re
import os

# Define the input and output paths
input_pattern = 'Input/CharSplit/DataStore_Characters_Info_*.txt'
output_file = 'Output/61-MoneyMacro.txt'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Regular expression to match the line with money value
money_regex = re.compile(r'\["money"\]\s*=\s*(\d+),')

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate through each file matching the pattern
    for filename in glob.glob(input_pattern):
        with open(filename, 'r') as infile:
            # Read the content of the file
            for line in infile:
                # Search for the money line
                match = money_regex.search(line)
                if match:
                    # Extract the money number
                    money_number = match.group(1)
                    # Write the formatted line to the output file
                    outfile.write(f'\n.mod money -999999999\n')
                    outfile.write(f'\n.mod money {money_number}\n')
