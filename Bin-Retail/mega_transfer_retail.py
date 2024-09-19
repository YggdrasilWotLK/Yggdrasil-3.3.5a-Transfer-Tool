from datetime import datetime
import csv
import glob
import math
import os
import re
import requests
import shutil
import subprocess
import sys


def ensure_folder_exists(folder_path):
    """Creates the folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def delete_folder_contents(folder_path):
    """Deletes all files and subdirectories within the given folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

# Path to the folders to be cleaned
folders_to_clean = ['Input/CharSplit', 'References']

for folder in folders_to_clean:
    ensure_folder_exists(folder)  # Create the folder if it doesn't exist
    delete_folder_contents(folder)

def check_account_structure(root_dir):
    """
    Check if there's an 'Account' subdirectory in RawData,
    and if it exists, ensure it contains a 'SavedVariables' folder.
    """
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item.lower() == 'account':
            # Found an 'Account' folder, now check for 'SavedVariables'
            if 'SavedVariables' not in os.listdir(item_path):
                return False
    return True

def main():
    rawdata = 'RawData'

    if not check_account_structure(rawdata):
        print("ERROR! Erroneous data structure. Check your transfer files! Terminating.")
        input("Press any key to continue...")
        sys.exit()

if __name__ == "__main__":
    main()

def find_file(root_dir, filename):
    """Search for a file with the specified name in the given directory and its subdirectories."""
    for dirpath, _, files in os.walk(root_dir):
        if filename in files:
            return True
    return False

def find_account_folder(root_dir):
    """Recursively search for an 'Account' folder in the given directory and its subdirectories."""
    for dirpath, dirs, _ in os.walk(root_dir):
        if 'Account' in dirs:
            return os.path.join(dirpath, 'Account')
    return None

def list_directories(root_dir):
    """List all directories in the specified root directory, excluding 'SavedVariables'."""
    return [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d != 'SavedVariables']

def copy_lua_files(src_dir, dest_dir):
    """Copy only .lua files from the source directory to the destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for filename in os.listdir(src_dir):
        if filename.endswith('.lua'):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
                
def delete_non_lua_files(directory):
    """Delete all files that are not .lua files in the specified directory, and delete WTF folder if it exists."""
    # Delete non-.lua files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and not filename.endswith('.lua'):
            os.remove(file_path)
    
    # Delete WTF folder if it exists
    wtf_folder = os.path.join(directory, 'WTF')
    if os.path.exists(wtf_folder) and os.path.isdir(wtf_folder):
        shutil.rmtree(wtf_folder)

def main():
    rawdata = 'RawData'
    search_file = 'Blizzard_GlueSavedVariables.lua'

    # Check if RawData only has one subdirectory named 'Split'
    subdirs = [d for d in os.listdir(rawdata) if os.path.isdir(os.path.join(rawdata, d))]
    if len(subdirs) == 1 and subdirs[0] == 'Split':
        print("Account processing complete. Has tool already been run for these files? Attempting to proceed to character selection.")
        print("")
        return

    if find_file(rawdata, search_file):
        account_folder_path = find_account_folder(rawdata)
        
        if account_folder_path:
            directories = list_directories(account_folder_path)
            
            if not directories:
                print("No account folders found.")
                return
            
            print("Welcome to Yggdrasil's retail to WotLK 3.3.5a toon transfer utility!")
            print("")
            print("Account-based structure identified! Please select account by number:")
            for i, folder in enumerate(directories, start=1):
                print(f"{i}. {folder}")
            
            while True:
                try:
                    choice = int(input("Enter account number: "))
                    if 1 <= choice <= len(directories):
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            selected_folder = directories[choice - 1]
            print(f"You selected: {selected_folder}")
            
            # Copy .lua files from selected account's SavedVariables to RawData
            src_dir = os.path.join(account_folder_path, selected_folder, 'SavedVariables')
            copy_lua_files(src_dir, rawdata)
            
            # Delete all non-.lua files in RawData
            delete_non_lua_files(rawdata)
            
        else:
            print(f"ERROR: Account folder not found! Check your transfer files!")
            input("Press any key to continue...")
            sys.exit()
    else:
        print(f"ERROR: Couldn't identify retail files! Check your transfer files!")
        input("Press any key to continue...")
        sys.exit()

if __name__ == "__main__":
    main()

def find_lua_files_or_wtf(directory):
    """Check for .lua files or WTF folder in the specified directory."""
    for root, dirs, files in os.walk(directory):
        if 'WTF' in dirs:
            return True
        for file in files:
            if file.endswith('.lua'):
                return True
    return False

def find_file(root_dir, filename):
    """Search for a file with the specified name in the given directory and its subdirectories."""
    for dirpath, _, files in os.walk(root_dir):
        if filename in files:
            return dirpath
    return None

def find_account_folder(root_dir):
    """Recursively search for an 'Account' folder in the given directory and its subdirectories."""
    for dirpath, dirs, _ in os.walk(root_dir):
        if 'Account' in dirs:
            return os.path.join(dirpath, 'Account')
    return None

def list_directories(root_dir):
    """List all directories in the specified root directory, excluding 'SavedVariables'."""
    return [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d != 'SavedVariables']

def copy_files(src_dir, dest_dir):
    """Copy all files from the source directory to the destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)
    print(f"Files copied from {src_dir} to {dest_dir}")

def main():
    rawdata = 'RawData'  # Current directory's RawData folder
    parent_rawdata = '../RawData'  # Parent directory's RawData folder
    search_file = 'Blizzard_GlueSavedVariables.lua'


    if not find_lua_files_or_wtf(rawdata):
        
        file_location = find_file(parent_rawdata, search_file)
        
        if file_location:
            
            account_folder_path = find_account_folder(parent_rawdata)
            
            if account_folder_path:
                print("Account-based structure found! Please select a retail account.")
                directories = list_directories(account_folder_path)
                
                if not directories:
                    print("ERROR: No account folders found.")
                    return
                
                for i, folder in enumerate(directories, start=1):
                    print(f"{i}. {folder}")
                
                while True:
                    try:
                        choice = int(input("Enter account number: "))
                        if 1 <= choice <= len(directories):
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                
                selected_folder = directories[choice - 1]
                print(f"You selected: {selected_folder}")
                
                # Copy files from selected account's SavedVariables to current RawData
                src_dir = os.path.join(account_folder_path, selected_folder, 'SavedVariables')
                dest_dir = rawdata
                copy_files(src_dir, dest_dir)
                
            else:
                print(f"Account folder not found in {parent_rawdata}. Check your transfer files!")
                sys.exit()
        else:
            print(f"ERROR: {search_file} not found in {parent_rawdata}. Check your transfer files!")
            sys.exit()

if __name__ == "__main__":
    main()

def parse_characters(file_path):
    characters = {}
    character_list = []
    within_character_ids = False

    with open(file_path, 'r') as file:
        for line in file:
            # Check if we're entering the DataStore_CharacterIDs section
            if 'DataStore_CharacterIDs = {' in line:
                within_character_ids = True
                continue

            # Check if we're leaving the DataStore_CharacterIDs section
            if within_character_ids and '}' in line:
                within_character_ids = False
                continue

            # If within the DataStore_CharacterIDs section, extract the characters
            if within_character_ids:
                match = re.match(r'\["(Default\..*?)"\] = (\d+),', line)
                if match:
                    character_name = match.group(1)
                    bracket_number = int(match.group(2))
                    characters[character_name] = bracket_number
                    character_list.append(character_name)

    return characters, character_list

