#Authored by mostly nick :)
import csv

def read_talent_file(filename):
    """
    Reads a talent file and returns a list of lines from the file.
    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())  # append the entire line to lines list
    return lines

def read_combined_talent_file(filename, class_id):
    """
    Reads CombinedTalentRank.txt and returns a dictionary mapping (ability_name, rank, class_id) to ability_id.
    """
    combined_talents = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 4:
                try:
                    ability_id = int(row[0].strip())
                    ability_name = row[1].strip()
                    rank = int(row[2].strip())
                    combined_class_id = int(row[3].strip())
                    if combined_class_id == class_id:
                        combined_talents[(ability_name, rank, combined_class_id)] = ability_id
                except ValueError:
                    pass  # Commented out the print statement for invalid data format
                    # print(f"Error: Invalid data format in line '{row}'")
            else:
                print(f"Warning: Unexpected line format '{row}'")
    return combined_talents

def process_and_write_output(input_filename, combined_filename, output_filename, class_id):
    """
    Processes the input file against the combined talents file based on the specified class_id
    and writes the output to the output file.
    """
    input_lines = read_talent_file(input_filename)
    combined_talents = read_combined_talent_file(combined_filename, class_id)

    with open(output_filename, 'w') as output_file:
        for line in input_lines:
            line = line.strip()
            if line and not line.startswith('--'):  # process only non-empty lines not starting with '--'
                parts = line.split(',')
                if len(parts) == 2:
                    ability = parts[0].strip()
                    try:
                        rank = int(parts[1].strip())
                        key = (ability, rank, class_id)
                        if key in combined_talents:
                            ability_id = combined_talents[key]
                            output_file.write(f"{ability_id},{rank}\n")
                            # Optionally, print for debugging:
                            # print(f"Replaced: {ability},{rank} -> {ability_id},{rank}")
                        else:
                            output_file.write(f"{ability},{rank}\n")
                            # Optionally, print for debugging:
                            # print(f"No replacement found for: {ability},{rank}")
                    except ValueError:
                        print(f"Error: Invalid rank value in line '{line}'")
                else:
                    print(f"Warning: Unexpected line format '{line}' in {input_filename}")
            else:
                output_file.write(f"{line}\n")  # write lines starting with '--' unchanged

if __name__ == "__main__":
    # File paths
    input_file = 'talenttemp1.txt'
    combined_file = 'References/CombinedTalentRank.txt'
    output_file = 'talenttemp2.txt'
    class_id_file = 'References/Class-ID.txt'

    # Read class_id from Class-ID.txt
    try:
        with open(class_id_file, 'r') as file:
            class_id = int(file.read().strip())  # Assuming the class_id is read from a file
    except FileNotFoundError:
        print(f"Error: {class_id_file} not found.")
        exit(1)
    except ValueError:
        print(f"Error: {class_id_file} does not contain a valid integer.")
        exit(1)

    # Process and generate output
    process_and_write_output(input_file, combined_file, output_file, class_id)
