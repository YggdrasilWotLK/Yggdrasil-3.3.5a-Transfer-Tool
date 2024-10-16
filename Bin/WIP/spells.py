import os
import re

# Define input and output file paths
input_file = "Input/DataStore_Spells.lua"
output_file = "Output/Y-SpellsMacro.txt"

# Regular expression pattern
pattern = r"\b(\d{3,5})\b"

# Delete the output file if it exists (prevents appending)
try:
  os.remove(output_file)
  #print(f"Deleted existing {output_file}")
except FileNotFoundError:
  pass  # Don't raise an error if the file doesn't exist

# Open the input file in read mode
with open(input_file, "r") as file:
  data = file.read()

# Find all occurrences of the pattern
matches = re.findall(pattern, data)

# Open the output file in write mode (overwrites existing content)
with open(output_file, "w") as output:
  # Write each digit prefixed with ".learn " to the output file
  for digit in matches:
    output.write("/in 20 /s #learnspell " + digit + "\n")

#print("Extraction completed! Output written to SpellsMacro.txt in Output folder.")