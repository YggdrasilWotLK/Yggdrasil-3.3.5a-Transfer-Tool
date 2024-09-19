#Authored by mostly nick :)
import re
import csv
import os
import shutil

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