def select_character_and_store_bracket(file_path):
    # Parse the characters from the file
    characters, character_list = parse_characters(file_path)

    # Save the character count to "References/1-CharCount.txt"
    char_count_path = "References/1-CharCount.txt"
    char_count_dir = os.path.dirname(char_count_path)
    os.makedirs(char_count_dir, exist_ok=True)
    
    with open(char_count_path, "w") as file:
        file.write(f"{len(character_list)}\n")

    # Display the available characters with realm and character name separately
    if character_list:
        while True:
            print("Select character and realm: ")
            for index, character in enumerate(character_list, start=1):
                realm_name, char_name = character.split('.')[1:]
                print(f"{index}. Realm: {realm_name}. Character: {char_name}")

            # Prompt user for selection
            try:
                selection = int(input("\nEnter number of character and realm: "))
                
                # Validate selection
                if 1 <= selection <= len(character_list):
                    selected_character = character_list[selection - 1]
                    bracket_number = characters[selected_character]
                    realm_name, char_name = selected_character.split('.')[1:]

                    # Write the bracket number to "References/1-Selection.txt"
                    selection_path = "References/1-Selection.txt"
                    selection_dir = os.path.dirname(selection_path)
                    os.makedirs(selection_dir, exist_ok=True)

                    with open(selection_path, "w") as file:
                        file.write(f"{bracket_number}\n")

                    # Write the character name to "References/2-RetailChar.txt"
                    char_name_path = "References/2-RetailChar.txt"
                    with open(char_name_path, "w") as file:
                        file.write(f"{char_name}\n")

                    # Write the realm name to "References/3-Realm.txt"
                    realm_name_path = "References/3-Realm.txt"
                    with open(realm_name_path, "w") as file:
                        file.write(f"{realm_name}\n")

                    # Prompt user for region
                    while True:
                        region = input("Enter region (US, EU, TW): ").strip().upper()
                        if region in {'US', 'EU', 'TW'}:
                            # Write the region to "References/4-Region.txt"
                            region_path = "References/4-Region.txt"
                            with open(region_path, "w") as file:
                                file.write(f"{region}\n")

                            print(f"Continuing with '{char_name}' in realm '{realm_name}' for region '{region}'.")
                            break
                        else:
                            print("Invalid region. Please enter US, EU, or TW.")
                    
                    break
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print(" ")
                print("Invalid input. Please enter a number.")
                print(" ")
    else:
        print("No characters found.")

# Run the function
if __name__ == "__main__":
    # Specify the path to your DataStore.lua file
    file_path = "RawData/DataStore.lua"
    select_character_and_store_bracket(file_path)


def find_top_level_brackets(text, start_line_num):
    lines = text.split('\n')
    brackets = []
    depth = 0
    ignore_next = True  # To ignore the first opening bracket
    for line_num, line in enumerate(lines, start=start_line_num):
        line = line.strip()
        for col_num, char in enumerate(line, start=1):
            if char == '{':
                if depth == 1 and not ignore_next:
                    brackets.append((line_num, col_num))
                depth += 1
                ignore_next = False
            elif char == '}':
                depth -= 1
    return brackets

def process_input(input_text, filename):
    sections = re.split(r'(\w+)\s*=\s*{', input_text)[1:]
    results = {}
    line_num = 1
    for i in range(0, len(sections), 2):
        section_name = sections[i]
        section_content = '{' + sections[i+1]  # Add back the opening brace
        section_line_num = line_num
        line_num += section_content.count('\n') + 1
        results[section_name] = {
            'line_num': section_line_num,
            'brackets': find_top_level_brackets(section_content, section_line_num)
        }
    return results

# Find all files matching the pattern
file_pattern = 'RawData/DataStore_*.lua'
files = glob.glob(file_pattern)

# Open the output file for writing
with open('References/2-Sections.txt', 'w') as output_file:
    for filename in files:
        # Read input from file
        with open(filename, 'r') as file:
            input_text = file.read()

        results = process_input(input_text, filename)

        # Write the results to the output file
        output_file.write(f"{filename}\n\n")
        for name, data in results.items():
            output_file.write(f"Section '{name}' (Line {data['line_num']}):\n")
            for line_num, col_num in data['brackets']:
                output_file.write(f"    Line {line_num}\n")
        output_file.write('\n')


def extract_sections(section_file):
    with open(section_file, 'r') as f:
        lines = f.readlines()

    section_dict = {}
    current_file = None
    current_section = None

    for line in lines:
        line = line.strip()
        if line.endswith('.lua'):
            current_file = line
        elif line.startswith('Section'):
            current_section = line.split("'")[1]
            section_dict[(current_file, current_section)] = []
        elif line.startswith('Line'):
            section_dict[(current_file, current_section)].append(int(line.split(' ')[1]))

    for (data_file, section), lines in section_dict.items():
        if not os.path.exists(data_file):
            print(f"File {data_file} does not exist. Skipping...")
            continue

        with open(data_file, 'r') as f:
            data = f.readlines()

        # Ensure that there's an entry for lines not just between but after the last line.
        lines.append(len(data) + 1)

        for i in range(len(lines) - 1):
            start = lines[i] - 1
            end = lines[i + 1] - 1
            with open(f'{section}_{i+1}.txt', 'w') as f:
                f.write(''.join(data[start:end]))

        # Make sure to handle the very last range correctly
        if len(lines) > 1:
            start = lines[-2] - 1
            end = len(data)
            with open(f'{section}_{len(lines) - 1}.txt', 'w') as f:
                f.write(''.join(data[start:end]))

# Replace 'References/2-Sections.txt' with the path to your section file
extract_sections('References/2-Sections.txt')


# Define the source and destination directories
source_dir = '.'
destination_dir = 'RawData/Split/'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Loop through the files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        # Construct full file paths
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.move(source_file, destination_file)
        #print(f"Moved: {filename}")

#print("All .txt files have been moved.")

def read_number_from_file(filepath):
    """Reads a single integer from a text file."""
    with open(filepath, 'r') as file:
        number = file.read().strip()
        return int(number)  # Convert the read string to an integer

