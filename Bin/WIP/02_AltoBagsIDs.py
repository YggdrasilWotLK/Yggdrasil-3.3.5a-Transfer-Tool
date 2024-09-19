# Open the file in read mode
with open('prepped2.txt', 'r') as file:
    # Read the content of the file
    content = file.readlines()

# Remove the second comma in every line and delete lines containing 'Hitem'
modified_lines = []
for line in content:
    if 'Hitem' not in line:
        # Remove the second comma
        line = line.replace(',', '', 1)
        # Remove any comma at the end of the line
        line = line.rstrip(',')
        modified_lines.append(line)

# Join the lines and apply the other modifications
modified_content = ''.join(modified_lines)
modified_content = modified_content.replace(' ', '')  # Remove all spaces
modified_content = modified_content.replace('[', '')  # Remove all [
modified_content = modified_content.replace('], ', '')  # Remove '], '
modified_content = modified_content.replace('],', '')  # Remove '], '

# Open the file in write mode
with open('prepped3.txt', 'w') as file:
    # Write the modified content to the new file
    file.write(modified_content)

#print("Replacement completed successfully.")