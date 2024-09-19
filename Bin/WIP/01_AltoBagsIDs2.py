#Authored by mostly nick :)
def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    output_lines = []
    IDcount = 0
    start_index = None

    for i, line in enumerate(lines):
        if '["ids"] = {' in line:
            IDcount += 1
            start_index = i
            while '}' not in lines[i]:
                i += 1
            end_index = i
            bag_data = lines[start_index:end_index+1]
            output_lines.extend([f"{line.strip()},{IDcount}\n" for line in bag_data])

    with open(output_file, 'w') as f:
        f.writelines(output_lines)


if __name__ == "__main__":
    input_file = "prepped.txt"
    output_file = "prepped2.txt"

    process_file(input_file, output_file)