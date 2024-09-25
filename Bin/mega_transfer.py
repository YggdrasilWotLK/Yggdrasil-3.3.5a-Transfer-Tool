import csv
import os
import re
import shutil
import subprocess
import sys

#Authored by mostly nick :)

file_path_terminate = 'TERMINATERETAIL.txt'

# Check if the file exists and delete it
if os.path.exists(file_path_terminate):
    os.remove(file_path_terminate)
    #print(f"{file_path_terminate} has been deleted.")

def find_file(root_dir, filename):
    """Search for a file with the specified name in the given directory and its subdirectories."""
    for dirpath, _, files in os.walk(root_dir):
        if filename in files:
            return dirpath
    return None

def find_account_folder(root_dir):
    """Recursively search for an 'ACCOUNT' folder in the given directory and its subdirectories."""
    for dirpath, dirs, _ in os.walk(root_dir):
        if 'Account' in dirs:
            return os.path.join(dirpath, 'ACCOUNT')
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

def main():
    root_path = '../RawData'
    search_file = 'Blizzard_GlueSavedVariables.lua'
    retail_folder = '../Bin-Retail/RawData'
    
    # Use absolute path for the batch script
    batch_script = os.path.abspath('../Bin-Retail/0_Run.bat')
    
    #print(f"Searching for '{search_file}' in {root_path}...")

    file_location = find_file(root_path, search_file)
    
    if file_location:
        print("Welcome to Yggdrasil's retail to WotLK 3.3.5a toon transfer utility!")
        print(" ")
        
        account_folder_path = find_account_folder(root_path)
        
        if account_folder_path:
            #print(f"ACCOUNT folder found at: {account_folder_path}")
            print("Please select a retail account to continue with:")
            directories = list_directories(account_folder_path)
            
            if not directories:
                print("No account folders found.")
                return
            
            for i, folder in enumerate(directories, start=1):
                print(f"{i}. {folder}")
            
            choice = 1  # Default choice
            try:
                user_input = input("Enter account number: ")
                choice = int(user_input)
                if not (1 <= choice <= len(directories)):
                    print("Choice out of range. Defaulting to 1.")
                    choice = 1
            except ValueError:
                print("Invalid input. Defaulting to 1.")
                
            selected_folder = directories[choice - 1]
            selected_folder_path = os.path.join(account_folder_path, selected_folder, 'SavedVariables')
            
            if os.path.isdir(selected_folder_path):
                copy_files(selected_folder_path, retail_folder)
                
                with open(file_path_terminate, "w") as file:
                    file.write("")

                batch_dir = os.path.dirname(batch_script)
                os.chdir(batch_dir)
                
                try:
                    print(" ")
                    subprocess.run([os.path.basename(batch_script)], shell=True, check=True)
                    #print("Batch script executed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error executing batch script: {e}")
                
            else:
                print(f"Folder {selected_folder_path} does not exist.")
        else:
            print(f"ACCOUNT folder not found in {root_path}.")

if __name__ == "__main__":
    main()
#Authored by mostly nick :)

file_path = 'TERMINATERETAIL.txt'

# Check if the file exists
if os.path.exists(file_path):
    parent_pid = os.getppid()  # Get the parent process ID
    os.kill(parent_pid, 9)  # Send SIGKILL signal to the parent
else:
    print(f"Welcome to Yggdrasil's WotLK 3.3.5a toon transfer utility!")
#Authored by mostly nick :)

def delete_small_folder(folder_path, size_threshold=1024):
  """Deletes a folder if its total size is less than the specified threshold.

  Args:
    folder_path: The path to the folder to check.
    size_threshold: The minimum size of the folder in bytes to keep it.
  """

  if not os.path.exists(folder_path):
    return  # Folder doesn't exist, do nothing

  total_size = 0
  for root, _, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      total_size += os.path.getsize(file_path)

  if total_size < size_threshold:
    shutil.rmtree(folder_path)
    #print(f"Deleted folder: {folder_path}")

# Replace with the actual path to your RawData folder
folder_to_check = "../RawData/Account"
delete_small_folder(folder_to_check)

#Authored by mostly nick :)

def clean_raw_data():
  """Cleans the ../RawData folder, preserving only the "Account" folder."""

  raw_data_path = "../RawData"

  # Check if RawData folder exists
  if not os.path.exists(raw_data_path):
    #print(f"Error: RawData folder '{raw_data_path}' does not exist.")
    return

  # Check if Account folder exists within RawData
  account_path = os.path.join(raw_data_path, "Account")
  if not os.path.exists(account_path):
    return

  # Get a list of all files and folders in RawData except Account
  items_to_delete = [item for item in os.listdir(raw_data_path) if item != "Account"]

  # Delete each item in the list
  for item in items_to_delete:
    item_path = os.path.join(raw_data_path, item)
    if os.path.isfile(item_path):
      os.remove(item_path)
    elif os.path.isdir(item_path):
      shutil.rmtree(item_path)

if __name__ == "__main__":
  clean_raw_data()

#Authored by mostly nick :)

def move_wtf_contents(base_dir):
    wtf_dir = os.path.join(base_dir, 'WTF')
    
    if os.path.exists(wtf_dir) and os.path.isdir(wtf_dir):
        items = os.listdir(wtf_dir)
        
        for item in items:
            source_path = os.path.join(wtf_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            shutil.move(source_path, destination_path)
        
        os.rmdir(wtf_dir)

def list_folders_in_account(base_dir):
    account_dir = os.path.join(base_dir, 'account')
    
    if os.path.exists(account_dir) and os.path.isdir(account_dir):
        items = os.listdir(account_dir)
        folders = [item for item in items if os.path.isdir(os.path.join(account_dir, item))]
        
        if folders:
            print("Account-based structure identified. Available accounts:")
            for idx, folder in enumerate(folders):
                print(f"{idx + 1}. {folder}")
            return folders
        else:
            print("ERROR: No accounts found!")
            return []
    else:
        return []

def move_contents(selected_folder, base_dir):
    source_dir = os.path.join(base_dir, 'account', selected_folder)
    
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        items = os.listdir(source_dir)
        
        for item in items:
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(base_dir, item)
            
            shutil.move(source_path, destination_path)

def check_for_conflict(base_dir):
    for item in os.listdir(base_dir):
        subdir = os.path.join(base_dir, item)
        if os.path.isdir(subdir):
            account_dir = os.path.join(subdir, 'account')
            saved_vars_dir = os.path.join(subdir, 'SavedVariables')
            if os.path.isdir(account_dir) and os.path.isdir(saved_vars_dir):
                print(f"Conflict found in directory: {subdir}")
                return True
    return False

def main():
    base_dir = '../RawData'

    if check_for_conflict(base_dir):
        print("Operation aborted due to directory conflict.")
        return

    move_wtf_contents(base_dir)
    folders = list_folders_in_account(base_dir)
    
    if folders:
        while True:
            try:
                selection = int(input("Select an account by number: ")) - 1
                if 0 <= selection < len(folders):
                    selected_folder = folders[selection]
                    move_contents(selected_folder, base_dir)
                    break
                else:
                    print("Invalid selection. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

#Authored by mostly nick :)

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        # Iterate over all the files and folders in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The folder {folder_path} does not exist.')

# Paths to the folders
input_folder = 'Input'
output_folder = 'Output'

# Clear the folders
clear_folder(input_folder)
clear_folder(output_folder)

#print("Input and Output folders have been cleared!")
#Authored by mostly nick :)

def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) and not filename.endswith(".lua"):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

def move_lua_files(source_dir, dest_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith(".lua"):
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            try:
                shutil.move(source_file, dest_file)
            except Exception as e:
                print(f"Failed to move {source_file} to {dest_file}: {e}")

def main():
    # 1. Go back to the RawData folder
    raw_data_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "RawData"))

    # 2. Delete all files in RawData folder except .lua files
    delete_files_in_directory(raw_data_dir)

    # 3. Check if SavedVariables folder exists
    saved_variables_dir = os.path.join(raw_data_dir, "SavedVariables")
    if os.path.exists(saved_variables_dir):
        # Move .lua files from SavedVariables folder to RawData folder
        move_lua_files(saved_variables_dir, raw_data_dir)
        
        # 4. Delete the SavedVariables folder
        try:
            shutil.rmtree(saved_variables_dir)
            #print("Deleted SavedVariables folder.")
        except Exception as e:
            print(f"Failed to delete SavedVariables folder: {e}")
    #else:
        #print("No account identified. Skipping to character identification.")

if __name__ == "__main__":
    main()
#Authored by mostly nick :)

def read_file_safely(file_path):
    """Reads the file content safely, handling potential decoding errors."""
    content = []
    with open(file_path, 'rb') as file:
        for line in file:
            try:
                content.append(line.decode('utf-8'))
            except UnicodeDecodeError:
                content.append('')  # Add an empty line for lines that can't be decoded
    return ''.join(content)

def write_file_safely(file_path, content):
    """Writes content to a file, ignoring encoding errors."""
    with open(file_path, 'wb') as file:
        file.write(content.encode('utf-8', errors='ignore'))

