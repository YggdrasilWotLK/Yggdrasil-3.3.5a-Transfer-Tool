#Authored by mostly nick :)
import re
import os

def extract_class_id(input_file, output_file, target_vars=["Offset","GENERIC", "UNK1", "MAGE", "WARRIOR", "WARLOCK", "PRIEST", "DRUID", "ROGUE", "HUNTER", "PALADIN", "SHAMAN", "UNK2", "POTION", "DEATHKNIGHT", "PET"]):
  """
  Reads a file, checks for specific variables as substrings in lines,
  and prints the corresponding output column value to a new file,
  stopping after the first match.

  Args:
      input_file: Path to the input file (DataStore_Characters.lua).
      output_file: Path to the output file (References/Class-ID.txt).
      target_vars: List of variables to check for.
  """
  class_id_map = {var: i for i, var in enumerate(target_vars)}  # Dictionary comprehension for class ID mapping

  # Delete existing output file before processing (optional)
  try:
    os.remove(output_file)
  except FileNotFoundError:
    pass  # Ignore if file doesn't exist

  with open(output_file, 'a') as f_out:
    found = False  # Flag to track if a match occurred
    for line in open(input_file, 'r'):
      # Skip empty lines
      if not line.strip():
        continue

      # Check if any target variable is a substring (case-insensitive)
      for var in target_vars:
        if var.lower() in line.strip().lower():
          f_out.write(str(class_id_map[var]) + '\n')
          found = True
          break  # Exit inner loop after finding a match
        
      if found:
        break  # Exit outer loop after first occurrence

# Example usage
input_file = "Input/DataStore_Characters.lua"
output_file = "References/Class-ID.txt"
extract_class_id(input_file, output_file)

#print(f"Output written to: {output_file}")

output_file.close()
