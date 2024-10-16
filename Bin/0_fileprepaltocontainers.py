def process_line(line):
    # Check if the line contains the word "Size"
    if "Size" in line:
        return None  # Skip this line
    
    # Preserve the leading whitespace (tabs or spaces)
    leading_whitespace = len(line) - len(line.lstrip())
    indentation = line[:leading_whitespace]
    
    # Check if the line has a number and a bracket
    if "[" in line and "]" in line:
        # Find the position of the equals sign
        equals_pos = line.find("=")
        if (equals_pos != -1) and ("," in line or line.strip().endswith(']')):
            # Split the line into three parts
            before_equals = line[:equals_pos].strip()
            after_equals = line[equals_pos + 1:].strip()

            # Find the position of the bracket
            bracket_start_pos = before_equals.find("[")
            bracket_end_pos = before_equals.find("]") + 1

            # Extract the bracket part
            bracket_part = before_equals[bracket_start_pos:bracket_end_pos]

            # Extract the rest of the line
            rest_of_line = after_equals

            # Reconstruct the line
            new_line = f"{rest_of_line} -- {bracket_part}\n"
            return f"{indentation}{new_line}"
    return line

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            processed_line = process_line(line)
            if processed_line is not None:
                # Replace all instances of '=' with '--' but preserve indentation
                leading_whitespace = len(line) - len(line.lstrip())
                indentation = line[:leading_whitespace]
                outfile.write(f"{indentation}{processed_line}")

# File paths
input_file = 'Input/DataStore_Containers.lua'
output_file = 'prepped.txt'

# Process the file
process_file(input_file, output_file)