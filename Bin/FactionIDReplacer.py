#Authored by mostly nick :)
import os

def compare_and_create_output(temp_file, ids_file):
  """
  Compares names in column 1 of temp.txt to IDs in table 2 (IDs.txt).
  If a match is found, creates a new line with the matching ID, a space, and the corresponding value from temp.txt.
  Prefixes each output line with ".mod reputation ".
  Deletes the temporary file (temp.txt) after processing.

  Args:
    temp_file: Path to the temporary file containing data (name-value pairs).
    ids_file: Path to the file containing IDs (format: "ID;Name").
  """

  # Create a dictionary to store ID data (name as key, ID as value)
  id_data = {}
  for line in open(ids_file, 'r'):
    parts = line.strip().split(';')
    if len(parts) == 2:
      id_data[parts[1]] = parts[0]  # Name is key, ID is value

  # Read lines from temp_file
  with open(temp_file, 'r') as f_temp:
    lines = f_temp.readlines()

  # Create output lines
  output_lines = []
  for line in lines:
    name, value = line.strip().split(':')  # Split by colon (:)
    if name in id_data:
      output_lines.append(f".mod reputation {id_data[name]} {value}\n")  # Combine ID, space, and value

  # Write output lines to a new file (e.g., output.txt)
  with open("Output/FactionOutput.txt", 'w') as f_out:
    f_out.writelines(output_lines)

  # Delete the temporary file
  os.remove(temp_file)  # Use os.remove to delete the file

# Example usage
temp_file = "temp.txt"
ids_file = "References/IDs.txt"

# Compare and create output
compare_and_create_output(temp_file, ids_file)