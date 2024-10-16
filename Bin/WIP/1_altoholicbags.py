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
            if item_id >= 1001:
                if count > 1000:
                    count = 1
                processed_data.append(line)

    with open(temp_file, 'w') as outfile:
        outfile.writelines(processed_data)
    
    # Deleting prepped.txt
    os.remove(input_file)

input_file = 'prepped.txt'
output_file = 'temp.txt'
extract_data(input_file, output_file)