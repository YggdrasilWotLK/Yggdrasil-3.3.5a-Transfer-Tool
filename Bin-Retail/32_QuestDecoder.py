#Authored by mostly nick :)
import math

# Function to decode quest IDs from a bitfield
def decode_quest_ids(bitfield, base_index):
    quest_ids = []
    for bit_pos in range(64):
        if bitfield & (1 << bit_pos):
            quest_ids.append(bit_pos + 64 * base_index)
    return quest_ids

# Function to process the file
def process_file(filename):
    quest_ids = []
    
    with open(filename, 'r') as file:
        base_index = 0
        for line in file:
            # Ignore lines with brackets
            if '[' in line or ']' in line:
                continue
            
            # Convert scientific notation to a float and then to an integer
            try:
                bitfield = int(float(line.strip()))
                # Decode quest IDs for the current base index
                quest_ids.extend(decode_quest_ids(bitfield, base_index))
            except ValueError:
                print(f"ALERT! Quest section 32 - Skipping invalid line: {line.strip()}")
            
            base_index += 1
    
    return quest_ids

# Function to write all quest IDs to a file
def write_quest_ids_to_file(quest_ids, output_filename):
    with open(output_filename, 'w') as file:
        for quest_id in quest_ids:
            file.write(f"{quest_id}\n")

# Main execution
if __name__ == "__main__":
    input_filename = '30-QuestTemp.txt'
    output_filename = '32-QuestNoIndex.txt'
    quest_ids = process_file(input_filename)
    write_quest_ids_to_file(quest_ids, output_filename)
