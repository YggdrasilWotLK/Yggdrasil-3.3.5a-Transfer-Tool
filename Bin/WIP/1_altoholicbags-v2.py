#Authored by mostly nick :)
import re
import os

def extract_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = infile.readlines()

    bag_data = {}
    current_bag = None
    ids = []
    counts = {}

    for line in data:
        bag_match = re.match(r'\s*\["Bag(\d+)"\]\s*=\s*{', line)
        if bag_match:
            if current_bag is not None:
                # Finalize the current bag's data
                bag_data[current_bag] = [(item_id, counts.get(i + 1, 1)) for i, item_id in enumerate(ids)]
            current_bag = bag_match.group(1)
            ids = []
            counts = {}

        # Extract item IDs (only 4- and 5-digit numbers)
        id_match = re.findall(r'(\d{4,5}),?\s*-- \[(\d+)\]', line)
        if id_match:
            for item_id, index in id_match:
                ids.append(int(item_id))
        
        # Extract counts
        count_match = re.findall(r'(\d+),?\s*-- \[(\d+)\]', line)
        if count_match:
            for count, index in count_match:
                counts[int(index)] = int(count)
                
    if current_bag is not None:
        # Finalize the last bag's data
        bag_data[current_bag] = [(item_id, counts.get(i + 1, 1)) for i, item_id in enumerate(ids)]

    # Writing initial output to temp.txt
    temp_file = output_file
    with open(temp_file, 'w') as outfile:
        for bag, items in bag_data.items():
            outfile.write(f"Bag {bag}:\n")
            for item_id, count in items:
                if 1001 <= item_id <= 99999:  # Only include 4- and 5-digit item IDs
                    outfile.write(f"  Item ID: {item_id}, Count: {count}\n")
            outfile.write("\n")

    # Processing temp.txt
    with open(temp_file, 'r') as infile:
        temp_data = infile.readlines()

    processed_data = []
    for line in temp_data:
        item_id_match = re.search(r'Item ID: (\d{4,5})', line)
        count_match = re.search(r'Count: (\d+)', line)
        if item_id_match and count_match:
            processed_data.append(line)

    with open(temp_file, 'w') as outfile:
        outfile.writelines(processed_data)

    # Deleting prepped.txt
    os.remove(input_file)

# Example usage
input_file = 'prepped.txt'
output_file = 'temp.txt'
extract_data(input_file, output_file)
