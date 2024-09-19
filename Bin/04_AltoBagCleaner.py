def compare_files(prepped3_file, preppedcount2_file, output_file):
    # Read lines from both files
    with open(prepped3_file, 'r') as file1, open(preppedcount2_file, 'r') as file2:
        prepped3_lines = file1.readlines()
        preppedcount2_lines = file2.readlines()

    # Create dictionaries to store values from preppedcount2.txt
    preppedcount2_dict = {}
    for line in preppedcount2_lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            key, value = parts
            preppedcount2_dict[value] = key

    # Open the output file for writing
    with open(output_file, 'w') as output:
        for line in prepped3_lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                key, value = parts
                if value in preppedcount2_dict:
                    output.write(f"{key}:{preppedcount2_dict[value]}\n")
                else:
                    output.write(f"{key}:1\n")

# Define file names
prepped3_file = 'prepped3.txt'
preppedcount2_file = 'preppedcount2.txt'
output_file = 'PreppedItemOutput.txt'

# Call the function to compare files and write output
compare_files(prepped3_file, preppedcount2_file, output_file)