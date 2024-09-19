#Authored by mostly nick :)
import csv

def match_columns(input_file, reference_file, output_file):
    # Read the reference file into a dictionary
    references = {}
    with open(reference_file, 'r') as ref_file:
        ref_reader = csv.reader(ref_file, delimiter=',')
        for row in ref_reader:
            references[row[136]] = row[0]

    # Match column 1 in input file with column 137 in reference file
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        input_reader = csv.reader(input_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')
        
        for row in input_reader:
            talent_name = row[0]
            if talent_name == "--secondary" or talent_name == "--primary":
                output_writer.writerow(row)
            elif talent_name in references:
                output_row = [references[talent_name], int(row[1]) - 1]
                if output_row[0]:  # Check if the talent name is non-empty
                    output_writer.writerow(output_row)
            else:
                output_writer.writerow(row)  # Write the unmatched line from input file

# Example usage:
match_columns('talenttemp1.txt', 'References/TalentSpellsClass.txt', 'talenttemp2.txt')