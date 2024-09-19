#Authored by mostly nick :)
import re
import glob

def find_top_level_brackets(text, start_line_num):
    lines = text.split('\n')
    brackets = []
    depth = 0
    ignore_next = True  # To ignore the first opening bracket
    for line_num, line in enumerate(lines, start=start_line_num):
        line = line.strip()
        for col_num, char in enumerate(line, start=1):
            if char == '{':
                if depth == 1 and not ignore_next:
                    brackets.append((line_num, col_num))
                depth += 1
                ignore_next = False
            elif char == '}':
                depth -= 1
    return brackets

def process_input(input_text, filename):
    sections = re.split(r'(\w+)\s*=\s*{', input_text)[1:]
    results = {}
    line_num = 1
    for i in range(0, len(sections), 2):
        section_name = sections[i]
        section_content = '{' + sections[i+1]  # Add back the opening brace
        section_line_num = line_num
        line_num += section_content.count('\n') + 1
        results[section_name] = {
            'line_num': section_line_num,
            'brackets': find_top_level_brackets(section_content, section_line_num)
        }
    return results

# Find all files matching the pattern
file_pattern = 'RawData/DataStore_*.lua'
files = glob.glob(file_pattern)

# Open the output file for writing
with open('References/2-Sections.txt', 'w') as output_file:
    for filename in files:
        # Read input from file
        with open(filename, 'r') as file:
            input_text = file.read()

        results = process_input(input_text, filename)

        # Write the results to the output file
        output_file.write(f"{filename}\n\n")
        for name, data in results.items():
            output_file.write(f"Section '{name}' (Line {data['line_num']}):\n")
            for line_num, col_num in data['brackets']:
                output_file.write(f"    Line {line_num}\n")
        output_file.write('\n')
