#Authored by mostly nick :)
# Open the input file for reading
with open('Output/X1-PrimarySpec.txt', 'r') as input_file:
    # Open the output files for writing
    with open('Output/X1-PrimarySpec1.txt', 'w') as output_file1, \
         open('Output/X1-PrimarySpec2.txt', 'w') as output_file2, \
         open('Output/X1-PrimarySpec3.txt', 'w') as output_file3, \
         open('Output/X1-PrimarySpec4.txt', 'w') as output_file4:
        # Read each line from the input file
        for line in input_file:
            # Check if the line starts with '/in'
            if line.startswith('/s'):
                # Write to the first output file with /in 5 replaced by /in 6
                output_file1.write(line.replace('/s', '/in 0.5 /s'))
                
                # Write to the second output file with /in 5 replaced by /in 7
                output_file2.write(line.replace('/s', '/in 1 /s'))
                
                # Write to the second output file with /in 5 replaced by /in 7
                output_file3.write(line.replace('/s', '/in 1.5 /s'))
                
                # Write to the second output file with /in 5 replaced by /in 7
                output_file4.write(line.replace('/s', '/in 2.5 /s'))