def get_character_names_and_realms(file_path):
    """Extracts character names and realms from the Lua file."""
    content = read_file_safely(file_path)

    # Pattern for 'profileKeys' mapping
    profile_keys_pattern = r'\["profileKeys"\]\s*=\s*\{([^}]*)\}'
    profile_keys_matches = re.findall(profile_keys_pattern, content, re.DOTALL)
    
    # Pattern for 'global' character definitions
    global_chars_pattern = r'\["Default\.(.*?)\.(.*?)"\]\s*=\s*\{[^}]*\["name"\]\s*=\s*"(.*?)"'
    global_chars_matches = re.findall(global_chars_pattern, content)

    results = {}
    
    # Extract data from profileKeys matches
    for match in profile_keys_matches:
        pairs = re.findall(r'\["(.*?)"\]\s*=\s*"(.*?)"', match)
        for key, value in pairs:
            parts = key.split(' - ')
            if len(parts) == 3:
                char_name = parts[0]
                realm = ' - '.join(parts[1:])  # Realm
                if char_name not in results:
                    results[char_name] = (realm, value)

    # Extract data from global characters matches
    for realm, char_name, display_name in global_chars_matches:
        if char_name not in results:
            results[char_name] = (realm, display_name)

    return results

def write_to_file(name):
    """Writes the selected character name to a file."""
    os.makedirs('References', exist_ok=True)
    with open('References/Argument.txt', 'w') as file:
        file.write(name)

def update_lua_files(raw_data_path, selected_name, selected_realm):
    """Updates Lua files to remove/rename non-selected realm entries."""
    for root, _, files in os.walk(raw_data_path):
        for file in files:
            if file.endswith(".lua"):
                file_path = os.path.join(root, file)
                content = read_file_safely(file_path)

                # Update non-selected realms
                content = re.sub(rf'\["Default\.(?!{selected_realm})(.*?)\.{selected_name}"\]', '["Default.\\1.DELETEDNAME"]', content)
                content = re.sub(rf'\["{selected_name} - (?!{selected_realm})(.*?)"\]', '["DELETEDNAME - \\1"]', content)

                write_file_safely(file_path, content)

def main():
    """Main function to handle user interaction and file updates."""
    raw_data_path = "../RawData"
    lua_file = "DataStore_Characters.lua"
    file_path = os.path.join(raw_data_path, lua_file)

    try:
        characters = get_character_names_and_realms(file_path)
        if not characters:
            raise FileNotFoundError

        if len(characters) > 1:
            print("Character names found:")
            for i, (name, _) in enumerate(characters.items(), 1):
                print(f"{i}. {name}")

            while True:
                selection = input("Select character name by number: ")
                try:
                    index = int(selection) - 1
                    if 0 <= index < len(characters):
                        selected_name = list(characters.keys())[index]
                        break
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

        elif len(characters) == 1:
            selected_name = list(characters.keys())[0]

        selected_realm = characters[selected_name][0]

        write_to_file(selected_name)
        print(f"Character identified: {selected_name} - {selected_realm}. Extracting character files...")

        update_lua_files(raw_data_path, selected_name, selected_realm)

    except FileNotFoundError:
        print(f"ERROR: No characters found, terminating! Were the transfer addons correctly set up?")
        input("Press Enter to exit...")
        parent_pid = os.getppid()
        os.kill(parent_pid, 9)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}. Terminating!")
        input("Press Enter to exit...")
        parent_pid = os.getppid()
        os.kill(parent_pid, 9)

if __name__ == "__main__":
    main()



#Authored by mostly nick :)

# Prompt the user for input
character_name = input("Enter name of new character on Yggdrasil, if not same as on old server: ")

# Specify the file paths
argument_file = "References/Argument.txt"
recipient_file = "References/Recipient.txt"

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
#Authored by mostly nick :)

def read_character_name(file_path):
  """Reads the character name from the specified file."""
  try:
    with open(file_path, "r") as file:
      character_name = file.readline().strip()
      return character_name
  except FileNotFoundError:
    return None
  except Exception as e:
    return None

def search_and_copy_valid_files(character_name):
    raw_folder = "../RawData"
    found_file = False
    for root, dirs, files in os.walk(raw_folder):
        for file in files:
            if file == "EveryQuest.lua":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    if "EveryQuestDBPC" in content and character_name in content:
                        destination = os.path.join(raw_folder, "EveryQuestData.lua")
                        if not os.path.exists(destination) or os.path.getsize(file_path) != os.path.getsize(destination):
                            shutil.copyfile(file_path, destination)
                            found_file = True
                            break
        if found_file:
            break
    return found_file
    
def main():
    character_name_file = "References/Argument.txt"
    character_name = read_character_name(character_name_file)
    if character_name:
        found_valid_file = search_and_copy_valid_files(character_name)
        if not found_valid_file:
            # Check for EveryQuestData.lua in ../RawData
            if not os.path.exists("../RawData/EveryQuestData.lua"):
                print("ALERT: Did not find EveryQuests file for character. Ignore me if you're not transferring quests..")

    else: 
        pass

if __name__ == "__main__":
  main()



#Authored by mostly nick :)

def clear_and_copy(source_folder, destination_folder):
    # Clear the contents of the destination folder
    for filename in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    # Copy files from source to destination
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        try:
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
        except Exception as e:
            print(f"Failed to copy {source_file} to {destination_file}. Reason: {e}")

if __name__ == "__main__":
    source_folder = "../RawData"
    destination_folder = "Raw"
    clear_and_copy(source_folder, destination_folder)
#Originally authored by Lortz
#Appended by mostly  nick :)

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

with open("Input/DataStore_Talents.lua", 'r') as f:
    lines = f.readlines()

with open("temp_output.txt", 'w') as out:
    flag = None
    p = False
    for line in lines:
        if "Class" in line:
            var_class = line.strip().split('"')[3].strip()
        if "DataStore_TalentsRefDB" in line:
            break
        elif "TalentTrees" in line:
            p = True
        if p:
            out.write(line)

with open("temp_output.txt", 'r') as f2:
    lines = f2.readlines()

with open("main_spec.txt", 'w') as pri, open("sec_spec.txt", 'w') as sec:
    for line in lines:
        if "|" in line.strip():
            flag = line.split('|')[1].split('"')[0]
        if "nil".casefold() in line:
            continue
        if "}," in line:
            continue
        if "TalentTrees" in line:
            continue
        if "PointsSpent" in line:
            break
        if flag == "1":
            pri.write(line.strip() + "\n")
        if flag == "2":
            sec.write(line.strip() + "\n")

out_macro_file = open("out_macro_talent.txt", 'w')

with open("main_spec.txt", 'r') as f3:
    lines = f3.readlines()

out_macro_file.write("/click TalentMicroButton" + "\n")
out_macro_file.write("/click GameMenuButtonUIOptions" + "\n")
out_macro_file.write("/click InterfaceOptionsFeaturesPanelPreviewTalentChanges" + "\n")
out_macro_file.write("/click InterfaceOptionsFrameOkay\n")
out_macro_file.write("/click GameMenuButtonContinue\n")
out_macro_file.write("/click PlayerSpecTab1" + "\n")

dict_class = {
    'Blood': 1, 'Frost': 2, 'Unholy': 3, 'Balance': 1, 'Feral': 2, 'Restoration': 3,
    'Beast Mastery': 1, 'Marksmanship': 2, 'Survival': 3, 'Arcane': 1, 'Fire': 2,
    'Frost_m': 3, 'Holy_p': 1, 'Protection_p': 2, 'Retribution': 3, 'Discipline': 1,
    'Holy': 2, 'Shadow': 3, 'Assassination': 1, 'Combat': 2, 'Subtlety': 3,
    'Elemental': 1, 'Enhancement': 2, 'Restoration_s': 3, 'Affliction': 1,
    'Demonology': 2, 'Destruction': 3, 'Arms': 1, 'Fury': 2, 'Protection': 3
}

for line in lines:
    if "|" in line:
        spec = (line.split('|')[0].split('"')[1])
        if spec == "Frost" and var_class == "MAGE":
            spec = "Frost_m"
        if spec == "Holy" and var_class == "PALADIN":
            spec = "Holy_p"
        if spec == "Protection" and var_class == "PALADIN":
            spec = "Protection_p"
        if spec == "Restoration" and var_class == "SHAMAN":
            spec = "Restoration_s"
        val = dict_class.get(spec)
        out_macro_file.write("/click PlayerTalentFrameTab" + str(val) + "\n")
    if "--" in line.strip():
        value = int(line.split(",")[0])
        ind = line.split('[')[1].split(']')[0]
        for i in range(value):
            out_macro_file.write("/click PlayerTalentFrameTalent" + ind + "\n")
    if "=" in line.strip() and "," in line.strip():
        value = int(line.split("=")[1].split(",")[0])
        ind = line.split('[')[1].split(']')[0]
        for i in range(value):
            out_macro_file.write("/click PlayerTalentFrameTalent" + ind + "\n")

if os.stat("sec_spec.txt").st_size == 0:
    out_macro_file.write("/click PlayerTalentFrameLearnButton" + "\n")
    out_macro_file.write("/click StaticPopup1Button1\n")
    out_macro_file.write("/click TalentMicroButton\n")

if os.stat("sec_spec.txt").st_size > 0:
    out_macro_file.write("/click TalentMicroButton\n")
    out_macro_file.write("/click PlayerTalentFrameLearnButton" + "\n")
    out_macro_file.write("/click StaticPopup1Button1" + "\n")
    out_macro_file.write(".learn 63644" + "\n")
    out_macro_file.write(".cast 63624" + "\n")
    out_macro_file.write(".cast 63644" + "\n")
    out_macro_file.write("/click TalentMicroButton\n")
    out_macro_file.write("/click PlayerSpecTab2" + "\n")
    with open("sec_spec.txt", 'r') as f4:
        lines = f4.readlines()
        for line in lines:
            if "|" in line:
                spec = (line.split('|')[0].split('"')[1])
                if spec == "Frost" and var_class == "MAGE":
                    spec = "Frost_m"
                if spec == "Holy" and var_class == "PALADIN":
                    spec = "Holy_p"
                if spec == "Protection" and var_class == "PALADIN":
                    spec = "Protection_p"
                if spec == "Restoration" and var_class == "SHAMAN":
                    spec = "Restoration_s"
                val = dict_class.get(spec)
                out_macro_file.write("/click PlayerTalentFrameTab" + str(val) + "\n")
            if "--" in line.strip():
                value = int(line.split(",")[0])
                ind = line.split('[')[1].split(']')[0]
                for i in range(value):
                    out_macro_file.write("/click PlayerTalentFrameTalent" + ind + "\n")
            if "=" in line.strip() and "," in line.strip():
                value = int(line.split("=")[1].split(",")[0])
                ind = line.split('[')[1].split(']')[0]
                for i in range(value):
                    out_macro_file.write("/click PlayerTalentFrameTalent" + ind + "\n")
    out_macro_file.write("/click PlayerTalentFrameLearnButton" + "\n")
    out_macro_file.write("/click StaticPopup1Button1\n")
    out_macro_file.write(".cheat casttime off" + "\n")

