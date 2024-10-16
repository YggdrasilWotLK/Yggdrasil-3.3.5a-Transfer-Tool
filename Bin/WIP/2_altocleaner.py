import os
import re

def process_temp_file(temp_file):
    # Define numbers to be removed
    numbers_to_remove = {"6948", "70613", "59569", "54729", "10677", "73313", "76154", "6948", "1002", "70613", "59569", "54729", "10677", "73313", "76154", "49379", "72286"}

    # Read content from temp.txt
    with open(temp_file, 'r') as infile:
        temp_data = infile.read().replace('\n', '')

    processed_data = []
    for line in temp_data.split("  "):
        # Replace "Item ID:" with ".send items Playername "Items" "Items""
        modified_line = line.replace("Item ID:", '')
        
        # Search for Count: and extract its value
        count_match = re.search(r'Count: (\d+)', modified_line)
        if count_match:
            count = int(count_match.group(1))
            # If count is above 1000, replace it with 1
            if count > 1000:
                count = 1
            # Replace count in the line
            modified_line = re.sub(r'Count: \d+', f'Count: {count}', modified_line)

        # Check if the line contains any of the numbers to be removed
        if not any(num in modified_line for num in numbers_to_remove):
            processed_data.append(modified_line)

    # Replace ", Count: " with ":"
    processed_data = [line.replace(", Count: ", ":") for line in processed_data]
    processed_data = [line.replace("6948:1", "") for line in processed_data]
    processed_data = [line.replace("70613:1", "") for line in processed_data]
    processed_data = [line.replace("59569:1", "") for line in processed_data]
    processed_data = [line.replace("54729:1", "") for line in processed_data]
    processed_data = [line.replace("10677:1", "") for line in processed_data]
    processed_data = [line.replace("73313:1", "") for line in processed_data]
    processed_data = [line.replace("76154:1", "") for line in processed_data]
    processed_data = [line.replace("6948:1", "") for line in processed_data]
    processed_data = [line.replace("1002:1", "") for line in processed_data]
    processed_data = [line.replace("70613:1", "") for line in processed_data]
    processed_data = [line.replace("59569:1", "") for line in processed_data]
    processed_data = [line.replace("54729:1", "") for line in processed_data]
    processed_data = [line.replace("10677:1", "") for line in processed_data]
    processed_data = [line.replace("73313:1", "") for line in processed_data]
    processed_data = [line.replace("76154:1", "") for line in processed_data]
    processed_data = [line.replace("49379:1", "") for line in processed_data]
    processed_data = [line.replace("72286:1", "") for line in processed_data]
    processed_data = [line.replace("90015:1", "") for line in processed_data]
    processed_data = [line.replace("90044:1", "") for line in processed_data]
    processed_data = [line.replace("91000:1", "") for line in processed_data]
    processed_data = [line.replace("91000:2", "") for line in processed_data]
    processed_data = [line.replace("91000:3", "") for line in processed_data]
    processed_data = [line.replace("91000:4", "") for line in processed_data]
    processed_data = [line.replace("91000:5", "") for line in processed_data]
    processed_data = [line.replace("91000:6", "") for line in processed_data]
    processed_data = [line.replace("91000:7", "") for line in processed_data]
    processed_data = [line.replace("91000:8", "") for line in processed_data]
    processed_data = [line.replace("91000:9", "") for line in processed_data]
    processed_data = [line.replace("91000:10", "") for line in processed_data]
    processed_data = [line.replace("91000:11", "") for line in processed_data]
    processed_data = [line.replace("91000:12", "") for line in processed_data]
    processed_data = [line.replace("91000:13", "") for line in processed_data]
    processed_data = [line.replace("91000:14", "") for line in processed_data]
    processed_data = [line.replace("91000:15", "") for line in processed_data]
    processed_data = [line.replace("91000:16", "") for line in processed_data]
    processed_data = [line.replace("91000:17", "") for line in processed_data]
    processed_data = [line.replace("91000:18", "") for line in processed_data]
    processed_data = [line.replace("91000:19", "") for line in processed_data]
    processed_data = [line.replace("91000:20", "") for line in processed_data]
    processed_data = [line.replace("153594:1", "") for line in processed_data]

    # Insert line shifts after every 12th block of text
    processed_data_with_line_shifts = []
    for i, line in enumerate(processed_data, start=1):
        processed_data_with_line_shifts.append(line)
        if i % 12 == 0:  # Check if it's the 12th block
            processed_data_with_line_shifts.append('\n')

    # Write the modified content to output.txt
    output_file = 'temp2.txt'
    with open(output_file, 'w') as outfile:
        outfile.write(''.join(processed_data_with_line_shifts))

    # Delete temp.txt
    os.remove(temp_file)

temp_file = 'ItemOutput.txt'
process_temp_file(temp_file)