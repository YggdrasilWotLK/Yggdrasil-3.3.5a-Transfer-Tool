#Authored by mostly nick :)
import glob
import re
import os

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
