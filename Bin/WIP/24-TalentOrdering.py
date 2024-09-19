import os

def process_input(input_text):
    lines = input_text.split('\n')
    processed_lines = []

    for line in lines:
        line = line.strip()
        if line:
            if line.startswith("--secondary"):
                line = "--secondary"
            elif line.startswith("--primary"):
                line = "--primary"
            elif line[0].isdigit():
                parts = line.split(',')
                last_number = int(parts[-1].strip())
                reduced_number = last_number - 1
                line = f"/s #learn({parts[0]},{reduced_number})"
            processed_lines.append(line)

    return '\n'.join(processed_lines)


input_file_path = 'talenttemp3.txt'
output_file_path = 'talenttemp4.txt'

# Check if input file exists
if os.path.exists(input_file_path):
    with open(input_file_path, 'r') as file:
        input_text = file.read()

    output_text = process_input(input_text)

    # Write processed output to output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_text)

    ##print(f"Output written to '{output_file_path}'")

    # Optionally delete input file after processing
    # try:
    #     os.remove(input_file_path)
    #     print(f"'{input_file_path}' deleted successfully.")
    # except FileNotFoundError:
    #     print(f"'{input_file_path}' not found.")
else:
    print(f"Input file '{input_file_path}' not found.")
