import re
import os

# Define the input and output file paths
input_file_path = "Input/DataStore_Characters.lua"
output_file_path = "Output/1-Level.txt"

# Define the pattern to search for the level
pattern = r'\["level"\]\s*=\s*(\d+),'

# Function to extract the level from a line
def extract_level(line):
    match = re.search(pattern, line)
    if match:
        return int(match.group(1))
    else:
        return None

# Check if the input file exists
if os.path.exists(input_file_path):
    # Read input file and extract levels
    levels = []
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            level = extract_level(line)
            if level is not None:
                levels.append(level - 1)

    # Write -80 if level variable exists
    #if level is not None:
    #    with open(output_file_path, 'a') as output_file:
    #        output_file.write(".levelup -80\n")
    # Write levels to output file with ".levelup" prefix
    with open(output_file_path, 'w') as output_file:
        for level in levels:
                #output_file.write(".gm on\n")
                output_file.write(".gm visible off\n")
                output_file.write(".levelup -80\n")
                output_file.write(".levelup " + str(level) + '\n')


    print("Character level set to:", levels[-1] + 1)
else:
    print("ERROR: Level not found! Does DataStore_Characters.lua not exist?", input_file_path)