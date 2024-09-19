import os
import glob

def read_file_content(file_path):
    """Read and return the content of a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_to_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def get_rest_xp_value(file_pattern):
    """Extract the restXP value from the DataStore files."""
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            for line in file:
                if '["restXP"]' in line:
                    # Extract the value
                    start_idx = line.find('=') + 1
                    end_idx = line.find(',', start_idx)
                    rest_xp_value = int(line[start_idx:end_idx].strip())
                    return rest_xp_value // 1000
    raise FileNotFoundError("No valid DataStore file found or ['restXP'] not found")

def main():
    references_path = 'References/5-MaxLevel.txt'
    output_path = 'Output/60-LevelUpMacro.txt'
    datastore_pattern = 'Input/CharSplit/DataStore_Characters_Info_*.txt'
    
    if os.path.exists(references_path) and os.path.getsize(references_path) > 0:
        # Read the value from the 5-MaxLevel.txt file
        max_level_value = read_file_content(references_path)
        content = f"\n.levelup -80 \n.levelup {max_level_value}\n"
    else:
        # Read the value from the DataStore file
        try:
            number_from_datastore = get_rest_xp_value(datastore_pattern)
            content = f".levelup -80 \n.levelup {number_from_datastore}\n"
        except FileNotFoundError as e:
            print(e)
            return
    
    # Write to the Output/5-LevelUpMacro.txt file
    write_to_file(output_path, content)
    #print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()
