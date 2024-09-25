#Authored by mostly nick :)
# Function to read lines from a file and return them as a list
def read_lines_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

# Function to write lines to a file without an extra newline at the end
def write_lines_to_file(filepath, lines):
    with open(filepath, 'w') as file:
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                file.write(line)
            else:
                file.write(line.rstrip('\n'))

# Function to filter lines in PreppedItemOutput.txt based on ids in References/ids_item.txt
def filter_prepped_item_output(prepped_item_file, ids_item_file, output_file):
    # Read lines from PreppedItemOutput.txt
    prepped_item_lines = read_lines_from_file(prepped_item_file)
    
    # Read lines from References/ids_item.txt and create a set of IDs for quick lookup
    ids_item_lines = read_lines_from_file(ids_item_file)
    ids_set = set(line.strip() for line in ids_item_lines)
    
    # Filter lines in PreppedItemOutput.txt
    filtered_lines = []
    for line in prepped_item_lines:
        number1, number2 = line.strip().split(':')
        if number1 in ids_set:
            filtered_lines.append(line)
    
    # Write filtered lines to PreppedItemCount_Filtered.txt without an extra newline
    write_lines_to_file(output_file, filtered_lines)

# File paths
prepped_item_file = 'PreppedItemOutput.txt'
ids_item_file = 'References/ids_item.txt'
output_file = 'PreppedItemCount_Filtered.txt'

# Run the filtering process
filter_prepped_item_output(prepped_item_file, ids_item_file, output_file)