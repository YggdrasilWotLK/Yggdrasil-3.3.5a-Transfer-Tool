#Originally authored by Lortz
#Appended by mostly  nick :)
import sys
import os

# List of input files
input_files = [
    "DataStore_Reputations.lua",
    "DataStore_Currencies.lua",
    "DataStore_Crafts.lua",
    "DataStore_Characters.lua",
    "DataStore_Containers.lua",
    "DataStore_Inventory.lua",
    "DataStore_Pets.lua",
    "DataStore_Quests.lua",
    "DataStore_Achievements.lua",    # New file
    "DataStore_Skills.lua",           # New file
    "DataStore_Spells.lua",           # New file
    "DataStore_Stats.lua",            # New file
    "DataStore_Talents.lua"          # New file
]

# Create corresponding temp file names
temp_files = ["Input/DataStore_" + file.split("_", 1)[1] for file in input_files]

# Read toon from Arguments.txt
arguments_file = "References/Argument.txt"
if not os.path.exists(arguments_file):
    print("Error: Character not specified! Is there no References/Arguments.txt file?")
    sys.exit(1)

with open(arguments_file, 'r') as arg_file:
    toon = arg_file.read().strip()

# Capitalize the first letter of the toon if it's not already capitalized
toon = toon.capitalize()

# Process each file
error_occurred = False  # Flag to track if an error occurred
for input_file, temp_file in zip(input_files, temp_files):
    with open("Raw/" + input_file, 'rb') as f_in, open(temp_file, 'w') as fi_temp:
        p = False
        lines = f_in.readlines()
        for line in lines:
            line = line.decode('utf-8')
            if "Default" in line.strip() and (f'{toon}"]' in line.strip()):
                p = True
            if p:
                if "Default" in line.strip() and (f'{toon}"]' not in line.strip()):
                    break
                if "Guilds" in line.strip():
                    break
                fi_temp.write(line)
    
    # Check if the temp file is empty
    if os.stat(temp_file).st_size == 0:
        print(f"ALERT: File {input_file} is empty! Is it supposed to have contents?")

# Display error message if necessary
