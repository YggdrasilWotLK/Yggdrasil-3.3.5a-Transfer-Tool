import os

def extract_sections(section_file):
    with open(section_file, 'r') as f:
        lines = f.readlines()

    section_dict = {}
    current_file = None
    current_section = None

    for line in lines:
        line = line.strip()
        if line.endswith('.lua'):
            current_file = line
        elif line.startswith('Section'):
            current_section = line.split("'")[1]
            section_dict[(current_file, current_section)] = []
        elif line.startswith('Line'):
            section_dict[(current_file, current_section)].append(int(line.split(' ')[1]))

    for (data_file, section), lines in section_dict.items():
        if not os.path.exists(data_file):
            print(f"File {data_file} does not exist. Skipping...")
            continue

        with open(data_file, 'r') as f:
            data = f.readlines()

        # Ensure that there's an entry for lines not just between but after the last line.
        lines.append(len(data) + 1)

        for i in range(len(lines) - 1):
            start = lines[i] - 1
            end = lines[i + 1] - 1
            with open(f'{section}_{i+1}.txt', 'w') as f:
                f.write(''.join(data[start:end]))

        # Make sure to handle the very last range correctly
        if len(lines) > 1:
            start = lines[-2] - 1
            end = len(data)
            with open(f'{section}_{len(lines) - 1}.txt', 'w') as f:
                f.write(''.join(data[start:end]))

# Replace 'References/2-Sections.txt' with the path to your section file
extract_sections('References/2-Sections.txt')
