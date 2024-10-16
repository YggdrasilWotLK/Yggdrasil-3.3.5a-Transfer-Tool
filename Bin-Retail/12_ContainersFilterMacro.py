# Open the input file for reading
with open('Output/10-ContainersSplit.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Open the output file for writing
with open('Output/11-ContainersFiltered.txt', 'w') as file:
    # Define the set of numbers to filter out
    exclude_numbers = {'6948', '44810', '44430', '43824', '43348', '40643', '49054', '49052', '43349', '43300', '53010', '52369', '46753', '52328', '52078', '54849'}
    
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

# Initialize the processed data list
processed_data = []
temp_line = []

# Iterate over units and introduce line shifts as necessary
for unit in units:
    number, value = unit.split(':')
    # Check if the value is greater than 20
    if int(value) > 20:
        # If we have units in the temp_line, join them and add to processed data
        if temp_line:
            processed_data.append(' '.join(temp_line))
            temp_line = []
        # Add the current unit and add it as a new line
        processed_data.append(unit)
    else:
        temp_line.append(unit)

# Add any remaining units in temp_line
if temp_line:
    processed_data.append(' '.join(temp_line))

# Introduce new line shifts after each 12 units
final_data = []
for line in processed_data:
    units_in_line = line.split()
    for i in range(0, len(units_in_line), 12):
        final_data.append(' '.join(units_in_line[i:i+12]))

# Write the final data back to the file
with open('Output/11-ContainersFiltered.txt', 'w') as file:
    file.write('\n'.join(final_data))

# Open the file to add the macro commands
with open('Output/11-ContainersFiltered.txt', 'r') as file:
    with open('Output/11-ContainersMacro.txt', 'w') as file_modified:
        # Read each line from the input file
        for line in file:
            # Prepend the desired string to the beginning of the line
            modified_line = '.send items Charactername "Items" "Items" ' + line.strip() + '\n'
            # Write the modified line to the output file
            file_modified.write(modified_line)

import os

# Delete the input files
os.remove('Output/10-ContainersSplit.txt')
os.remove('Output/11-ContainersFiltered.txt')
