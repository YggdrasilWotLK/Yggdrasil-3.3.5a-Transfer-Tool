#Authored by mostly nick :)
# Open the input file for reading
with open('Output/X2-SecondarySpec.txt', 'r') as input_file:
    # Open the output files for writing
    with open('Output/X2-SecondarySpec1.txt', 'w') as output_file1, \
         open('Output/X2-SecondarySpec2.txt', 'w') as output_file2, \
         open('Output/X2-SecondarySpec3.txt', 'w') as output_file3:
        # Read each line from the input file
        for line in input_file:
            # Check if the line starts with '/in'
            if line.startswith('/in'):
                # Write to the first output file with /in 5 replaced by /in 6
                output_file1.write(line.replace('/in 13', '/in 15'))
                
                # Write to the second output file with /in 5 replaced by /in 7
                output_file2.write(line.replace('/in 13', '/in 16'))
                
                # Write to the second output file with /in 5 replaced by /in 7
                output_file3.write(line.replace('/in 13', '/in 17'))