def copy_files_with_number(src_dir, dest_dir, number):
    """Copies files from src_dir to dest_dir that contain the specified number in their filenames."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # Create destination directory if it doesn't exist

    for filename in os.listdir(src_dir):
        if str(number) in filename:
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.copy(src_file, dest_file)
            #print(f'Copied: {filename}')

def main():
    # Paths to the files and directories
    selection_file = 'References/1-Selection.txt'
    source_directory = 'RawData/Split'
    destination_directory = 'Input/CharSplit'

    # Read the number from the file
    number = read_number_from_file(selection_file)
    
    # Copy files that contain the number in their filename
    copy_files_with_number(source_directory, destination_directory, number)

if __name__ == "__main__":
    main()


# Prompt the user for input
print("")
character_name = input("Enter name of new character on Yggdrasil, if not same as on old server: ")

# Specify the file paths
argument_file = "References/2-RetailChar.txt"
recipient_file = "References/1-Recipient.txt"

if character_name:
    # User provided input, write it to Recipient.txt
    with open(recipient_file, 'w') as file:
        file.write(character_name)
    print(f"Character name '{character_name}' has been saved as recipient.")
else:
    # No input provided, copy contents of Argument.txt to Recipient.txt
    try:
        with open(argument_file, 'r') as src, open(recipient_file, 'w') as dest:
            dest.write(src.read())
        print(f"Continuing with same name as on old server.")
    except FileNotFoundError:
        print(f"CRITICAL ERROR: Cached character file(s) not found, terminating!")
        selection = input("")
        parent_pid = os.getppid()  # Get the parent process ID
        os.kill(parent_pid, 9)  # Send SIGKILL signal to the parent


# Define the directory and file patterns
directory = 'Input/CharSplit'
old_pattern = 'DataStore_Inventory_Characters_*.txt'
new_prefix = 'DataStore_Containers_Inventory_Characters_'

# Construct the old file pattern path
old_pattern_path = os.path.join(directory, old_pattern)

# Find all files matching the old pattern
files_to_rename = glob.glob(old_pattern_path)

# Iterate through each file and rename
for old_file in files_to_rename:
    # Construct the new file name
    old_filename = os.path.basename(old_file)
    new_filename = new_prefix + old_filename[len('DataStore_Inventory_Characters_'):]
    
    # Construct full paths for old and new files
    old_file_path = old_file
    new_file_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    #print(f'Renamed: {old_file_path} -> {new_file_path}')


def extract_item_numbers(input_files_pattern, output_file_path):
    # Compile a regex pattern to match lines containing 'Hitem:' and extract the item number
    item_pattern = re.compile(r'Hitem:(\d+)', re.IGNORECASE)
    
    # Open the output file in append mode
    with open(output_file_path, 'a') as output_file:
        # Loop over all files matching the input pattern
        for file_path in glob.glob(input_files_pattern):
            #print(f"Processing file: {file_path}")
            
            # Open each file and process lines
            with open(file_path, 'r') as file:
                for line in file:
                    # Check if the line contains 'Hitem:' and does not start with a number
                    if 'Hitem:' in line and not re.match(r'^\[\d+\]', line):
                        # Search for the item number in the line
                        match = item_pattern.search(line)
                        if match:
                            item_number = match.group(1)
                            # Append the item number to the output file
                            output_file.write(f"{item_number}:1\n")

if __name__ == "__main__":
    # Define the input file pattern and output file path
    input_files_pattern = "Input/CharSplit/DataStore_Containers_*.txt"
    output_file_path = "Output/10-ContainersSplit.txt"
    
    # Call the function to process the files and extract item numbers
    extract_item_numbers(input_files_pattern, output_file_path)
    print("Processing complete.")


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

# Open the input file for reading
with open('Output/10-ContainersSplit.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Open the output file for writing
with open('Output/11-ContainersFiltered.txt', 'w') as file:
    # Define the set of numbers to filter out
    exclude_numbers = {'6948', '44810', '44430', '43824', '43348', '40643', '49054', '49052', '43349', '43300'}
    
    # Iterate over each line
    for line in lines:
        # Split the line into number and value
        number, value = line.split(':')
        
        # Check if the number should be excluded
        if int(number) > 56806 or number in exclude_numbers:
            # If it does, skip this line
            continue
        
        # If it doesn't, write the line to the output file
        file.write(line)

# Open the filtered file for processing
with open('Output/11-ContainersFiltered.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    
# Split the data into units
units = data.split()

# Introduce new line shifts after each 12 units
data = '\n'.join([' '.join(units[i:i+12]) for i in range(0, len(units), 12)])

# Write the data back to the file
with open('Output/11-ContainersFiltered.txt', 'w') as file:
    file.write(data)

# Open the file to add the macro commands
with open('Output/11-ContainersFiltered.txt', 'r') as file:
    with open('Output/11-ContainersMacro.txt', 'w') as file_modified:
        # Read each line from the input file
        for line in file:
            # Prepend the desired string to the beginning of the line
            modified_line = '.send items Charactername "Items" "Items" ' + line
            # Write the modified line to the output file
            file_modified.write(modified_line)


# Delete the input files
os.remove('Output/10-ContainersSplit.txt')
os.remove('Output/11-ContainersFiltered.txt')


# List of achievement IDs to search for
achievement_ids = [6, 7, 8, 9, 10, 14782, 11, 14783, 12, 15805, 13, 19459, 4826, 6193, 9060, 10671, 12544]

# Regular expression pattern to match achievement IDs and completion dates
pattern = r'\[(\d+)\] = (\d+),'

# List to store the results
results = []

# Loop through all files in the Input/CharSplit directory that match the pattern
for filename in glob.glob('Input/CharSplit/DataStore_Achievements_Characters_*.txt'):
    with open(filename, 'r') as f:
        # Loop through each line in the file
        for line in f:
            # Search for the pattern in the line
            match = re.search(pattern, line)
            if match:
                # Extract the achievement ID and completion date
                achievement_id = int(match.group(1))
                completion_date = match.group(2)
                # If the achievement ID is in the list of IDs we're looking for, add it to the results list
                if achievement_id in achievement_ids:
                    results.append(f'{achievement_id}:{completion_date}')

# Write the results to the output file
with open('Output/20-ExpacAchis.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')


# Define the time spans for each expansion
expansions = {
    "Vanilla": ("01/01/2007", "15/01/2007"),
    "The Burning Crusade": ("16/01/2007", "12/11/2008"),
    "The Wrath of the Lich King": ("13/11/2008", "06/12/2010"),
    "Cataclysm": ("07/12/2010", "24/09/2012"),
    "Mists of Pandaria": ("25/09/2012", "12/11/2014"),
    "Warlords of Draenor": ("13/11/2014", "29/08/2016"),
    "Legion": ("30/08/2016", "13/08/2018"),
    "Battle for Azeroth": ("14/08/2018", "26/10/2020"),
    "Shadowlands": ("27/10/2020", "27/11/2022"),
    "Dragonflight": ("28/11/2022", "23/08/2024"),
    "The War Within": ("24/08/2024", "31/12/9999")
}

# Define the achievements and their corresponding expansions
achievement_expansions = {
    6: "Vanilla",
    7: "Vanilla",
    8: "Vanilla",
    9: "Vanilla",
    10: "Vanilla",
    11: "Vanilla",
    12: "The Burning Crusade",
    13: "The Wrath of the Lich King",
    4826: "Cataclysm",
    6193: "Mists of Pandaria",
    9060: "Warlords of Draenor",
    10671: "Legion",
    12544: "Battle for Azeroth",
    14783: "Shadowlands",
    15805: "Dragonflight",
    19459: "The War Within"
}

# Read the achievements from the file
achievements = {}
with open("Output/20-ExpacAchis.txt", "r") as file:
    for line in file:
        # Split the line on ":" to separate ID and date parts
        ach_id_str, date_str = line.split(":")
        
        # Strip any extra whitespace and convert to integers
        ach_id = int(ach_id_str.strip())
        date = int(date_str.strip())
        
        # Convert the date from yymmdd to a datetime object
        achievements[ach_id] = datetime.strptime(str(date), "%y%m%d")

# Flag to check if at least one achievement is valid
any_valid_achievement = False

# Check the completion date for each achievement and validate it against the corresponding expansion
for ach_id, date in achievements.items():
    exp_name = achievement_expansions.get(ach_id)
    
    if exp_name:
        start, end = expansions[exp_name]
        start_date = datetime.strptime(start, "%d/%m/%Y")
        end_date = datetime.strptime(end, "%d/%m/%Y")
        
        if not any_valid_achievement and start_date <= date <= end_date:
            print(f"Max level achievement ID {ach_id} from retail {exp_name} found! Max level achieved, setting toon level to 80.")
            any_valid_achievement = True
    else:
        print(f"Achievement ID {ach_id} not found in the expansions list.")

# Write to file if at least one achievement is valid
if any_valid_achievement:
    with open("References/5-MaxLevel.txt", "w") as file:
        file.write("79")


# Define the file path
file_path = 'Output/20-ExpacAchis.txt'

# Check if the file exists
if os.path.isfile(file_path):
    try:
        # Delete the file
        os.remove(file_path)
        #print(f"The file '{file_path}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")
else:
    print(f"The file '{file_path}' does not exist.")

# Define the file patterns and output file
input_pattern = 'Input/CharSplit/DataStore_Achievements_Characters_*.txt'
output_file = 'Output/22-AchievementMacro.txt'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

def extract_numbers_from_line(line):
    # Use regular expressions to find numbers within square brackets
    return re.findall(r'\[(\d+)\]', line)

def process_file(file_path):
    with open(file_path, 'r') as file:
        in_dates_section = False
        numbers = []
        
        for line in file:
            if '["CompletionDates"] = {' in line:
                in_dates_section = True
                continue
            
            if in_dates_section:
                if '}' in line:
                    break  # Stop reading when we reach the closing brace
                
                # Extract numbers from the current line
                numbers.extend(extract_numbers_from_line(line))
    
    return numbers

def write_numbers_to_file(numbers, output_path):
    with open(output_path, 'w') as file:
        for number in numbers:
            file.write(f'.achievement add {number}\n')

def main():
    # Find the input file
    input_files = glob.glob(input_pattern)
    if not input_files:
        print(f'No files found matching pattern: {input_pattern}')
        return

    # Process each file and extract numbers
    all_numbers = []
    for input_file in input_files:
        #print(f'Processing file: {input_file}')
        numbers = process_file(input_file)
        all_numbers.extend(numbers)
    
    # Write the numbers to the output file
    if all_numbers:
        write_numbers_to_file(all_numbers, output_file)
        #print(f'Numbers written to {output_file}')
    else:
        print('No numbers found to write.')

if __name__ == '__main__':
    main()


# Define file paths
input_file_pattern = 'Input/CharSplit/DataStore_Quests_History_*.txt'
output_file_path = '30-QuestTemp.txt'

# Regular expression to find lines with numbers
number_pattern = re.compile(r'\d+(\.\d+)?([eE][+-]?\d+)?')

def process_file(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            if number_pattern.search(line) and '"' not in line:
                # Write the line to the output file
                outfile.write(line)

def remove_commas(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Replace all commas with an empty string
    modified_content = content.replace(',', '')

    # Open the file for writing (this will overwrite the file)
    with open(file_path, 'w') as file:
        # Write the modified content back to the file
        file.write(modified_content)

if __name__ == '__main__':
    # Process all files matching the pattern
    for input_file_path in glob.glob(input_file_pattern):
        #print(f"Processing file: {input_file_path}")
        process_file(input_file_path, output_file_path)
    
    # Remove commas from the output file
    remove_commas(output_file_path)
    #print(f"Lines containing numbers and not containing quotes have been copied to {output_file_path}, and commas have been removed.")


# Helper function to convert bitfield to quest IDs
def decode_quest_ids(bitfield, base_index):
    quest_ids = []
    for bit_pos in range(64):
        if bitfield & (1 << bit_pos):
            quest_ids.append(bit_pos + 64 * base_index)
    return quest_ids

def parse_value(value):
    try:
        # Handle scientific notation and regular integers
        return int(float(value))
    except ValueError:
        # Return None if conversion fails
        return None

def main():
    # Read the file
    with open('30-QuestTemp.txt', 'r') as file:
        lines = file.readlines()
    
    # Parse the file content into a dictionary
    quest_data = {}
    for line in lines:
        line = line.strip()
        if line:
            # Process lines with index = bitfield format only
            if '=' in line:
                # Extract index and bitfield using regex
                match = re.match(r'\[(\d+)\] = ([\d.e+]+)', line)
                if match:
                    index = int(match.group(1))
                    value = match.group(2)
                    bitfield = parse_value(value)
                    if bitfield is not None:
                        quest_data[index] = bitfield

    # Write output to file
    with open('31-QuestIndexID.txt', 'w') as outfile:
        for index, bitfield in sorted(quest_data.items()):
            quest_ids = decode_quest_ids(bitfield, index)
            #outfile.write(f"Index {index}: {quest_ids}\n")
            outfile.write(f"{quest_ids}\n")

if __name__ == "__main__":
    main()

# Define the filename
filename = '31-QuestIndexID.txt'

# Read the content from the file
with open(filename, 'r') as file:
    content = file.read()

# Remove all square brackets
content = content.replace('[', '')
content = content.replace(']', '')

# Replace all commas with line breaks
content = content.replace(',', '\n')

# Split the content into lines and strip both leading and trailing spaces
lines = content.splitlines()
lines = [line.strip() for line in lines]

# Join the lines back into a single string with newline characters
processed_content = '\n'.join(lines)

# Write the modified content back to the file
with open(filename, 'w') as file:
    file.write(processed_content)


# Function to decode quest IDs from a bitfield
def decode_quest_ids(bitfield, base_index):
    quest_ids = []
    for bit_pos in range(64):
        if bitfield & (1 << bit_pos):
            quest_ids.append(bit_pos + 64 * base_index)
    return quest_ids

# Function to process the file
def process_file(filename):
    quest_ids = []
    
    with open(filename, 'r') as file:
        base_index = 0
        for line in file:
            # Ignore lines with brackets
            if '[' in line or ']' in line:
                continue
            
            # Convert scientific notation to a float and then to an integer
            try:
                bitfield = int(float(line.strip()))
                # Decode quest IDs for the current base index
                quest_ids.extend(decode_quest_ids(bitfield, base_index))
            except ValueError:
                print(f"ALERT! Quest section 32 - Skipping invalid line: {line.strip()}")
            
            base_index += 1
    
    return quest_ids

# Function to write all quest IDs to a file
def write_quest_ids_to_file(quest_ids, output_filename):
    with open(output_filename, 'w') as file:
        for quest_id in quest_ids:
            file.write(f"{quest_id}\n")

# Main execution
if __name__ == "__main__":
    input_filename = '30-QuestTemp.txt'
    output_filename = '32-QuestNoIndex.txt'
    quest_ids = process_file(input_filename)
    write_quest_ids_to_file(quest_ids, output_filename)

# Define the filenames
file1 = '32-QuestNoIndex.txt'
file2 = '31-QuestIndexID.txt'
output_file = '33-QuestIDs.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Process the first file
    with open(file1, 'r') as infile1:
        # Read the content of the first file
        content1 = infile1.read()
        # Write the content to the output file
        outfile.write(content1)
        # Optionally, add a separator or newline
        outfile.write('\n')  # Add a newline between file contents for clarity

    # Process the second file
    with open(file2, 'r') as infile2:
        # Read the content of the second file
        content2 = infile2.read()
        # Write the content to the output file
        outfile.write(content2)
# Filename of the file to sort
filename = '33-QuestIDs.txt'

def sort_file_numerically(filename):
    try:
        # Read the file
        with open(filename, 'r') as file:
            # Read all lines and strip any extra whitespace
            lines = [line.strip() for line in file if line.strip()]

        # Convert lines to integers, ignoring any non-numeric lines
        numbers = []
        for line in lines:
            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                # Skip lines that cannot be converted to integers
                continue

        # Sort numbers numerically
        numbers.sort()

        # Write the sorted numbers back to the file
        with open(filename, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")

        #print(f"File '{filename}' has been sorted numerically.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to sort the file
sort_file_numerically(filename)

# Define the filename
filename = '33-QuestIDs.txt'

# Read the file and filter out lines with values over 26034
with open(filename, 'r') as file:
    lines = file.readlines()

# Filter lines, handling potential ValueError if conversion fails
filtered_lines = []
for line in lines:
    stripped_line = line.strip()
    if stripped_line:  # Check if the line is not empty
        try:
            value = int(stripped_line)
            if value <= 26034:
                filtered_lines.append(line)
        except ValueError:
            # Skip lines that cannot be converted to integer
            continue

# Write the filtered lines back to the file
with open(filename, 'w') as file:
    file.writelines(filtered_lines)


# Define the source file, destination file, and output folder
source_filename = '33-QuestIDs.txt'
output_folder = 'Output'
destination_filename = '36-QuestMacro.txt'

def prepend_and_write_file(source_file, output_folder, dest_file):
    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Open the source file for reading
        with open(source_file, 'r') as file:
            # Read all lines from the source file
            lines = file.readlines()

        # Prepare the path for the destination file
        destination_path = os.path.join(output_folder, dest_file)

        # Open the destination file for writing
        with open(destination_path, 'w') as file:
            for line in lines:
                # Strip any existing whitespace and prepend '#qc '
                modified_line = '/s #qc ' + line.strip() + '\n'
                file.write(modified_line)

        #print(f"File '{destination_path}' has been created and written successfully.")

    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to process the file
prepend_and_write_file(source_filename, output_folder, destination_filename)

def delete_txt_files(directory):
    # Construct the search pattern for .txt files
    pattern = os.path.join(directory, '*.txt')
    
    # Use glob to find all .txt files
    txt_files = glob.glob(pattern)
    
    # Delete each .txt file
    for file_path in txt_files:
        try:
            os.remove(file_path)
            #print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"ALERT! Quest part 36, cleanup - Error deleting {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    delete_txt_files(current_directory)

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


def get_bits(value, start, end):
    """Extract bits from 'start' to 'end' from 'value'."""
    mask = (1 << (end - start + 1)) - 1
    return (value >> start) & mask

def right_shift(value, shift_amount):
    """Right shift the 'value' by 'shift_amount' bits."""
    return value >> shift_amount

def test_bit(value, bit_position):
    """Test if a specific bit is set in 'value'."""
    return (value & (1 << bit_position)) != 0

def get_limits(earned):
    """Placeholder function for limits. Customize if needed."""
    # Default limits: Example values for normal ranges
    bottom = 0
    top = 21000000  # Arbitrary upper limit for demonstration
    return bottom, top

def get_reputation_info(raw_value):
    # Extract faction type (bits 0-2)
    faction_type = get_bits(raw_value, 0, 2)
    
    # Check if faction type is normal
    if faction_type == 0:  # Assuming FACTION_TYPE_NORMAL == 0
        # Extract isNegative (bit 3)
        is_negative = test_bit(raw_value, 3)
        
        # Extract standing (bits 4-7)
        standing = get_bits(raw_value, 4, 7)
        
        # Extract earned value (bits 8+)
        earned = right_shift(raw_value, 8)
        
        # Adjust for negative reputation
        earned = -earned if is_negative else earned
        
        # Get limits (you can customize this part)
        bottom, top = get_limits(earned)
        
        return bottom, top, earned
    
    return None

def read_reputation_file(file_path):
    """Read the input file and parse the faction data."""
    faction_reputations = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split()
                faction_id = int(parts[0])
                raw_value = int(parts[1])
                faction_reputations[faction_id] = raw_value
    return faction_reputations

def main():
    # Path to the input file
    input_file = '40-ReputationsInput.txt'
    output_file = 'Output/41-ReputationMacro.txt'
    
    # Create the Output directory if it doesn't exist
    if not os.path.exists('Output'):
        os.makedirs('Output')
    
    # Read the faction reputation data from the file
    faction_reputations = read_reputation_file(input_file)
    
    # Write the interpreted reputation values to the output file
    with open(output_file, 'w') as file:
        for faction, raw_value in faction_reputations.items():
            result = get_reputation_info(raw_value)
            if result:
                bottom, top, reputation = result
                file.write(f".mod reputation {faction} {reputation}\n")
            else:
                file.write(f"ALERT! Reputation script section 41 - Faction ID {faction}: Invalid or unsupported faction type\n")

if __name__ == "__main__":
    main()

# Define the file path
file_path = 'Output/41-ReputationMacro.txt'

# Read the file and process it
try:
    # Open the file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines containing " 0"
    filtered_lines = [line for line in lines if " 0" not in line]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    #print(f"Lines containing ' 0' have been deleted from {file_path}")

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
def delete_txt_files(directory):
    # Construct the search pattern for .txt files
    pattern = os.path.join(directory, '*.txt')
    
    # Use glob to find all .txt files
    txt_files = glob.glob(pattern)
    
    # Delete each .txt file
    for file_path in txt_files:
        try:
            os.remove(file_path)
            #print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"ALERT! Reputation macro part 41, cleanup - Error deleting {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    delete_txt_files(current_directory)

def check_file_content(file_path):
    """Check if the file has content."""
    if os.path.exists(file_path):
        # Read the file and check if it has content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                return True
    return False

def download_html(url, output_file):
    """Download the HTML content from the URL and save it to the specified file."""
    print(f"Fetching data from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        
        # Save the HTML content to the specified file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML content saved to '{output_file}'")
    except requests.RequestException as e:
        print(f"Failed to retrieve data. Error: {e}")

def extract_reputation_data(html_file, output_file):
    """Extract the reputation data from the HTML file and save it to the output file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Define the regex pattern to extract the relevant part
        pattern = re.compile(r'Wrath of the Lich King","reputations":(.*?)}]}]}]}', re.DOTALL)
        match = pattern.search(html_content)
        
        if match:
            reputation_data = match.group(1).strip()
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(reputation_data)
            print(f"Reputation data saved to '{output_file}'")
        else:
            print("No reputation data found.")
    except FileNotFoundError as e:
        print(f"Error reading HTML file: {e}")

