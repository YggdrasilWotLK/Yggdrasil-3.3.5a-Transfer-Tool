#Authored by mostly nick :)
import sys
import os

# List of input files
input_files = [
    "DataStore_TalentData.lua",            # New file
]

# Create corresponding temp file names
temp_files = ["Input/DataStore_" + file.split("_", 1)[1] for file in input_files]

# Read argument from file
with open("References/Argument.txt", 'r') as arg_file:
    toon = arg_file.read().strip().capitalize()

# Process each file
error_occurred = False  # Flag to track if an error occurred
for input_file, temp_file in zip(input_files, temp_files):
    with open("Raw/" + input_file, 'rb') as f_in, open(temp_file, 'w') as fi_temp:
        p = False
        lines = f_in.readlines()
        for line in lines:
            line = line.decode('utf-8')
            if "Default" in line.strip() and toon in line.strip() or toon in line.strip() and "Default" not in line.strip() and "Guilds" not in line.strip():
                p = True
            if p:
                if "Default" in line.strip() and toon not in line.strip():
                    break
                if "Guilds" in line.strip():
                    break
                fi_temp.write(line)
    
    # Check if the temp file is empty
    if os.stat(temp_file).st_size == 0:
        print(f"Input error in file {input_file}! File is empty! Is it supposed to have contents?")