out_macro_file.close()

def extract_number(line):
    numbers = re.findall(r'\d+', line)
    if numbers:
        return int(numbers[-1])
    else:
        return float('inf')

def sort_lines_between_targets(filename):
    target1 = "/click PlayerTalentFrameTab"
    target2 = "/click PlayerTalentFrameLearnButton"

    with open(filename, 'r') as f:
        lines = f.readlines()

    sorted_sections = []
    start_index = 0

    for i in range(len(lines)):
        if target1 in lines[i] or target2 in lines[i] or i == len(lines) - 1:
            if i != start_index:
                sorted_section = sorted(lines[start_index:i], key=extract_number)
                sorted_sections.extend(sorted_section)
            sorted_sections.append(lines[i])
            start_index = i + 1

    return sorted_sections

def split_file(sorted_content):
    split_index = -1
    for i, line in enumerate(sorted_content):
        if ".learn 63644" in line:
            split_index = i
            part1 = sorted_content[:split_index]
            part2 = sorted_content[split_index:]

            with open("../MacroTalentsPrimary.txt", 'w') as file1:
                file1.writelines(part1)
            with open("../MacroTalentsSecondary.txt", 'w') as file2:
                file2.writelines(part2)
            break

    if split_index == -1:
        if os.path.exists("../MacroTalentsPrimary.txt"):
            os.remove("../MacroTalentsPrimary.txt")
        if os.path.exists("../MacroTalentsSecondary.txt"):
            os.remove("../MacroTalentsSecondary.txt")

        shutil.copyfile("out_macro_talent.txt", "../MacroTalentsPrimary.txt")

if __name__ == "__main__":
    filename = "out_macro_talent.txt"
    sorted_content = sort_lines_between_targets(filename)
    split_file(sorted_content)

#Authored by mostly nick :)
file_path = "../MacroTalentsPrimary.txt"
string_to_remove = ".cast 63624"
lines_to_append = [
    "/click PlayerTalentFrameLearnButton\n",
    "/click StaticPopup1Button1\n"
]

with open(file_path, 'r') as file:
    lines = file.readlines()

modified_lines = [line.replace(string_to_remove, "") for line in lines]

if (len(modified_lines) >= 2 and
    modified_lines[-2].strip() == lines_to_append[0].strip() and
    modified_lines[-1].strip() == lines_to_append[1].strip()):
    pass
else:
    modified_lines.extend(lines_to_append)
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)




#Authored by mostly nick :)

def prepend_to_file(file_path, text_to_prepend):
  """Prepends text to a file if it exists."""
  if os.path.exists(file_path):
    with open(file_path, "r+") as f:
      content = f.read()
      f.seek(0, 0)  # Move the pointer to the beginning of the file
      f.write(text_to_prepend + content)

# Replace with the desired file path and text
file_path = "../MacroTalentsSecondary.txt"
text_to_prepend = ".cheat casttime on\n"

prepend_to_file(file_path, text_to_prepend)
#Authored by mostly nick :)

# Define the input and output file paths
input_file_path = 'Input/DataStore_Talents.lua'
output_file_path = 'GlyphSpellID.txt'

# Define a regular expression pattern to match 5-digit numbers preceded by a |
pattern = re.compile(r'\|(\d{5})\b')

# Initialize a list to store the extracted 5-digit numbers
five_digit_numbers = []

# Read the input file
with open(input_file_path, 'r') as file:
    content = file.read()

    # Find all 5-digit numbers in the file content preceded by |
    matches = pattern.findall(content)
    five_digit_numbers.extend(matches)

# Write the extracted 5-digit numbers to the output file
with open(output_file_path, 'w') as file:
    for number in five_digit_numbers:
        file.write(number + '\n')
#Authored by mostly nick :)