def format_reputation_file(input_file):
    """Format the reputation file to insert new lines before each {'id':."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace each {"id": with a new line before it
        formatted_content = re.sub(r'\{"id":', '\n{"id":', content)
        
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(formatted_content)
        print(f"Formatted reputation data saved to '{input_file}'")
    except FileNotFoundError as e:
        print(f"Error reading the file for formatting: {e}")

def remove_single_quotes(input_file):
    """Remove all single quotes from the file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove all single quotes
        content_no_quotes = content.replace("'", "")
        
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(content_no_quotes)
        print(f"Single quotes removed from '{input_file}'")
    except FileNotFoundError as e:
        print(f"Error reading the file for removing quotes: {e}")

def main():
    file_path = "Output/41-ReputationMacro.txt"
    url_template = "https://worldofwarcraft.blizzard.com/en-us/character/{region}/{realm}/{character}/reputation"
    html_file = "Output/reputation_page.html"
    reputation_file = "Output/42-ArmoryReputations.txt"
    
    # Read input values from files
    try:
        with open("References/4-Region.txt", "r") as file:
            region = file.read().strip().lower()
        
        with open("References/3-Realm.txt", "r") as file:
            realm = file.read().strip().lower().replace(" ", "-")
        
        with open("References/2-RetailChar.txt", "r") as file:
            character = file.read().strip().lower()
        
        # Construct the URL
        url = url_template.format(region=region, realm=realm, character=character)
    except FileNotFoundError as e:
        print(f"Error reading input files: {e}")
        return

    # Check if the file has content
    if check_file_content(file_path):
        print("Reputation macro OK!")
    else:
        print("Initiating reputation failover...")
        download_html(url, html_file)
        extract_reputation_data(html_file, reputation_file)
        format_reputation_file(reputation_file)
        remove_single_quotes(reputation_file)

