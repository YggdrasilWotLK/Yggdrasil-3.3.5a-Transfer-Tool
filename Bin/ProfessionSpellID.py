import re

def extract_numbers(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Read the input file
        content = f_in.read()
        
        # Use regular expressions to find all 3-, 4-, and 5-digit numbers between '|' and '"'
        numbers = re.findall(r'\|(\d{3,5})\"', content)
        
        # Write the numbers to the output file prefixed with ".learn"
        for number in numbers:
            f_out.write(".learn " + number + '\n')

# Input and output file paths
input_file = 'Input/DataStore_Crafts.lua'
output_file = 'Output/ProfessionSpellIDs.txt'

# Call the function to extract numbers
extract_numbers(input_file, output_file)

#print("Extraction completed!")