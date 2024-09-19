import re
import os

# Check if "tempquest.txt" exists
if os.path.exists("tempquest.txt"):
  # Open the input file (if it exists)
  with open("tempquest.txt", "r") as infile:
    # Open the output file
    with open("Output/3-QuestMacro.txt", "w") as outfile:
      # Initialize count
      count = 0
      # Iterate through each line in the input file
      for line in infile:
        # Check if the line contains ["status"] = 2
        if '["status"] = 2' in line:
          # Extract the number within the square brackets
          match = re.search(r'\[(\d+)\]', line)
          # Write the number (if found) prefixed with ".quest complete" to the output file
          if match:
            count += 1
            examplenumber = match.group(1)
            # Divide count by 1000
            count_in_thousands = count / 1000
            if count > 2000:  # Check if count is above 2000
              outfile.write(f"/in {count_in_thousands:.1f} /s #qc {examplenumber}\n")
            else:
              outfile.write(f"/s #qc {examplenumber}\n")

  # Write additional lines to the output file
  with open("Output/3-QuestMacro.txt", "a") as outfile:
    outfile.write(".unaura 61043\n")
    outfile.write(".unaura 35076\n")
    outfile.write(".modify money -999999999\n")

  # Delete the tempquest.txt file
  os.remove("tempquest.txt")