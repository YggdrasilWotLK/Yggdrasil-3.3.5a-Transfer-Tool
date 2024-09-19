#Authored by mostly nick :)
# Open the input file
with open('preppedcount.txt', 'r') as file:
    lines = file.readlines()

# Process the data
output_lines = []
for line in lines:
    # Strip any whitespace characters like \n at the end of each line
    line = line.strip()
    # Split the line into components
    parts = line.split(',')
    # Combine the 2nd and 3rd columns
    combined = parts[1] + parts[2]
    # Prepare the output line
    output_line = f"{parts[0]},{combined}"
    output_lines.append(output_line)

# Write the output to preppedcount2.txt
with open('preppedcount2.txt', 'w') as output_file:
    for output_line in output_lines:
        output_file.write(output_line + '\n')