if __name__ == "__main__":
    main()


# Define the standing values
standing_values = {
    'hated': -63000,
    'hostile': -6000,
    'unfriendly': -3000,
    'neutral': 0,
    'friendly': 3000,
    'honored': 6000,
    'revered': 9000,
    'exalted': 43000
}

# Function to process the files
def process_files():
    # Read the faction IDs from the FactionID.txt file
    faction_id_map = {}
    with open('Resources/FactionID.txt', 'r') as faction_file:
        for line in faction_file:
            parts = line.strip().split(';')
            if len(parts) == 2:
                id_str, name = parts
                faction_id_map[name.strip()] = id_str.strip()

    # Check if the reputations file exists before processing
    reputations_path = 'Output/42-ArmoryReputations.txt'
    if not os.path.exists(reputations_path):
        return  # Skip processing if the file does not exist

    # Process the reputations file
    with open(reputations_path, 'r') as reputations_file, \
         open('Output/43-ArmoryReputationMacro.txt', 'w') as output_file:
        
        for line in reputations_file:
            # Extract the data from the line using regex
            match = re.match(r'.*"name":"([^"]+)".*"standing":"([^"]+)".*"value":(\d+).*', line)
            if match:
                name, standing, value = match.groups()
                value = int(value)
                
                # Get the corresponding faction ID
                faction_id = faction_id_map.get(name.strip())
                
                if faction_id:
                    # Get the numeric standing value
                    standing_numeric = standing_values.get(standing.lower())
                    
                    if standing_numeric is not None:
                        # Write to the output file in the required format
                        output_file.write(f".mod reputation {faction_id} {value + standing_numeric}\n")

