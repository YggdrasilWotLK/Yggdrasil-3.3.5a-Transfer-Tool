#Authored by mostly nick :)
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
