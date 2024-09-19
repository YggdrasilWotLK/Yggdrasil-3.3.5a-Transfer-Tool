#Authored by mostly nick :)
import re
import glob

# Define file paths
input_file_pattern = 'Input/CharSplit/DataStore_Quests_History_*.txt'
output_file_path = '30-QuestTemp.txt'

# Regular expression to find lines with numbers
number_pattern = re.compile(r'\d+(\.\d+)?([eE][+-]?\d+)?')

def process_file(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            if number_pattern.search(line) and '"' not in line:
                # Write the line to the output file
                outfile.write(line)

def remove_commas(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Replace all commas with an empty string
    modified_content = content.replace(',', '')

    # Open the file for writing (this will overwrite the file)
    with open(file_path, 'w') as file:
        # Write the modified content back to the file
        file.write(modified_content)

if __name__ == '__main__':
    # Process all files matching the pattern
    for input_file_path in glob.glob(input_file_pattern):
        #print(f"Processing file: {input_file_path}")
        process_file(input_file_path, output_file_path)
    
    # Remove commas from the output file
    remove_commas(output_file_path)
    #print(f"Lines containing numbers and not containing quotes have been copied to {output_file_path}, and commas have been removed.")
