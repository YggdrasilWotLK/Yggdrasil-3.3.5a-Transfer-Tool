import os

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

#print("Cleanup complete.")