#Authored by mostly nick :)
import re
import glob
import os

# Define the file patterns and output file
input_pattern = 'Input/CharSplit/DataStore_Achievements_Characters_*.txt'
output_file = 'Output/22-AchievementMacro.txt'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

def extract_numbers_from_line(line):
    # Use regular expressions to find numbers within square brackets
    return re.findall(r'\[(\d+)\]', line)

def process_file(file_path):
    with open(file_path, 'r') as file:
        in_dates_section = False
        numbers = []
        
        for line in file:
            if '["CompletionDates"] = {' in line:
                in_dates_section = True
                continue
            
            if in_dates_section:
                if '}' in line:
                    break  # Stop reading when we reach the closing brace
                
                # Extract numbers from the current line
                numbers.extend(extract_numbers_from_line(line))
    
    return numbers

def write_numbers_to_file(numbers, output_path):
    with open(output_path, 'w') as file:
        for number in numbers:
            file.write(f'.achievement add {number}\n')

def main():
    # Find the input file
    input_files = glob.glob(input_pattern)
    if not input_files:
        print(f'No files found matching pattern: {input_pattern}')
        return

    # Process each file and extract numbers
    all_numbers = []
    for input_file in input_files:
        #print(f'Processing file: {input_file}')
        numbers = process_file(input_file)
        all_numbers.extend(numbers)
    
    # Write the numbers to the output file
    if all_numbers:
        write_numbers_to_file(all_numbers, output_file)
        #print(f'Numbers written to {output_file}')
    else:
        print('No numbers found to write.')

if __name__ == '__main__':
    main()
