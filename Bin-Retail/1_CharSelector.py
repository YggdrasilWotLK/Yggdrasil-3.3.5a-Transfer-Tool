#Authored by mostly nick :)
import re
import subprocess
import os
import shutil
import sys

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
