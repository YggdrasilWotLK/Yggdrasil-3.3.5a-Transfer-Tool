#Authored by mostly nick :)
# Define the filenames
file1 = '32-QuestNoIndex.txt'
file2 = '31-QuestIndexID.txt'
output_file = '33-QuestIDs.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Process the first file
    with open(file1, 'r') as infile1:
        # Read the content of the first file
        content1 = infile1.read()
        # Write the content to the output file
        outfile.write(content1)
        # Optionally, add a separator or newline
        outfile.write('\n')  # Add a newline between file contents for clarity

    # Process the second file
    with open(file2, 'r') as infile2:
        # Read the content of the second file
        content2 = infile2.read()
        # Write the content to the output file
        outfile.write(content2)