if __name__ == '__main__':
    process_files()


# Function to process the files
def process_exalted_reputations():
    # Read the faction IDs from the FactionID.txt file
    faction_id_map = {}
    with open('Resources/FactionID.txt', 'r') as faction_file:
        for line in faction_file:
            parts = line.strip().split(';')
            if len(parts) == 2:
                id_str, name = parts
                faction_id_map[name.strip()] = id_str.strip()

    # Check if the reputations file exists before processing
    reputations_path = 'Output/42-ArmoryReputations.txt'
    if not os.path.exists(reputations_path):
        return  # Skip processing if the file does not exist

    # Process the reputations file
    with open(reputations_path, 'r') as reputations_file, \
         open('Output/43-ArmoryReputationExalted.txt', 'w') as output_file:
        
        count_exalted = 0
        for line in reputations_file:
            # Extract the data from the line using regex
            match = re.search(r'"name":"([^"]+)".*"standing":"(Exalted|EXALTED|exalted)".*', line, re.IGNORECASE)
            if match:
                name = match.group(1).strip()
                
                # Get the corresponding faction ID
                faction_id = faction_id_map.get(name)
                
                if faction_id:
                    # Write to the output file in the required format
                    output_file.write(f".mod reputation {faction_id} 43000\n")
                    count_exalted += 1
                else:
                    print(f"Faction name '{name}' not found in FactionID.txt.")
        
        print(f"Found {count_exalted} 'EXALTED' standings. Results written to 43-ArmoryReputationExalted.txt.")

if __name__ == '__main__':
    process_exalted_reputations()

def combine_files():
    # File paths
    file_exalted = 'Output/43-ArmoryReputationExalted.txt'
    file_macro = 'Output/43-ArmoryReputationMacro.txt'
    output_file = 'Output/41-ReputationMacro.txt'
    reputations_path = 'Output/42-ArmoryReputations.txt'
    
    # Check if the reputations file exists before proceeding
    try:
        with open(reputations_path, 'r'):
            pass
    except FileNotFoundError:
        return

    # Read the content of the Exalted file
    try:
        with open(file_exalted, 'r') as f_exalted:
            exalted_lines = f_exalted.readlines()
    except FileNotFoundError:
        exalted_lines = []
    
    # Read the content of the Macro file
    try:
        with open(file_macro, 'r') as f_macro:
            macro_lines = f_macro.readlines()
    except FileNotFoundError:
        print(f"Error: {file_macro} not found.")
        macro_lines = []

    # Write combined content to the output file
    try:
        with open(output_file, 'w') as f_output:
            # Write the content from the Exalted file
            for line in exalted_lines:
                f_output.write(line)
            # Write the content from the Macro file
            for line in macro_lines:
                f_output.write(line)
        
        print(f"Combined content written to {output_file}.")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == '__main__':
    combine_files()

if os.path.isfile('Output/42-ArmoryReputations.txt'):
    os.remove('Output/42-ArmoryReputations.txt')

if os.path.isfile('Output/43-ArmoryReputationExalted.txt'):
    os.remove('Output/43-ArmoryReputationExalted.txt')

if os.path.isfile('Output/43-ArmoryReputationMacro.txt'):
    os.remove('Output/43-ArmoryReputationMacro.txt')
    
if os.path.isfile('Output/reputation_page.html'):
    os.remove('Output/reputation_page.html')

