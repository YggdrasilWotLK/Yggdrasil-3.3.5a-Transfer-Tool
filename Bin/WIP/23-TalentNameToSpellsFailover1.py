import csv

def match_columns(input_file, reference_file, output_file):
    # Read the reference file into dictionaries for both criteria
    criteria1_references = {}
    criteria2_references = {}
    
    with open(reference_file, 'r') as ref_file:
        ref_reader = csv.reader(ref_file, delimiter=',')
        for row in ref_reader:
            if len(row) > 137:  # Ensure column 137 exists in the reference file
                criteria1_references[row[136].strip()] = row[0].strip()
            if len(row) > 209:  # Ensure column 209 exists in the reference file
                criteria2_references[row[208].strip()] = row[0].strip()

    # Match both criteria from input file and write to output
    with open(input_file, 'r') as input_f, open(output_file, 'w', newline='') as output_f:
        input_reader = csv.reader(input_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')
        
        for row in input_reader:
            if row and len(row) >= 2:  # Check if the row is non-empty and has at least two columns
                criterion1_value = row[0].strip()  # Column 1 of talenttemp2.txt
                criterion2_value = row[1].strip()  # Column 2 of talenttemp2.txt
                
                # Check both criteria
                if criterion1_value in criteria1_references and criterion2_value in criteria2_references:
                    matched_value = criteria1_references[criterion1_value]
                    output_row = [matched_value] + row[1:]  # Write matched entry from criteria 1
                    print(f"ALERT: Error Spell.DBC! Talent not found: '{criterion1_value}'. Failover used: '{matched_value}'.")
                    output_writer.writerow(output_row)
                else:
                    output_writer.writerow(row)  # Write the original line from talenttemp2.txt if no match
            else:
                output_writer.writerow(row)  # Write the original line if it doesn't have at least two columns

# Example usage:
match_columns('talenttemp2.txt', 'References/SpellsNotClass.txt', 'talenttemp3.txt')
