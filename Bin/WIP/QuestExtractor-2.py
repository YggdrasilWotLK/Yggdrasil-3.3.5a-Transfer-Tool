#Authored by mostly nick :)
import re
import os

# Open the input file
with open("tempquest.txt", "r") as infile:
    # Open the output file
    with open("Output/QuestMacro.txt", "w") as outfile:
        # Iterate through each line in the input file
        for line in infile:
            # Check if the line contains ["status"] = 2
            if '["status"] = 2' in line:
                # Extract all numbers from the line
                numbers = re.findall(r'\d{4,5}', line)
                # Write the last number (if any) prefixed with ".quest complete" to the output file
                if numbers:
                    last_number = numbers[-1]
                    outfile.write(".quest complete " + last_number + '\n')

# Delete the tempquest.txt file
os.remove("tempquest.txt")