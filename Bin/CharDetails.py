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
