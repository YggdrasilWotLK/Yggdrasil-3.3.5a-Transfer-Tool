import csv

def match_columns(input_file, reference_file, output_file):
    # Read the reference file into a dictionary
    references = {}
    with open(reference_file, 'r') as ref_file:
        ref_reader = csv.reader(ref_file, delimiter=',')
        for row in ref_reader:
            talent_name = row[136].strip()  # Assuming column 137 in reference_file
            if talent_name not in references:
                references[talent_name] = row[0].strip()  # Store the first match only

    # Match column 1 in input file with column 137 in reference file
    temp_output_file = output_file + '.tmp'  # Use a temporary file for writing
    
    with open(input_file, 'r') as input_f, open(temp_output_file, 'w', newline='') as output_f:
        input_reader = csv.reader(input_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')
        
        for row in input_reader:
            if row:  # Check if the row is non-empty
                talent_name = row[0].strip()  # Column 1 of talenttemp3.txt (input_file)
                if talent_name == "--secondary" or talent_name == "--primary":
                    output_writer.writerow(row)
                elif talent_name in references:
                    changed_value = references[talent_name]
                    output_row = [changed_value] + row[1:]
                    print(f"ALERT: Error Spell.DBC! Talent not found: '{talent_name}'. Failover used: '{changed_value}'.")
                    output_writer.writerow(output_row)
                    del references[talent_name]  # Remove the entry to ensure it's used only once
                else:
                    output_writer.writerow(row)  # Write the unmatched line from input file
            else:
                output_writer.writerow(row)  # Write empty lines if any

    # Move the temporary file to the final output file
    import shutil
    shutil.move(temp_output_file, output_file)

# Example usage:
match_columns('talenttemp3.txt', 'References/Spell.txt', 'talenttemp3.txt')
