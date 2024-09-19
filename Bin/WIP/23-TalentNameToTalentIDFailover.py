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

def read_combined_talent_file(filename):
    """
    Reads CombinedTalentRank.txt and returns a dictionary mapping (ability_name, rank) to ability_id.
    """
    combined_talents = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        #next(csv_reader, None)  # Skip header row
        for row in csv_reader:
            if len(row) == 4:
                try:
                    ability_id = int(row[0].strip())
                    ability_name = row[1].strip()
                    rank = int(row[2].strip())
                    combined_talents[(ability_name, rank)] = ability_id
                except ValueError:
                    # print(f"Error: Invalid data format in line '{row}'")
                    pass
            else:
                print(f"Warning: Unexpected line format '{row}'")
    return combined_talents

def process_and_write_output(input_filename, combined_filename, output_filename):
    """
    Processes the input file against the combined talents file and writes the output to the output file.
    """
    input_lines = read_talent_file(input_filename)
    combined_talents = read_combined_talent_file(combined_filename)

    with open(output_filename, 'w') as output_file:
        for line in input_lines:
            line = line.strip()
            if line and not line.startswith('--'):  # process only non-empty lines not starting with '--'
                parts = line.split(',')
                if len(parts) == 2:
                    ability = parts[0].strip()
                    try:
                        rank = int(parts[1].strip())
                        key = (ability, rank)
                        if key in combined_talents:
                            ability_id = combined_talents[key]
                            output_file.write(f"{ability_id},{rank}\n")
                            # print(f"Replaced: {ability},{rank} -> {ability_id},{rank}")
                        else:
                            output_file.write(f"{ability},{rank}\n")
                            # print(f"No replacement found for: {ability},{rank}")
                    except ValueError:
                        print(f"Error: Invalid rank value in line '{line}'")
                # else:
                #     print(f"Warning: Unexpected line format '{line}' in {input_filename}")
            else:
                output_file.write(f"{line}\n")  # write lines starting with '--' unchanged

if __name__ == "__main__":
    # File paths
    input_file = 'talenttemp2.txt'
    combined_file = 'References/CombinedTalentRank.txt'
    output_file = 'talenttemp3.txt'

    # Process and generate output
    process_and_write_output(input_file, combined_file, output_file)
