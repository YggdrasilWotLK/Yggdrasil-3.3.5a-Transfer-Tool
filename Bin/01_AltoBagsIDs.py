import re

def process_file(input_file, output_file):
    # Step 1: Read file and initialize IDcount
    IDcount = 0
    with open(input_file, 'r') as f:
        lines = f.readlines()

    output_lines = []

    # Step 2: Delete empty lines and replace ' --' with ','
    lines = [line.strip().replace(' --', ',') for line in lines if line.strip()]

    # Step 3-7: Loop through lines and process '["ids"] = {' entries
    while lines:
        # Find the index of the next '["ids"] = {' entry
        start_index = next((i for i, line in enumerate(lines) if '["ids"] = {' in line), None)
        if start_index is None:
            break  # If no more '["ids"] = {' entries are found, stop processing

        IDcount += 1  # Increase IDcount

        # Find the index of the first '}' after the '["ids"] = {' entry
        end_index = next((i for i, line in enumerate(lines[start_index:]) if '}' in line), None)
        if end_index is None:
            break  # If no '}' is found, stop processing

        end_index += start_index  # Adjust end_index to the global index

        # Extract lines with numbers and append IDcount to each line
        for line in lines[start_index:end_index]:
            numbers = re.findall(r'\d+', line)
            if numbers:
                output_lines.append(f"{','.join(numbers)}{IDcount * 7}\n")

        # Remove processed lines from lines list
        lines = lines[end_index+1:]

    # Write output lines to file
    with open(output_file, 'w') as f:
        f.writelines(output_lines)


if __name__ == "__main__":
    input_file = "prepped.txt"
    output_file = "prepped3.txt"

    process_file(input_file, output_file)