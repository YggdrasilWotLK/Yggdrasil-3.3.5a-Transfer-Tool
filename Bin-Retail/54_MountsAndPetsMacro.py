#Authored by mostly nick :)
import os
import glob

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
