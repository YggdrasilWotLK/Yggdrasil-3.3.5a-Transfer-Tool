#Authored by mostly nick :)
def delete_lines_with_specific_text(input_file, output_file):
    # Open input file for reading
    with open(input_file, "r") as input_f:
        lines = input_f.readlines()

    # Open output file for writing
    with open(output_file, "w") as output_f:
        # Iterate through each line
        for line in lines:
            # Check if the line contains the text "1, 1"
            if "1, 1" in line:
                continue  # Skip this line

            # Check if the line contains the word "Language"
            if "Language" in line:
                continue  # Skip this line

            # Split the line into columns
            columns = line.split()
            # Check if the second column contains '1'
            if columns[1] != "1":
                # Write the line to the output file
                output_f.write(line)

# Paths to input and output files
input_file = "10-skills.txt"
output_file = "11-skills.txt"

# Call the function to delete lines with specific text
delete_lines_with_specific_text(input_file, output_file)