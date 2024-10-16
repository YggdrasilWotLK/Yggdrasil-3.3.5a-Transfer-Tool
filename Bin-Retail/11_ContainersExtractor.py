import os
import re

def extract_numbers_from_file(input_file, output_file):
    # Prepare to open the output file
    with open(output_file, 'a') as output_f:
        # Iterate over all input files matching the pattern
        for filename in os.listdir(os.path.dirname(input_file)):
            if filename.startswith("DataStore_Containers_") and filename.endswith(".txt"):
                # Construct full file path
                file_path = os.path.join(os.path.dirname(input_file), filename)

                # Process the file
                with open(file_path, 'r') as input_f:
                    for line in input_f:
                        # Look for lines containing "Hitem:"
                        if "Hitem:" in line:
                            # Use regex to extract the count and itemID
                            match = re.match(r'\[(\d+)\].*Hitem:(\d+):', line)
                            if match:
                                count = match.group(1)
                                itemID = match.group(2)
                                # Extract the character name from the line
                                character_name = re.search(r'\[(.*?)\]', line)
                                character_name = character_name.group(1) if character_name else 'Unknown'
                                # Write the formatted output
                                output_f.write(f'{itemID}:{count} \n')

# Define input and output file paths
input_file_pattern = 'Input/CharSplit/DataStore_Containers_*.txt'
output_file = 'Output/10-ContainersSplit.txt'

# Call the function to extract numbers and write to output file
extract_numbers_from_file(input_file_pattern, output_file)