def extract_collected_mount_names(region, realm, character):
    # Construct the URL
    url = f"https://worldofwarcraft.blizzard.com/en-us/character/{region}/{realm}/{character}/collections/mounts"
    
    # Print the full URL
    print("")
    print("Gathering mounts...")
    print(f"Fetching data from: {url}")
    
    # Fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
    # Get the raw HTML content
    html_content = response.text
    
    # Save the raw HTML content to a file for reference
    with open("page_content.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML content saved to 'page_content.html'")
    
    # Regex pattern to find sections where "collected":true and extract the name value
    pattern = re.compile(r'\{"collected":true.*?"name":"(.*?)"', re.DOTALL)
    
    # Find all matches
    matches = pattern.findall(html_content)
    
    if matches:
        print("Collected Mounts:")
        with open("50-Mounts.txt", "w", encoding="utf-8") as output_file:
            for name in matches:
                print(name)
                output_file.write(name + "\n")
        print(f"\nCollected mount names have been saved to '50-Mounts.txt'")
        return matches
    else:
        print("No collected mounts found.")
        return None

def read_input_from_files():
    # Read inputs from files
    try:
        with open("References/4-Region.txt", "r") as file:
            region = file.read().strip().lower()
        
        with open("References/3-Realm.txt", "r") as file:
            realm = file.read().strip().lower().replace(" ", "-")
        
        with open("References/2-RetailChar.txt", "r") as file:
            character = file.read().strip().lower()
        
        return region, realm, character

    except FileNotFoundError as e:
        print(f"Error reading files: {e}")
        return None, None, None

if __name__ == "__main__":
    # Read input values from files
    region, realm, character = read_input_from_files()
    
    if region and realm and character:
        # Extract and print mount names
        extract_collected_mount_names(region, realm, character)
    else:
        print("Error: Could not read one or more input files.")


def extract_collected_pet_names(region, realm, character):
    # Construct the URL
    url = f"https://worldofwarcraft.blizzard.com/en-us/character/{region}/{realm}/{character}/collections/pets"
    
    # Print the full URL
    print("")
    print("Gathering pets...")
    print(f"Fetching data from: {url}")
    
    # Fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
    # Get the raw HTML content
    html_content = response.text
    
    # Save the raw HTML content to a file for reference
    with open("page_content.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML content saved to 'page_content.html'")
    
    # Regex pattern to find collected pet names
    pattern = re.compile(r'"collected":true,.*?"level":\d+,"name":"(.*?)"')
    
    # Find all matches
    matches = pattern.findall(html_content)
    
    if matches:
        print("Collected Pets:")
        with open("51-Pets.txt", "w", encoding="utf-8") as output_file:
            for name in matches:
                print(name)
                output_file.write(name + "\n")
        print(f"\nCollected pet names have been saved to '51-Pets.txt'")
        return matches
    else:
        print("No collected pets found.")
        return None

def read_input_from_files():
    # Read inputs from files
    try:
        with open("References/4-Region.txt", "r") as file:
            region = file.read().strip().lower()
        with open("References/3-Realm.txt", "r") as file:
            realm = file.read().strip().lower().replace(" ", "-")
        with open("References/2-RetailChar.txt", "r") as file:
            character = file.read().strip().lower()
        return region, realm, character
    except FileNotFoundError as e:
        print(f"Error reading files: {e}")
        return None, None, None

if __name__ == "__main__":
    # Read input values from files
    region, realm, character = read_input_from_files()
    
    if region and realm and character:
        # Extract and print pet names
        extract_collected_pet_names(region, realm, character)
    else:
        print("Error: Could not read one or more input files.")

# Define file paths
mounts_file = '50-Mounts.txt'
pets_file = '51-Pets.txt'
spell_file = 'Resources/Spell.txt'
mounts_output_file = '52-MountSpellIDs.txt'
pets_output_file = '52-PetSpellIDs.txt'

