import sys
import os
import glob
import re
import shutil

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
