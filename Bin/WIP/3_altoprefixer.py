import re
import os

def extract_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = infile.readlines()

    bag_data = {}
    current_bag = None

    for line in data:
        bag_match = re.match(r'\s*\["Bag(\d+)"\]\s*=\s*{', line)
        if bag_match:
            if current_bag is not None:
                bag_data[current_bag] = [(item_id, counts.get(index, 1)) for index, item_id in enumerate(ids, start=1)]
            current_bag = bag_match.group(1)
            ids = []
            counts = {}
        
        id_match = re.findall(r'(\d+),?\s*-- \[(\d+)\]', line)
        if id_match:
            for item_id, index in id_match:
                ids.append(int(item_id))
                counts[int(index)] = int(item_id)
                
    if current_bag is not None:
        bag_data[current_bag] = [(item_id, counts.get(index, 1)) for index, item_id in enumerate(ids, start=1)]

    # Writing initial output to temp.txt
    temp_file = 'temp.txt'
    with open(temp_file, 'w') as outfile:
        for bag, items in bag_data.items():
            outfile.write(f"Bag {bag}:\n")
            for item_id, count in items:
                outfile.write(f"  Item ID: {item_id}, Count: {count}\n")
            outfile.write("\n")
    
    # Processing temp.txt
    with open(temp_file, 'r') as infile:
        temp_data = infile.readlines()

    processed_data = []
    for line in temp_data:
        item_id_match = re.search(r'Item ID: (\d+)', line)
        count_match = re.search(r'Count: (\d+)', line)
        if item_id_match and count_match:
            item_id = int(item_id_match.group(1))
            count = int(count_match.group(1))
            if item_id >= 9999:
                if count > 999:
                    count = 1
                processed_data.append(line)

    with open(temp_file, 'w') as outfile:
        outfile.writelines(processed_data)
    

def process_temp_file(filename):
    # Define what you want to do with the temp file
    pass  # Placeholder, replace with actual code

input_filename = "temp2.txt"
output_filename = os.path.join("Output", "AltoholicInventoryMacro.txt")
prefix = '.send items Playername "Items" "Items"'

# Ensure the Output directory exists
os.makedirs("Output", exist_ok=True)

# Open input file for reading and output file for writing
with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
    # Read lines from input file
    lines = input_file.readlines()
    
    # Write prefixed lines to output file
    for line in lines:
        # Replace double spaces with single space
        line = line.replace("  ", " ")
        # Prefix the line
        prefixed_line = f'{prefix} {line}'
        output_file.write(prefixed_line)

# Remove the temporary file
os.remove(input_filename)

# Call the function to process the temporary file
process_temp_file(input_filename)

output_file = 'temp.txt'