def match_columns(glyph_file, reference_file, output_file):
    # Read the reference file into a dictionary with column 1 as key and column 137 as value
    references = {}
    with open(reference_file, 'r') as ref_file:
        ref_reader = csv.reader(ref_file, delimiter=',')
        for row in ref_reader:
            if row:  # Check if the row is non-empty
                references[row[0]] = row[136]

    # Match column 1 in glyph file with the dictionary and write the corresponding value to output file
    with open(glyph_file, 'r') as glyph_f, open(output_file, 'w', newline='') as output_f:
        glyph_reader = csv.reader(glyph_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')
        
        for row in glyph_reader:
            if row:  # Check if the row is non-empty
                glyph_id = row[0]
                if glyph_id in references:
                    output_writer.writerow([references[glyph_id]])
                else:
                    output_writer.writerow([])  # Write an empty row if no match found

# Example usage:
match_columns('GlyphSpellID.txt', 'References/Spell.txt', 'GlyphName.txt')

#Authored by mostly nick :)
# Read GlyphName.txt
with open('GlyphName.txt', 'r', encoding='utf-8') as glyph_file:
    glyph_lines = glyph_file.readlines()

# Extract glyph names from GlyphName.txt
glyph_names = [line.strip() for line in glyph_lines]

# Create a dictionary to store glyph names and their occurrences
glyph_occurrences = {}

# Count occurrences of each glyph in GlyphName.txt
for glyph_name in glyph_names:
    if glyph_name in glyph_occurrences:
        glyph_occurrences[glyph_name] += 1
    else:
        glyph_occurrences[glyph_name] = 1

# Write occurrences of each glyph to GlyphCount.txt
with open('GlyphCount.txt', 'w', encoding='utf-8') as count_file:
    for glyph_name, occurrences in glyph_occurrences.items():
        count_file.write(f"{glyph_name}:{occurrences}\n")

# Print occurrences of each glyph
for glyph_name, occurrences in glyph_occurrences.items():
    print(f"Occurrences of '{glyph_name}': {occurrences}")

#Authored by mostly nick :)

def compare_and_replace():
    # Read GlyphCount.txt
    with open('GlyphCount.txt', 'r') as glyph_file:
        glyph_lines = glyph_file.readlines()

    # Read ItemID_full.txt
    with open('References/ItemID_full.txt', 'r') as item_file:
        item_reader = csv.reader(item_file)
        item_data = list(item_reader)

    # Read playername from Recipient.txt
    with open('References/Recipient.txt', 'r') as args_file:
        playername = args_file.readline().strip()

    # Iterate through each line in GlyphCount.txt
    for i, glyph_line in enumerate(glyph_lines):
        # Get the text before the colon
        glyph_text = glyph_line.split(':')[0].strip()

        # Iterate through each row in ItemID_full.txt
        for item_row in item_data:
            # Get the text between the 4th and 5th commas
            item_text = item_row[4].strip()

            # If there's a match
            if glyph_text.casefold() == item_text.casefold():
                # Replace the matching text in GlyphCount.txt with the number from the first column of ItemID_full.txt
                glyph_lines[i] = glyph_lines[i].replace(glyph_text, item_row[0])

    # Write the modified content back to GlyphCount.txt with spaces at the end of each line
    with open('GlyphCount.txt', 'w') as glyph_file:
        for line in glyph_lines:
            glyph_file.write(line.rstrip() + ' ')

    # Prefix each line with '.send items playername'
    with open('GlyphCount.txt', 'r') as glyph_file:
        modified_lines = glyph_file.readlines()

    with open('GlyphCount.txt', 'w') as glyph_file:
        for line in modified_lines:
            glyph_file.write(f'.send items {playername} "Glyphs" "Glyphs" {line}')

    # Copy GlyphCount.txt to the output folder and rename it to GlyphMacro.txt
    shutil.copy('GlyphCount.txt', 'output/GlyphMacro.txt')

    # Delete GlyphCount.txt, GlyphSpellID.txt, and GlyphName.txt
    os.remove('GlyphCount.txt')
    os.remove('GlyphSpellID.txt')
    os.remove('GlyphName.txt')

if __name__ == "__main__":
    compare_and_replace()

#Authored by mostly nick :)

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
#Authored by mostly nick :)

def extract_numbers_from_lua(file_path):
    numbers = []
    pattern = r':(\d+)(?![|\d])'

    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        numbers.extend(matches)

    return numbers

ench_input_file1 = 'Input/DataStore_Containers.lua'
ench_input_file2 = 'Input/DataStore_Inventory.lua'
ench_reference_csv = 'References/SpellItemEnchantment.csv'
ench_recipient_file = 'References/Recipient.txt'
ench_output_folder = 'Output'

ench_numbers1 = extract_numbers_from_lua(ench_input_file1)
ench_numbers2 = extract_numbers_from_lua(ench_input_file2)

all_numbers = ench_numbers1 + ench_numbers2

temp_file = 'EnchantIDs.txt'
with open(temp_file, 'w') as file:
    for number in all_numbers:
        file.write(f'{number}\n')

reference_values = set()
with open(ench_reference_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        reference_values.add(row[0])

filtered_lines = []
with open(temp_file, 'r') as file:
    for line in file:
        if line.strip() in reference_values:
            filtered_lines.append(line)

with open(temp_file, 'w') as file:
    file.writelines(filtered_lines)
    
reference_values = {}
with open(ench_reference_csv, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        reference_values[row[0]] = row[33]
        
filtered_lines = []
with open(temp_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line in reference_values:
            filtered_lines.append(f'{reference_values[line]}\n')
        else:
            filtered_lines.append(f'{line}\n')

ench_file = 'Gems.txt'
with open(ench_file, 'w') as file:
    file.writelines(filtered_lines)

file_path = 'Gems.txt'
gemstemp_file = 'GemsTemp.txt'  # Temporary file to store non-'0' lines

# Open file.txt and filter lines
with open(file_path, 'r') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if line.strip() != '0']

# Write filtered lines to temp.txt
with open(gemstemp_file, 'w') as file:
    file.writelines(filtered_lines)

# Replace file.txt with temp.txt
os.replace(gemstemp_file, file_path)

# Open file.txt and read all lines
with open(file_path, 'r') as file:
    content = file.read()

# Replace line breaks with spaces
modified_content = content.replace('\n', ' ')

# Write modified content to temp.txt
with open(gemstemp_file, 'w') as file:
    file.write(modified_content)

# Replace file.txt with temp.txt
os.replace(gemstemp_file, file_path)


# Open file.txt and read all content
with open(file_path, 'r') as file:
    content = file.read()

# Split the content into words based on spaces
words = content.split(' ')

# Initialize a counter to keep track of spaces
space_count = 0

# Iterate through the words and insert line breaks every 12th space
modified_content = []
for word in words:
    modified_content.append(word)
    if space_count == 11:
        modified_content.append('\n')
        space_count = 0
    else:
        modified_content.append(' ')
        space_count += 1

# Join the modified content back into a single string
modified_content = ''.join(modified_content)

# Write modified content to modified_file.txt
with open(file_path, 'w') as file:
    file.write(modified_content)
    

# Read recipient name from References/Recipient.txt
with open(ench_recipient_file, 'r') as ench_recipient_file:
    recipient_name = ench_recipient_file.read().strip()

# Open file.txt and read all lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Prefix each line with '.send items Playername "Gems" "Gems"'
modified_lines = [f'.send items {recipient_name} "Gems" "Gems" {line}' for line in lines]

# Write modified lines back to file.txt
with open(file_path, 'w') as file:
    file.writelines(modified_lines)

# Define the destination path in the output folder
destination_path = os.path.join(ench_output_folder, os.path.basename(file_path))

# Copy file_path to the Output folder
shutil.copyfile(file_path, destination_path)
#Authored by mostly nick :)
def process_line(line):
    # Check if the line contains the word "Size"
    if "Size" in line:
        return None  # Skip this line
    
    # Preserve the leading whitespace (tabs or spaces)
    leading_whitespace = len(line) - len(line.lstrip())
    indentation = line[:leading_whitespace]
    
    # Check if the line has a number and a bracket
    if "[" in line and "]" in line:
        # Find the position of the equals sign
        equals_pos = line.find("=")
        if (equals_pos != -1) and ("," in line or line.strip().endswith(']')):
            # Split the line into three parts
            before_equals = line[:equals_pos].strip()
            after_equals = line[equals_pos + 1:].strip()

            # Find the position of the bracket
            bracket_start_pos = before_equals.find("[")
            bracket_end_pos = before_equals.find("]") + 1

            # Extract the bracket part
            bracket_part = before_equals[bracket_start_pos:bracket_end_pos]

            # Extract the rest of the line
            rest_of_line = after_equals

            # Reconstruct the line
            new_line = f"{rest_of_line} -- {bracket_part}\n"
            return f"{indentation}{new_line}"
    return line

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            processed_line = process_line(line)
            if processed_line is not None:
                # Replace all instances of '=' with '--' but preserve indentation
                leading_whitespace = len(line) - len(line.lstrip())
                indentation = line[:leading_whitespace]
                outfile.write(f"{indentation}{processed_line}")

# File paths
input_file = 'Input/DataStore_Containers.lua'
output_file = 'prepped.txt'

# Process the file
process_file(input_file, output_file)

#Authored by mostly nick :)
def process_entries(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('["Bag'):
            bag_name = line.split('"]')[0] + '"]'

            # Find the end of the current ["BagX"] entry
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('["Bag'):
                j += 1

            # Extract the entire entry content
            entry_lines = lines[i:j]

            # Check for '["counts"]' in the entry content
            counts_found = any('["counts"]' in entry_line for entry_line in entry_lines)

            if not counts_found:
                # Write the entire entry to a separate file
                with open('1-BagsNoCount.txt', 'a') as no_count_file:
                    no_count_file.writelines(entry_lines)

                # Remove the lines of the current ["BagX"] entry from the original list
                lines[i:j] = []
                continue

            # Move i to the end of the current ["BagX"] entry
            i = j - 1

        i += 1

    # Write back the modified content (excluding removed entries) to the original file
    with open(filename, 'w') as file:
        file.writelines(lines)

# Usage example:
filename = "prepped.txt"
process_entries(filename)
#Authored by mostly nick :)

# Define the input and output file names
input_file = 'prepped.txt'
output_file = 'preppedcount.txt'

# Initialize variables
bag_count = 0
inside_counts_block = False

# Open the input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        # Check for "Bag" and increment the bag count
        if re.search(r'\["Bag', line):
            bag_count += 1

        # Check for counts block start
        if '["counts"]' in line:
            inside_counts_block = True
        elif inside_counts_block:
            if '}' in line:
                inside_counts_block = False
            else:
                counts_id_match = re.search(r'(\d+), -- \[(\d+)\]', line)
                if counts_id_match:
                    counts_id = counts_id_match.group(1)
                    bag_id = counts_id_match.group(2)
                    f_out.write(f"{counts_id},{bag_id},{bag_count * 7}\n")  # Multiply bag_count by 7
#Authored by mostly nick :)
# Open the input file
with open('preppedcount.txt', 'r') as file:
    lines = file.readlines()

# Process the data
output_lines = []
for line in lines:
    # Strip any whitespace characters like \n at the end of each line
    line = line.strip()
    # Split the line into components
    parts = line.split(',')
    # Combine the 2nd and 3rd columns
    combined = parts[1] + parts[2]
    # Prepare the output line
    output_line = f"{parts[0]},{combined}"
    output_lines.append(output_line)

# Write the output to preppedcount2.txt
with open('preppedcount2.txt', 'w') as output_file:
    for output_line in output_lines:
        output_file.write(output_line + '\n')
#Authored by mostly nick :)

def process_file(input_file, output_file):
    # Step 1: Read file and initialize IDcount
    IDcount = 0
    with open(input_file, 'r') as f:
        lines = f.readlines()

    output_lines = []

    # Step 2: Delete empty lines and replace ' --' with ','
    lines = [line.strip().replace(' --', ',') for line in lines if line.strip()]

    # Step 3-7: Loop through lines and process '["ids"] = {' entries
    while lines:
        # Find the index of the next '["ids"] = {' entry
        start_index = next((i for i, line in enumerate(lines) if '["ids"] = {' in line), None)
        if start_index is None:
            break  # If no more '["ids"] = {' entries are found, stop processing

        IDcount += 1  # Increase IDcount

        # Find the index of the first '}' after the '["ids"] = {' entry
        end_index = next((i for i, line in enumerate(lines[start_index:]) if '}' in line), None)
        if end_index is None:
            break  # If no '}' is found, stop processing

        end_index += start_index  # Adjust end_index to the global index

        # Extract lines with numbers and append IDcount to each line
        for line in lines[start_index:end_index]:
            numbers = re.findall(r'\d+', line)
            if numbers:
                output_lines.append(f"{','.join(numbers)}{IDcount * 7}\n")

        # Remove processed lines from lines list
        lines = lines[end_index+1:]

    # Write output lines to file
    with open(output_file, 'w') as f:
        f.writelines(output_lines)


if __name__ == "__main__":
    input_file = "prepped.txt"
    output_file = "prepped3.txt"

    process_file(input_file, output_file)
#Authored by mostly nick :)
def compare_files(file1, file2, output_file):
    # Reading the first file into a dictionary
    preppedcount2 = {}
    with open(file1, 'r') as f:
        for line in f:
            if "," in line:
                col1, col2 = line.strip().split(',')
                preppedcount2[col2] = col1
            else:
                continue
    
    with open(file2, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            if "," in line:
                col1, col2 = line.strip().split(',')
            else:
                continue
            
            if col2 in preppedcount2:
                out.write(f"{col1}:{preppedcount2[col2]}\n")
            else:
                out.write(f"{col1}:1\n")

# Usage
compare_files('preppedcount2.txt', 'prepped3.txt', 'ItemOutput.txt')
#Authored by mostly nick :)
def compare_files(prepped3_file, preppedcount2_file, output_file):
    # Read lines from both files
    with open(prepped3_file, 'r') as file1, open(preppedcount2_file, 'r') as file2:
        prepped3_lines = file1.readlines()
        preppedcount2_lines = file2.readlines()

    # Create dictionaries to store values from preppedcount2.txt
    preppedcount2_dict = {}
    for line in preppedcount2_lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            key, value = parts
            preppedcount2_dict[value] = key

    # Open the output file for writing
    with open(output_file, 'w') as output:
        for line in prepped3_lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                key, value = parts
                if value in preppedcount2_dict:
                    output.write(f"{key}:{preppedcount2_dict[value]}\n")
                else:
                    output.write(f"{key}:1\n")

# Define file names
prepped3_file = 'prepped3.txt'
preppedcount2_file = 'preppedcount2.txt'
output_file = 'PreppedItemOutput.txt'

# Call the function to compare files and write output
compare_files(prepped3_file, preppedcount2_file, output_file)
#Authored by mostly nick :)
# Function to read lines from a file and return them as a list
def read_lines_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

# Function to write lines to a file without an extra newline at the end
def write_lines_to_file(filepath, lines):
    with open(filepath, 'w') as file:
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                file.write(line)
            else:
                file.write(line.rstrip('\n'))

# Function to filter lines in PreppedItemOutput.txt based on ids in References/ids_item.txt
def filter_prepped_item_output(prepped_item_file, ids_item_file, output_file):
    # Read lines from PreppedItemOutput.txt
    prepped_item_lines = read_lines_from_file(prepped_item_file)
    
    # Read lines from References/ids_item.txt and create a set of IDs for quick lookup
    ids_item_lines = read_lines_from_file(ids_item_file)
    ids_set = set(line.strip() for line in ids_item_lines)
    
    # Filter lines in PreppedItemOutput.txt
    filtered_lines = []
    for line in prepped_item_lines:
        number1, number2 = line.strip().split(':')
        if number1 in ids_set:
            filtered_lines.append(line)
    
    # Write filtered lines to PreppedItemCount_Filtered.txt without an extra newline
    write_lines_to_file(output_file, filtered_lines)

# File paths
prepped_item_file = 'PreppedItemOutput.txt'
ids_item_file = 'References/ids_item.txt'
output_file = 'PreppedItemCount_Filtered.txt'

# Run the filtering process
filter_prepped_item_output(prepped_item_file, ids_item_file, output_file)
#Authored by mostly nick :)

# Define the file paths
input_file_path = 'PreppedItemCount_Filtered.txt'
output_file_path = 'Output/AltoBagMacro.txt'
reference_file_path = 'References/Recipient.txt'

# Read the player name from the reference file
with open(reference_file_path, 'r') as ref_file:
    player_name = ref_file.read().strip()

# Read the content of the input file
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Insert a space at the end of each line
lines_with_spaces = [line.rstrip() + ' ' for line in lines]

# Join all lines into a single string to remove line breaks
single_line_output = ''.join(lines_with_spaces)

# Introduce a line break after every 12th space
output_with_line_breaks = ''
space_count = 0
for char in single_line_output:
    if char == ' ':
        space_count += 1
        if space_count == 12:
            output_with_line_breaks += char + '\n'
            space_count = 0
        else:
            output_with_line_breaks += char
    else:
        output_with_line_breaks += char

# Prefix every line with '.send items Playername "Items" "Items" '
prefix = f'.send items {player_name} "Items" "Items" '
output_with_prefix = prefix + output_with_line_breaks.replace('\n', f'\n{prefix}')

# Write the modified content to the output file
with open(output_file_path, 'w') as file:
    file.write(output_with_prefix)

#print("File processing complete. Output written to AltoBagMacro.txt.")

# Delete specified files
files_to_delete = ['prepped.txt', 'prepped2.txt', 'prepped3.txt', 'preppedcount.txt', 'PreppedItemCount_Filtered.txt', 'preppedcount2.txt', 'ItemOutput.txt', 'PreppedItemOutput.txt']
for file_name in files_to_delete:
    if os.path.exists(file_name):
        os.remove(file_name)
        #print(f"Deleted {file_name}")
#Authored by mostly nick :)
def read_file(filepath):
    """Read the content of a file and return it as a list of lines."""
    with open(filepath, 'r') as file:
        return file.readlines()

def write_file(filepath, content):
    """Write a list of lines to a file."""
    with open(filepath, 'w') as file:
        file.writelines(content)

def process_files(altobagmacro_path, items_to_remove_path):
    # Read the contents of both files
    altobagmacro_lines = read_file(altobagmacro_path)
    items_to_remove_lines = read_file(items_to_remove_path)
    
    # Remove trailing newlines and spaces from items to remove
    items_to_remove = set(line.strip() for line in items_to_remove_lines)
    
    # Process each line of AltoBagMacro
    updated_lines = []
    for line in altobagmacro_lines:
        # Split the line by spaces and filter out items that need to be removed
        parts = line.split()
        new_parts = [part for part in parts if part not in items_to_remove]
        updated_lines.append(' '.join(new_parts) + '\n')
    
    # Write the updated lines back to the AltoBagMacro file
    write_file(altobagmacro_path, updated_lines)

# Paths to the files
altobagmacro_path = 'Output/AltoBagMacro.txt'
items_to_remove_path = 'References/ItemsToRemove.txt'

# Process the files
process_files(altobagmacro_path, items_to_remove_path)

print("Processing complete. Items have been removed from AltoBagMacro.")


def remove_37711_from_line(file_path):
  """Removes '37711:(any number)' from each line in the specified file.

  Args:
    file_path: The path to the file to modify.
  """

  with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    file.truncate()

    for line in lines:
      line = re.sub(r' 37711:\d+', '', line)  # Remove leading space
      file.write(line)

if __name__ == '__main__':
  file_path = 'Output/AltoBagMacro.txt'
  remove_37711_from_line(file_path)
#Authored by mostly nick :)

# Regex pattern to match numbers of 3-, 4-, or 5-digits
number_pattern = r'\b\d{3,5}\b'

# Input and output file paths
input_file = '1-BagsNoCount.txt'
output_file = 'Output/BagsWithoutCounts.txt'
recipient_file = 'References/Recipient.txt'  # Path to recipient file

# Function to extract numbers from a line
def extract_numbers(line):
    return re.findall(number_pattern, line)

# Function to read player_name from recipient file
def read_player_name(file_path):
    with open(file_path, 'r') as f:
        return f.readline().strip()

# Check if input file exists
if os.path.exists(input_file):
    # Get player_name from recipient file
    player_name = read_player_name(recipient_file)

    # Open input and output files
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Initialize a list to store all extracted numbers
        all_numbers = []

        # Iterate through each line in the input file
        for line in f_in:
            # Check if the line contains "Hitem" or "interface"
            if 'Hitem' in line or 'interface' in line:
                continue  # Skip the line if it contains these words
            
            # Extract numbers from the line
            numbers = extract_numbers(line)
            
            # Add extracted numbers to all_numbers list
            all_numbers.extend(numbers)

        # Ensure all_numbers contains unique numbers in the order they first appeared
        unique_numbers = []
        seen = set()
        for number in all_numbers:
            if number not in seen:
                unique_numbers.append(number)
                seen.add(number)

        # Split unique_numbers into batches of up to 12 numbers
        for i in range(0, len(unique_numbers), 12):
            batch = unique_numbers[i:i+12]
            # Format the output line with .send items {player_name} "Items" "Items"
            output_line = f'.send items {player_name} "Items" "Items" {" ".join(batch)}\n'
            f_out.write(output_line)

    # Delete the input file after processing
    os.remove(input_file)
#Authored by mostly nick :)

def extract_link_numbers(input_filename, output_filename):
    # Check if Recipient.txt exists and has content
    if os.path.exists('References/Recipient.txt'):
        with open('References/Recipient.txt', 'r') as player_file:
            playername = player_file.read().strip()
        
        if not playername:
            playername = input("Please enter the player name: ").strip()
            with open('References/Recipient.txt', 'w') as player_file:
                player_file.write(playername)
                print(f"Player name '{playername}' written to References/Recipient.txt.")
    else:
        playername = input("Please enter the player name: ").strip()
        with open('References/Recipient.txt', 'w') as player_file:
            player_file.write(playername)
            print(f"Player name '{playername}' written to References/Recipient.txt.")

    with open(input_filename, 'r') as file:
        lines = file.readlines()
    
    pattern = r'\|Hitem:(\d{5}):'
    matches = []

    for line in lines:
        if '["link"]' in line:
            match = re.search(pattern, line)
            if match:
                matches.append(match.group(1))
    
    with open(output_filename, 'w') as file:
        for i in range(0, len(matches), 12):
            items = ' '.join(matches[i:i+12])
            file.write(f'.send items {playername} "Bags" "Bags" {items}\n')

# Use the function
input_filename = 'Input/DataStore_Containers.lua'
output_filename = 'Output/BagIDs.txt'
extract_link_numbers(input_filename, output_filename)
#Authored by mostly nick :)

def read_lua_file(file_path):
    """Reads the content of a LUA file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_achievement_ids(lines):
    """Extracts achievement IDs from lines containing 'true'."""
    achievement_ids = []
    for line in lines:
        if "true" in line:
            match = re.search(r'\b(\d+)', line)
            if match:
                achievement_ids.append(match.group(1))
    return achievement_ids

def write_achievement_commands(achievement_ids, output_file, excluded_ids):
    """Writes sorted achievement add commands to the output file, excluding specific IDs."""
    with open(output_file, 'w') as file:
        for achievement_id in sorted(achievement_ids, key=int):
            if achievement_id not in excluded_ids:
                file.write(f".achievement add {achievement_id}\n")

def main():
    input_file = 'Input/DataStore_Achievements.lua'
    output_file = 'Output/AchievementGranter.txt'
    excluded_ids = {str(i) for i in range(1, 14)}  # IDs to exclude

    #print(f"Reading LUA file: {input_file}")
    lines = read_lua_file(input_file)
    #print("Extracting achievement IDs...")
    
    achievement_ids = extract_achievement_ids(lines)
    #print(f"Found {len(achievement_ids)} achievements to add.")

    #print(f"Writing sorted achievement add commands to '{output_file}'...")
    write_achievement_commands(achievement_ids, output_file, excluded_ids)
    #print("Achievement add commands have been written to the output file.")
    #print("Processing complete.")

if __name__ == '__main__':
    main()
#Authored by mostly nick :)

def extract_numbers(input_file, output_file):
    """
    Extracts all numbers from each line of a file, filtering out first, last, and values above 99999, reverses the order, separates them with colon (:), prefixes each line with '.additem', and writes non-empty lines without ':0' to another file.

    Args:
        input_file: Path to the file containing the data.
        output_file: Path to the file where the filtered and reversed numbers will be written.
    """
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            # Use regular expression to find one or more digits (\d+)
            numbers = re.findall(r'\d+', line)
            # Filter out first and last values (slice from index 1 to -1)
            filtered_numbers = numbers[1:-1]
            # Filter out numbers above 99999
            filtered_numbers = [num for num in filtered_numbers if int(num) <= 99999]
            # Filter out the number 37742
            filtered_numbers = [num for num in filtered_numbers if num != '37742']
            # Reverse the order of filtered numbers
            filtered_numbers.reverse()
            # Join filtered numbers with colon (:)
            joined_numbers = " ".join(filtered_numbers)
            # Check if the line doesn't contain ":0" and write if not empty
            if filtered_numbers and ":0" not in joined_numbers:
                f_out.write(".additem " + joined_numbers + "\n")
        # Append .additem 0 -99 to the end of the output
        f_out.write(".additem 0 -99\n")
        f_out.write(".additem 37742 -9999\n")

if __name__ == "__main__":
    input_file = "Input/DataStore_Currencies.lua"
    output_file = "Output/CurrencyOutput.txt"
    extract_numbers(input_file, output_file)
#Authored by mostly nick :)

def extract_number(line):
    # Regex pattern to match 5-digit number
    five_digit_pattern = r"(?<![.\d])\d{5}(?!\d)"
    # Regex pattern to match 4-digit number (if no 5-digit found)
    four_digit_pattern = r"(?<![.\d])\d{4}(?!\d)"
  
    # Check for lines containing ["lastUpdate"] or ["averageItemLvl"]
    if '["lastUpdate"]' in line or '["averageItemLvl"]' in line:
        return None
    
    # List of numbers to exclude
    excluded_numbers = ["6948", "70613", "59569", "54729", "10677", "73313", "76154", "49379", "72286"]

    five_digit_match = re.search(five_digit_pattern, line)
    if five_digit_match:
        extracted_number = five_digit_match.group()
        if extracted_number not in excluded_numbers and int(extracted_number) <= 90000:
            return extracted_number
        return None
    
    four_digit_match = re.search(four_digit_pattern, line)
    if four_digit_match:
        extracted_number = four_digit_match.group()
        if extracted_number not in excluded_numbers:
            return extracted_number
    
    return None


def write_formatted_output(output_file, entries, playername):
    """Writes the list of entries to the output file, separated by spaces and limited to 12 per line, with a prefix at the beginning. Skips blank entries.

    Args:
        output_file: The opened file object for writing.
        entries: A list of strings to be written.
        playername: The player name to substitute in the output prefix.
    """
    prefix = f".send items {playername} \"Items\" \"items\""
    # Limit to 12 entries per line
    for i in range(0, len(entries), 12):
        # Only include non-empty entries in the output
        filtered_entries = [entry for entry in entries[i:i+12] if entry]
        if filtered_entries:  # Check if there are any non-empty entries
            # Join entries with spaces and add newline
            output_file.write(prefix + " " + " ".join(filtered_entries) + "\n")


# Specify the filename for input and output files
input_filename = "Input/DataStore_Inventory.lua"
output_filename = "Output/InventoryOutput.txt"

# Function to read playername from Recipient.txt or prompt user for input
def get_playername():
    if os.path.exists('References/Recipient.txt'):
        with open('References/Recipient.txt', 'r') as player_file:
            playername = player_file.read().strip()
        
        if not playername:
            playername = input("Please enter the player name: ").strip()
            with open('References/Recipient.txt', 'w') as player_file:
                player_file.write(playername)
                print(f"Player name '{playername}' written to References/Recipient.txt.")
    else:
        playername = input("Please enter the player name: ").strip()
        with open('References/Recipient.txt', 'w') as player_file:
            player_file.write(playername)
            print(f"Player name '{playername}' written to References/Recipient.txt.")
    
    return playername

try:
    # Open the input file in read mode
    with open(input_filename, "r") as input_file:
        # Open the output file in write mode (overwrite existing content)
        with open(output_filename, "w") as output_file:
            entries = []  # List to store extracted numbers/messages
            for line in input_file:
                extracted_number = extract_number(line.strip())
                if extracted_number:
                    entries.append(f"{extracted_number}")
            # Get playername
            playername = get_playername()
            # Write formatted output
            write_formatted_output(output_file, entries, playername)
except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
#Authored by mostly nick :)
def extract_info(input_file, temp_file):
    """
    Extracts words between first two quotation marks and only digits from the last number per line,
    skipping lines without a number between -43000 and 43000, and removes all apostrophes.
    The output format separates the first and second entries (excluding "lastupdate") with a colon (:).

    Args:
        input_file: Path to the input file.
        temp_file: Path to the temporary file (previously output_file).
    """
    with open(input_file, 'rb') as f_in, open(temp_file, 'w') as f_temp:
        lines = f_in.readlines()
        
        for line in lines:
            line = line.decode('utf-8')  # Decode for potential hidden characters
            
            # Check if the line contains a number between -43000 and 43000
            if not "lastUpdate" in line:
                # Split the line based on quotes
                parts = line.strip().split('"')
                
                # Check if there are at least 3 parts (2 quotes and content)
                if len(parts) >= 3:
                    # Extract text between first two quotes and remove apostrophes
                    text = parts[1].replace("'", "")
                    
                    # Split the line by pipe (|) and get the last part
                    last_part = line.split("|")[-1]
                    
                    # Extract the number from the last part while preserving the negative sign if present
                    number = ''.join(c for c in last_part if c.isdigit() or c == '-')
                    
                    # Check if the extracted number is within the range -43000 to 43000
                    if number:
                        number_value = int(number)
                        if -43000 <= number_value <= 43000:
                            # Remove "lastupdate" from the second column (digits)
                            number_without_update = number.rsplit('lastupdate', 1)[0].strip()
                            
                            # Combine text and number with colon separator
                            temp_line = f"{text}:{number_without_update}\n"
                            f_temp.write(temp_line)

# Example usage
input_file = "Input/DataStore_Reputations.lua"
temp_file = "temp.txt"
extract_info(input_file, temp_file)

#Authored by mostly nick :)

def compare_and_create_output(temp_file, ids_file):
  """
  Compares names in column 1 of temp.txt to IDs in table 2 (IDs.txt).
  If a match is found, creates a new line with the matching ID, a space, and the corresponding value from temp.txt.
  Prefixes each output line with ".mod reputation ".
  Deletes the temporary file (temp.txt) after processing.

  Args:
    temp_file: Path to the temporary file containing data (name-value pairs).
    ids_file: Path to the file containing IDs (format: "ID;Name").
  """

  # Create a dictionary to store ID data (name as key, ID as value)
  id_data = {}
  for line in open(ids_file, 'r'):
    parts = line.strip().split(';')
    if len(parts) == 2:
      id_data[parts[1]] = parts[0]  # Name is key, ID is value

  # Read lines from temp_file
  with open(temp_file, 'r') as f_temp:
    lines = f_temp.readlines()

  # Create output lines
  output_lines = []
  for line in lines:
    name, value = line.strip().split(':')  # Split by colon (:)
    if name in id_data:
      output_lines.append(f".mod reputation {id_data[name]} {value}\n")  # Combine ID, space, and value

  # Write output lines to a new file (e.g., output.txt)
  with open("Output/FactionOutput.txt", 'w') as f_out:
    f_out.writelines(output_lines)

  # Delete the temporary file
  os.remove(temp_file)  # Use os.remove to delete the file

# Example usage
temp_file = "temp.txt"
ids_file = "References/IDs.txt"

# Compare and create output
compare_and_create_output(temp_file, ids_file)
#Authored by Zyyn
def extract_numbers(input_file, output_file):
    seen_numbers = set()  # Set to track seen numbers
    
    # Set of numbers to skip
    skip_numbers = {
        '70613', '69002', '61773', '44841', '44842', '44843', 
        '60025', '59961', '40990', '68187', '68188', '60119', 
        '60118', '72808', '72807', '63956', '63963', '60024', 
        '61472'
    }
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.split('|')
            if len(parts) > 2:
                try:
                    second_number = parts[2].strip().split()[0]
                    # Check if the number is not in the skip list and not already seen
                    if second_number not in skip_numbers and second_number not in seen_numbers:
                        seen_numbers.add(second_number)
                        outfile.write(f".learn {second_number}\n")
                except IndexError:
                    print(f"Skipping line due to unexpected format: {line}")
                except ValueError:
                    print(f"Skipping line due to value conversion issue: {line}")

if __name__ == "__main__":
    input_file = 'Input/DataStore_Pets.lua'  # Input file name
    output_file = 'Output/PetImport.txt'  # Output file name with .txt extension
    extract_numbers(input_file, output_file)
#Authored by mostly nick :)

def extract_money_numbers(filename):
    money_numbers = []

    # Open the file for reading
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Search for the word "money" in the line
            if 'money' in line.lower():
                # Extract numbers from the line using regular expression
                numbers = re.findall(r'\b\d+\b', line)
                # Add extracted numbers to the list
                money_numbers.extend(numbers)

    return money_numbers

# Input and output file paths
input_filename = 'Input/DataStore_Characters.lua'
output_filename = 'Output/Z-Gold.txt'

# Extract money numbers
money_numbers = extract_money_numbers(input_filename)

# Write the extracted numbers to the output file with the prefix
with open(output_filename, 'w') as outfile:
    for number in money_numbers:
        outfile.write(f".modify money {number}\n")

# Print the count of extracted numbers
print(f"Copper extracted: {number}")
#Authored by mostly nick :)
with open('Output/AchievementGranter.txt', 'r') as input_file:
    # Read all lines from the file
    lines = input_file.readlines()

with open('Output/X0-DualSpecialization.txt', 'w') as output_file:
    # Iterate through each line in the input file
    for line in lines:
        # Check if the line contains the number 2716
        if '2716' in line:
            # If it does, write the desired output to the output file
            output_file.write(".cast 63680\n.cast 63624\n")
            break  # Stop searching after finding the first occurrence

#print("Dual Talent Specialization captured.")
#Authored by mostly nick :)

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
#Authored by mostly nick :)

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
#Authored by mostly nick :)
def delete_lines_with_specific_text(input_file, output_file):
    # Open input file for reading
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    # Open output file for writing
    with open(output_file, "w") as output_f:
        # Iterate through each line
        for line in lines:
            # Check if the line contains the text "1, 1"
            if "1, 1" in line:
                continue  # Skip this line

            # Check if the line contains the word "Language"
            if "Language" in line:
                continue  # Skip this line

            # Split the line into columns
            columns = line.split()
            # Check if the second column contains '1'
            if columns[1] != "1":
                # Write the line to the output file
                output_f.write(line)

# Paths to input and output files
input_file = "10-skills.txt"
output_file = "11-skills.txt"

# Call the function to delete lines with specific text
delete_lines_with_specific_text(input_file, output_file)
#Authored by mostly nick :)
def replace_skills(input_file, output_file):
    cooking_mapping = {
        75: "2550",
        150: "3102",
        225: "3413",
        300: "18260",
        375: "33359",
        450: "51296"
    }

    riding_mapping = {
        75: "33388",
        150: "33391",
        225: "34090 \n.learn 54197",
        300: "34091 \n.learn 51497"
    }

    fishing_mapping = {
        75: "7620",
        150: "7731",
        225: "7732",
        300: "18248",
        375: "33095",
        450: "51294"
    }

    first_aid_mapping = {
        75: "3273",
        150: "3274",
        225: "7924",
        300: "10846",
        375: "27028",
        450: "45542"
    }

    alchemy_mapping = {
        75: "2259",
        150: "3101",
        225: "3464",
        300: "11611",
        375: "28596",
        450: "51304"
    }

    blacksmithing_mapping = {
        75: "2018",
        150: "3100",
        225: "3538",
        300: "9785",
        375: "29844",
        450: "51300"
    }

    enchanting_mapping = {
        75: "7411",
        150: "7412",
        225: "7413",
        300: "13920",
        375: "28029",
        450: "51313"
    }

    engineering_mapping = {
        75: "4036",
        150: "4037",
        225: "4038",
        300: "12656",
        375: "30350",
        450: "51306"
    }

    herbalism_mapping = {
        75: "2366",
        150: "2368",
        225: "3570",
        300: "11993",
        375: "28695",
        450: "50300"
    }

    inscription_mapping = {
        75: "45357",
        150: "45358",
        225: "45359",
        300: "45360",
        375: "45361",
        450: "45363"
    }

    jewelcrafting_mapping = {
        75: "25229",
        150: "25230",
        225: "28894",
        300: "28894",
        375: "28897",
        450: "51311"
    }

    leatherworking_mapping = {
        75: "2108",
        150: "3104",
        225: "3811",
        300: "10662",
        375: "32549",
        450: "51302"
    }

    mining_mapping = {
        75: "2575",
        150: "2576",
        225: "3564",
        300: "10248",
        375: "29354",
        450: "50310"
    }

    skinning_mapping = {
        75: "8613",
        150: "8617",
        225: "8618",
        300: "10768",
        375: "32678",
        450: "50305"
    }

    tailoring_mapping = {
        75: "3908",
        150: "3909",
        225: "3910",
        300: "12180",
        375: "26790",
        450: "51309"
    }

    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    with open(output_file, "w") as output_f:
        for line in lines:
            columns = line.split(", ")
            if columns[0].strip() == "Cooking" and columns[2].strip().isdigit():
                cooking_skill = int(columns[2].strip())
                if cooking_skill in cooking_mapping:
                    output_f.write(f".learn {cooking_mapping[cooking_skill]}\n")
            elif columns[0].strip() == "Riding" and columns[2].strip().isdigit():
                riding_skill = int(columns[2].strip())
                if riding_skill in riding_mapping:
                    output_f.write(f".learn {riding_mapping[riding_skill]}\n")
            elif columns[0].strip() == "Fishing" and columns[2].strip().isdigit():
                fishing_skill = int(columns[2].strip())
                if fishing_skill in fishing_mapping:
                    output_f.write(f".learn {fishing_mapping[fishing_skill]}\n")
            elif columns[0].strip() == "First Aid" and columns[2].strip().isdigit():
                first_aid_skill = int(columns[2].strip())
                if first_aid_skill in first_aid_mapping:
                    output_f.write(f".learn {first_aid_mapping[first_aid_skill]}\n")
            elif columns[0].strip() == "Alchemy" and columns[2].strip().isdigit():
                alchemy_skill = int(columns[2].strip())
                if alchemy_skill in alchemy_mapping:
                    output_f.write(f".learn {alchemy_mapping[alchemy_skill]}\n")
            elif columns[0].strip() == "Blacksmithing" and columns[2].strip().isdigit():
                blacksmithing_skill = int(columns[2].strip())
                if blacksmithing_skill in blacksmithing_mapping:
                    output_f.write(f".learn {blacksmithing_mapping[blacksmithing_skill]}\n")
            elif columns[0].strip() == "Enchanting" and columns[2].strip().isdigit():
                enchanting_skill = int(columns[2].strip())
                if enchanting_skill in enchanting_mapping:
                    output_f.write(f".learn {enchanting_mapping[enchanting_skill]}\n")
            elif columns[0].strip() == "Engineering" and columns[2].strip().isdigit():
                engineering_skill = int(columns[2].strip())
                if engineering_skill in engineering_mapping:
                    output_f.write(f".learn {engineering_mapping[engineering_skill]}\n")
            elif columns[0].strip() == "Herbalism" and columns[2].strip().isdigit():
                herbalism_skill = int(columns[2].strip())
                if herbalism_skill in herbalism_mapping:
                    output_f.write(f".learn {herbalism_mapping[herbalism_skill]}\n")
            elif columns[0].strip() == "Inscription" and columns[2].strip().isdigit():
                inscription_skill = int(columns[2].strip())
                if inscription_skill in inscription_mapping:
                    output_f.write(f".learn {inscription_mapping[inscription_skill]}\n")
            elif columns[0].strip() == "Jewelcrafting" and columns[2].strip().isdigit():
                jewelcrafting_skill = int(columns[2].strip())
                if jewelcrafting_skill in jewelcrafting_mapping:
                    output_f.write(f".learn {jewelcrafting_mapping[jewelcrafting_skill]}\n")
            elif columns[0].strip() == "Leatherworking" and columns[2].strip().isdigit():
                leatherworking_skill = int(columns[2].strip())
                if leatherworking_skill in leatherworking_mapping:
                    output_f.write(f".learn {leatherworking_mapping[leatherworking_skill]}\n")
            elif columns[0].strip() == "Mining" and columns[2].strip().isdigit():
                mining_skill = int(columns[2].strip())
                if mining_skill in mining_mapping:
                    output_f.write(f".learn {mining_mapping[mining_skill]}\n")
            elif columns[0].strip() == "Skinning" and columns[2].strip().isdigit():
                skinning_skill = int(columns[2].strip())
                if skinning_skill in skinning_mapping:
                    output_f.write(f".learn {skinning_mapping[skinning_skill]}\n")
            elif columns[0].strip() == "Tailoring" and columns[2].strip().isdigit():
                tailoring_skill = int(columns[2].strip())
                if tailoring_skill in tailoring_mapping:
                    output_f.write(f".learn {tailoring_mapping[tailoring_skill]}\n")
            elif columns[0].strip() == "Lockpicking" and columns[2].strip().isdigit():
                    output_f.write(f"")
            else:
                output_f.write(line)

input_file = "11-skills.txt"
output_file = "12-skills.txt"

replace_skills(input_file, output_file)
#Authored by mostly nick :)
def extract_armor(filename, output_file):

  armor_codes = {
      "Plate Mail": 293,
      "Mail": 413,
      "Shield": 433,
  }
  with open(filename, 'r') as f, open(output_file, 'w') as out_file:
    for line in f:
      written_armor = False
      for armor_type in armor_codes:
        if armor_type in line and not written_armor:
          code = armor_codes[armor_type]
          if code is not None:
            out_file.write(".setskill " + str(code) + " 1\n")
          written_armor = True
          break  
          
input_file = "10-skills.txt"
output_file = "Output/Armor.txt"

extract_armor(input_file, output_file)
#Authored by mostly nick :)

def replace_lines(input_file, output_file):
    # Define the mapping of words to numbers
    replacement_mapping = {
        "Two-Handed Maces": "160",
        "Mail": "413",
        "Swords": "43",
        "Axes": "44",
        "Fist Weapons": "473",
        "Unarmed": "162",
        "Plate Mail": "293",
        "Plate": "293",
        "Thrown": "176",
        "Poisons": "40",
        "Shield": "433",
        "Dual Wield": "118",
        "Polearms": "229",
        "Two-Handed Swords": "55",
        "Two-Handed Axes": "172",
        "Guns": "46",
        "Runeforging": "776",
        "Staves": "136",
        "Crossbows": "226",
        "Maces": "54",
        "Wands": "228",
        "Daggers": "173",
        "Protection": "267",
        "Swimming": "155",
        "Bows": "45",
        "Frost": "771",
        "Defense": "95"
    }

    # Open input file for reading
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    # Open output file for writing
    with open(output_file, "w") as output_f:
        # Iterate through each line
        for line in lines:
            # Split the line into columns
            columns = line.split(", ")

            # Check if the first column is in the replacement mapping
            if columns[0].strip() in replacement_mapping:
                # Skip this line if it matches any skill in the replacement mapping
                continue

            # Write the original line to the output file
            output_f.write(line)

    # Delete the input file
    os.remove(input_file)
    # Move the output file to the Output folder
    os.replace(output_file, os.path.join("Output", output_file))

# Paths to input and output files
input_file = "12-skills.txt"
output_file = "SkillSpellIDMacro.txt"

# Call the function to replace lines with specified strings before the colon and delete the "Defense" line
replace_lines(input_file, output_file)
#Authored by mostly nick :)

# Skill mapping dictionary containing profession names as keys and skill IDs as values
skill_mapping = {
    "Two-Handed Maces": "160",
    "Mail": "413",
    "Swords": "43",
    "Axes": "44",
    "Fist Weapons": "473",
    "Unarmed": "162",
    "Plate Mail": "293",
    "Thrown": "176",
    "Poisons": "40",
    "Shield": "433",
    "Dual Wield": "118",
    "Polearms": "229",
    "Two-Handed Swords": "55",
    "Two-Handed Axes": "172",
    "Guns": "46",
    "Runeforging": "776",
    "Staves": "136",
    "Crossbows": "226",
    "Maces": "54",
    "Wands": "228",
    "Daggers": "173",
    "Protection": "267",
    "Swimming": "155",
    "Bows": "45",
    "Frost": "771",
    "Alchemy": "171",
    "Blacksmithing": "164",
    "Enchanting": "333",
    "Engineering": "202",
    "Herbalism": "182",
    "Inscription": "773",
    "Jewelcrafting": "755",
    "Leatherworking": "165",
    "Mining": "186",
    "Skinning": "393",
    "Tailoring": "197",
    "Cooking": "185",
    "Fishing": "356",
    "Riding": "762",
    "First Aid": "129",
    "Lockpicking": "633",
    "Defense": "95"
}

def replace_professions(input_file, output_file):
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    with open(output_file, "w") as output_f:
        for line in lines:
            columns = line.split(", ")
            if columns[0].strip() in skill_mapping:
                skill_id = skill_mapping[columns[0].strip()]
                output_f.write(f".setskill {skill_id} {columns[1].strip()}\n")
            else:
                output_f.write(line)

    # Delete the input files after processing
    os.remove(input_file)

# Paths to input and output files
input_file = "11-skills.txt"
output_file = "Output/SkillLevels.txt"

# Call the function to replace profession names with skill IDs
replace_professions(input_file, output_file)

#print("Profession names replaced with corresponding Skill IDs.")

# Delete the remaining input file
os.remove("10-skills.txt")

#Authored by mostly nick :)

def find_lua_file(filename):
  if os.path.isfile(filename):
    return filename
  else:
    return None

def remove_line_breaks_and_tabs(filename):
  with open(filename, 'r') as f:
    content = f.read()

  modified_content = content.replace('{\n', '{').replace('\t', '')

  with open('tempquest.txt', 'w') as f:
    f.write(modified_content)

lua_file = find_lua_file('Raw/EveryQuestData.lua')

if lua_file:
  remove_line_breaks_and_tabs(lua_file)
else:
  print("ERROR: EveryQuestData.lua not found. Please check that file is present if transferring quest progress.")
#Authored by mostly nick :)

# Check if "tempquest.txt" exists
if os.path.exists("tempquest.txt"):
  # Open the input file (if it exists)
  with open("tempquest.txt", "r") as infile:
    # Open the output file
    with open("Output/3-QuestMacro.txt", "w") as outfile:
      # Initialize count
      count = 0
      # Iterate through each line in the input file
      for line in infile:
        # Check if the line contains ["status"] = 2
        if '["status"] = 2' in line:
          # Extract the number within the square brackets
          match = re.search(r'\[(\d+)\]', line)
          # Write the number (if found) prefixed with ".quest complete" to the output file
          if match:
            count += 1
            examplenumber = match.group(1)
            # Divide count by 1000
            count_in_thousands = count / 1000
            if count > 2000:  # Check if count is above 2000
              outfile.write(f"/in {count_in_thousands:.1f} /s #qc {examplenumber}\n")
            else:
              outfile.write(f"/s #qc {examplenumber}\n")

  # Write additional lines to the output file
  with open("Output/3-QuestMacro.txt", "a") as outfile:
    outfile.write(".unaura 61043\n")
    outfile.write(".unaura 35076\n")
    outfile.write(".modify money -999999999\n")

  # Delete the tempquest.txt file
  os.remove("tempquest.txt")
#Authored by Lortz
with open("Output/2-macro_quests.txt",'w') as out, open("Input/DataStore_Quests.lua","r") as fi:
	text=fi.readlines()
	for line in text:
		if "Hquest:" in line:
			out.write(".quest add " + line.split(":")[1]+"\n")

#Authored by mostly nick :)

def create_and_write_file(file_path, text):
  """Creates a file at the specified path and writes the given text to it."""
  try:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if needed
    with open(file_path, "w") as file:
      file.write(text)
  except Exception as e:
    print(f"Error creating or writing to file: {e}")

if __name__ == "__main__":
  file_path = "Output/Z-Z-InnTeleport.txt"
  text = ".gm visible on\n.tele dalainn\n"
  create_and_write_file(file_path, text)


#Authored by mostly nick :)

def combine_text_files(folder_path, output_file):
    """
    Combines all text files in a folder into a single output file.

    Args:
        folder_path: Path to the folder containing the text files.
        output_file: Path to the output file where the combined content will be written.
    """
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Open the output file in write mode to start with onset commands
    with open(output_file, "w") as output:
        #output.write(".gm on\n")
        output.write("/target [@target,noexists] player\n")
        output.write(".character customize\n")

    # Open the output file in append mode
    with open(output_file, "a") as output:
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Check if it's a text file and not CombinedMacroOutput.txt
            if filename.endswith(".txt") and filename != "CombinedMacroOutput.txt":
                # Open the file in read mode
                with open(os.path.join(folder_path, filename), "r") as file:
                    # Read the content and write it to the output file
                    content = file.read()
                    output.write(content + "\n\n")  # Add a double newline for separation

    #print(f"Combined text files from '{folder_path}' to '{output_file}'.")

    # Write the .additem command to the output file
   # with open(output_file, "a") as output:
       # output.write(".additem 0 -99\n")
       # output.write(".kick\n")
       # output.write('/in 10 /run if UnitIsUnit("target", "player") then Logout() end')

# Get folder path and output file name from user (optional)
# folder_path = input("Enter the folder path containing text files: ")
# output_file = input("Enter the name of the output file: ")

# Example usage with predefined paths
folder_path = "Output"
output_file = "../CombinedMacroOutput.txt"

combine_text_files(folder_path, output_file)


os.remove("temp_output.txt")
os.remove("main_spec.txt")
os.remove("sec_spec.txt")
#os.remove("out_macro_file.txt")
#Authored by mostly nick :)

def copy_files_to_parent_directories(source_dir):
    # Get the absolute path of the current directory
    current_dir = os.getcwd()
    
    # Define the paths of the target directories
    target_dir1 = os.path.abspath(os.path.join(current_dir, 'Output/'))

    # Define the source directory
    source_dir = os.path.abspath(source_dir)

    # Define the filename to copy
    filename = "CombinedMacroOutput.txt"

    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Check if the source directory is indeed a directory
    if not os.path.isdir(source_dir):
        print(f"'{source_dir}' is not a directory.")
        return

    # Check if the target directories exist, if not, create them
    for target_dir in [target_dir1]:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    # Iterate over the files in the source directory
    for file in os.listdir(source_dir):
        # Check if the file is named "CombinedMacroOutput"
        if file == filename:
            # Construct the source and target file paths
            source_file = os.path.join(source_dir, file)
            target_file1 = os.path.join(target_dir1, file)

            # Copy the file to the target directories
            shutil.copyfile(source_file, target_file1)
            #print(f"File '{file}' copied to '{target_dir1}'.")

# Define the source directory
source_directory = '..'

# Call the function to copy files
copy_files_to_parent_directories(source_directory)
#Authored by mostly nick :)

# Get current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Filter out only .txt files
txt_files = [file for file in files if file.endswith('.txt')]

# Delete each .txt file
for txt_file in txt_files:
    file_path = os.path.join(current_directory, txt_file)
    os.remove(file_path)
#Authored by mostly nick :)
# Open the file for reading
with open('Input/DataStore_Characters.lua', 'r') as file:
    lines = file.readlines()

# Initialize variables to store class and race
char_class = None
char_race = None

# Iterate through each line in the file
for line in lines:
    # Look for lines containing ["class"]
    if '["class"]' in line:
        # Split the line by '=' to get the part after '='
        parts = line.split('=')
        # Trim any whitespace from the parts and remove surrounding quotes and comma
        char_class = parts[1].strip().strip('", \n')

    # Look for lines containing ["race"]
    elif '["race"]' in line:
        # Split the line by '=' to get the part after '='
        parts = line.split('=')
        # Trim any whitespace from the parts and remove surrounding quotes and comma
        char_race = parts[1].strip().strip('", \n')

# Print the formatted output
if char_class:
    print(f"Class: {char_class}")

if char_race:
    print(f"Race: {char_race}")
