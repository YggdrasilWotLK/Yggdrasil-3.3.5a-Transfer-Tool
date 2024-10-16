import re

# Define the input and output file names
input_file = 'prepped.txt'
output_file = 'preppedcount.txt'

# Initialize variables
bag_count = 0
inside_counts_block = False

# Open the input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        # Check for "Bag" and increment the bag count
        if re.search(r'\["Bag', line):
            bag_count += 1

        # Check for counts block start
        if '["counts"]' in line:
            inside_counts_block = True
        elif inside_counts_block:
            if '}' in line:
                inside_counts_block = False
            else:
                counts_id_match = re.search(r'(\d+), -- \[(\d+)\]', line)
                if counts_id_match:
                    counts_id = counts_id_match.group(1)
                    bag_id = counts_id_match.group(2)
                    f_out.write(f"{counts_id},{bag_id},{bag_count * 7}\n")  # Multiply bag_count by 7