def read_lines_from_file(file_path):
    """Read lines from a given file and return as a list of strings."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def read_spell_data(file_path):
    """Read data from the spell file and return it as a list of rows, where each row is a list of columns."""
    print("Cleaning out invalid mounts and pets from later expansions...")
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def find_matching_spell_ids(lines, spell_data):
    """Find matching spell IDs based on the lines and spell data."""
    spell_ids = []
    for line in lines:
        for row in spell_data:
            if line in row[1:]:  # Skip the first column, which is the spell ID
                spell_ids.append(row[0])
                break  # No need to check further columns if we found a match
    return spell_ids

def write_ids_to_file(file_path, ids):
    """Write the list of IDs to a file, one per line."""
    with open(file_path, 'w') as file:
        file.write('\n'.join(ids))

def main():
    # Read data from files
    mounts_lines = read_lines_from_file(mounts_file)
    pets_lines = read_lines_from_file(pets_file)
    spell_data = read_spell_data(spell_file)
    
    # Find matching spell IDs for mounts and pets
    mount_spell_ids = find_matching_spell_ids(mounts_lines, spell_data)
    pet_spell_ids = find_matching_spell_ids(pets_lines, spell_data)
    
    # Write results to output files
    write_ids_to_file(mounts_output_file, mount_spell_ids)
    write_ids_to_file(pets_output_file, pet_spell_ids)

if __name__ == "__main__":
    main()

# Define file paths
mount_spell_ids_file = '52-MountSpellIDs.txt'
allowed_mounts_file = 'Resources/AllowedMounts.txt'

# Read allowed mounts from AllowedMounts.txt
with open(allowed_mounts_file, 'r') as f:
    allowed_mounts = set(line.strip() for line in f)

# Read and filter mount spell IDs
with open(mount_spell_ids_file, 'r') as f:
    lines = f.readlines()

# Filter lines where the number is in allowed_mounts
filtered_lines = [line for line in lines if line.strip() in allowed_mounts]

# Write the filtered lines back to 52-MountSpellIDs.txt
with open(mount_spell_ids_file, 'w') as f:
    f.writelines(filtered_lines)

print("Filtering complete. Invalid mounts and pets removed.")


# Define file paths
mount_spell_ids_file = '52-MountSpellIDs.txt'
pet_spell_ids_file = '52-PetSpellIDs.txt'
output_file = 'Output/54-MountsAndPetsMacro.txt'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

def read_and_prefix(file_path, prefix):
    """Read a file and prefix each line with the given prefix."""
    with open(file_path, 'r') as file:
        return [prefix + line for line in file]

# Read and prefix lines from both files
mount_lines = read_and_prefix(mount_spell_ids_file, '.learn ')
pet_lines = read_and_prefix(pet_spell_ids_file, '.learn ')

# Combine the lines
combined_lines = mount_lines + pet_lines

# Write the combined lines to the output file
with open(output_file, 'w') as file:
    file.writelines(combined_lines)

# Get the current working directory
current_directory = os.getcwd()

# Define file patterns to match
file_patterns = ['*.txt', '*.html']

# Collect all files matching the patterns
files_to_delete = []
for pattern in file_patterns:
    files_to_delete.extend(glob.glob(os.path.join(current_directory, pattern)))

# Delete the matched files
for file_path in files_to_delete:
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"ALERT! Failed to delete {file_path}. Reason: {e}. Your macro file may be polluted!")

def modify_file_in_place(file_path, skip_numbers):
  """Modifies a file in place by removing lines containing specified numbers.

  Args:
    file_path: The path to the file to modify.
    skip_numbers: A set of numbers to filter out.
  """

  with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # Move the file pointer to the beginning
    file.truncate()  # Clear the file contents

    for line in lines:
      if not any(number in line for number in skip_numbers):
        file.write(line)

# Example usage
skip_numbers = {
    '70613', '69002', '61773', '44841', '44842', '44843',
    '60025', '59961', '40990', '68187', '68188', '60119',
    '60118', '72808', '72807', '63956', '63963', '60024',
    '61472'
}

input_file = 'Output/54-MountsAndPetsMacro.txt'
modify_file_in_place(input_file, skip_numbers)

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_to_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def get_rest_xp_value(file_pattern):
    """Extract the restXP value from the DataStore files."""
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            for line in file:
                if '["restXP"]' in line:
                    # Extract the value
                    start_idx = line.find('=') + 1
                    end_idx = line.find(',', start_idx)
                    rest_xp_value = int(line[start_idx:end_idx].strip())
                    return rest_xp_value // 1000
    raise FileNotFoundError("No valid DataStore file found or ['restXP'] not found")

def main():
    references_path = 'References/5-MaxLevel.txt'
    output_path = 'Output/60-LevelUpMacro.txt'
    datastore_pattern = 'Input/CharSplit/DataStore_Characters_Info_*.txt'
    
    if os.path.exists(references_path) and os.path.getsize(references_path) > 0:
        # Read the value from the 5-MaxLevel.txt file
        max_level_value = read_file_content(references_path)
        content = f"\n.levelup -80 \n.levelup {max_level_value}\n"
    else:
        # Read the value from the DataStore file
        try:
            number_from_datastore = get_rest_xp_value(datastore_pattern)
            content = f".levelup -80 \n.levelup {number_from_datastore}\n"
        except FileNotFoundError as e:
            print(e)
            return
    
    # Write to the Output/5-LevelUpMacro.txt file
    write_to_file(output_path, content)
    #print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()


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


# Define file paths
input_file = 'Output/22-AchievementMacro.txt'
output_file = 'Output/90-ProfessionPayment.txt'

# Delete output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Check if input file exists
if not os.path.exists(input_file):
    print(f"ALERT: Achivement file error!")
else:
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Determine the conditions based on file content
    contains_735 = '.achievement add 735' in content
    contains_734 = '.achievement add 734' in content

    # Prepare the output based on conditions
    if contains_735:
        output_content = (
            '.send items Charactername "Professions" "Hi! We see that you had two Grand Master professions previously. In order to select your new profession here, please find the enclosed emblems. You can exchange these at the Mall\'s Scientist to get two 450/450 professions of your choosing." 49426:200\n'
        )
        print("")
        print("Professions status:")
        print(f"Two professions found! Compensation to buy new professions written to to {output_file}")
        print("")
    elif contains_734 and not contains_735:
        output_content = (
            '.send items Charactername "Professions" "Hi! We see that you had one Grand Master profession previously. In order to select your new professions here, please find the enclosed emblems. You can exchange these at the Mall\'s Scientist to get a 450/450 profession of your choosing." 49426:100\n'
        )
        print("")
        print("Professions status:")
        print(f"One profession found! Compensation to buy new profession written to to {output_file}")
        print("")
    else:
        output_content = ''

    # Write to the output file
    if output_content:
        with open(output_file, 'w') as file:
            file.write(output_content)
    else:
        print("")
        print("Professions status:")
        print("Character has no maxed professions - skipping profession macro.")
        print("")


# Define file paths
death_knight_file = 'Output/97-DeathKnight.txt'
teleport_file = 'Output/97-Teleport.txt'
data_store_pattern = 'Input/CharSplit/DataStore_Spells_Characters_*.txt'

# Step 1: Delete the files if they exist
if os.path.exists(death_knight_file):
    os.remove(death_knight_file)

if os.path.exists(teleport_file):
    os.remove(teleport_file)

# Step 2: Check for the word "DEATHKNIGHT" in the relevant files
found_death_knight = False

# Search for files matching the pattern
files = glob.glob(data_store_pattern)

def check_and_write_files():
    found_death_knight = False

    # Search for files matching the pattern
    files = glob.glob(data_store_pattern)

    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            if 'DEATHKNIGHT' in content:
                found_death_knight = True
                break

    # Write the appropriate content to the files
    if found_death_knight:
        with open(death_knight_file, 'w') as f:
            f.write('\n.mod money -1073480')
            f.write('\n/in 60 /s #ti3j5kfo0s')
            f.write('\n.additem 37742 -42')
    else:
        with open(teleport_file, 'w') as f:
            f.write('\n.tele dalainn')


def check_file_size(folder_path):
    """Checks the size of all files in a given folder and prints an error message for files less than 5 bytes.

    Args:
        folder_path: The path to the folder to check.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size < 5:
                print("")
                print(f"ERROR! File {filename} is empty! Verify data integrity!")
                print("")

def replace_charactername(output_folder, recipient_file):
    try:
        with open(recipient_file, 'r') as f:
            replacement_text = f.read().strip()  # Remove leading/trailing whitespace

        for filename in os.listdir(output_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(output_folder, filename)
                with open(file_path, 'r+') as f:
                    content = f.read()
                    content = content.replace('Charactername', replacement_text)
                    f.seek(0)
                    f.write(content)
                    f.truncate()
    except FileNotFoundError:
        print(f"Error: File not found: {recipient_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_macro_files(folder_path):
    for file in glob.glob(os.path.join(folder_path, "*Macro*")):
        os.remove(file)

def create_customize_file(folder_path):
    file_path = os.path.join(folder_path, "95-Customize.txt")
    with open(file_path, "w") as f:
        f.write("\n.character changerace Charactername\n")
        f.write(".character changefaction Charactername\n")
        f.write(".character customize Charactername\n")
        f.write(".unlearn 53140\n")
        f.write(".unlearn 61721\n")
        f.write(".unlearn 59390\n")

def combine_text_files(folder_path):
    output_file_path = os.path.join(folder_path, "CombinedMacroOutput.txt")
    with open(output_file_path, "w") as outfile:
        for filename in glob.glob(os.path.join(folder_path, "*.txt")):
            if filename != output_file_path:
                with open(filename, "r") as infile:
                    outfile.write(infile.read())

def copy_file(source_file, destination_folder):
    shutil.copy2(source_file, destination_folder)

def find_classname(filename):
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'"englishClass"] = "([^"]+)"', line)
            if match:
                classname = match.group(1)
    return classname

def main():
    # Create the customization file first
    create_customize_file("Output")

    # Replace character names
    replace_charactername("Output", "References/1-Recipient.txt")

    # Check file sizes
    check_file_size("Output")

    # Check for DEATHKNIGHT and write to the appropriate files
    check_and_write_files()

    # Delete macro files
    delete_macro_files("..")

    # Combine text files
    combine_text_files("Output")

    # Copy the combined file to the destination folder
    copy_file("Output/CombinedMacroOutput.txt", "..")

    # Find class names and prompt user
    file_pattern = "Input/CharSplit/DataStore_Spells_Characters_*.txt"
    files = glob.glob(file_pattern)
    for file in files:
        classname = find_classname(file)
        print("Macro created! Remember to make a:")
        print("")
        print("Class: " + classname)
        print("Race: Any race. Race customization is pushed.")
        print("")
        print("Press any key to continue...")
        input()

    sys.exit()

if __name__ == "__main__":
    main()


def terminate_process():
    print("Terminating process...")
    os._exit(1)  # 0 is usually used for successful termination, non-zero for errors

if __name__ == "__main__":
    terminate_process()