#Authored by mostly nick :)
import re

# Helper function to convert bitfield to quest IDs
def decode_quest_ids(bitfield, base_index):
    quest_ids = []
    for bit_pos in range(64):
        if bitfield & (1 << bit_pos):
            quest_ids.append(bit_pos + 64 * base_index)
    return quest_ids

def parse_value(value):
    try:
        # Handle scientific notation and regular integers
        return int(float(value))
    except ValueError:
        # Return None if conversion fails
        return None

def main():
    # Read the file
    with open('30-QuestTemp.txt', 'r') as file:
        lines = file.readlines()
    
    # Parse the file content into a dictionary
    quest_data = {}
    for line in lines:
        line = line.strip()
        if line:
            # Process lines with index = bitfield format only
            if '=' in line:
                # Extract index and bitfield using regex
                match = re.match(r'\[(\d+)\] = ([\d.e+]+)', line)
                if match:
                    index = int(match.group(1))
                    value = match.group(2)
                    bitfield = parse_value(value)
                    if bitfield is not None:
                        quest_data[index] = bitfield

    # Write output to file
    with open('31-QuestIndexID.txt', 'w') as outfile:
        for index, bitfield in sorted(quest_data.items()):
            quest_ids = decode_quest_ids(bitfield, index)
            #outfile.write(f"Index {index}: {quest_ids}\n")
            outfile.write(f"{quest_ids}\n")

if __name__ == "__main__":
    main()

# Define the filename
filename = '31-QuestIndexID.txt'

# Read the content from the file
with open(filename, 'r') as file:
    content = file.read()

# Remove all square brackets
content = content.replace('[', '')
content = content.replace(']', '')

# Replace all commas with line breaks
content = content.replace(',', '\n')

# Split the content into lines and strip both leading and trailing spaces
lines = content.splitlines()
lines = [line.strip() for line in lines]

# Join the lines back into a single string with newline characters
processed_content = '\n'.join(lines)

# Write the modified content back to the file
with open(filename, 'w') as file:
    file.write(processed_content)
