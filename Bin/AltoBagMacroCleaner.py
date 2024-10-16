def read_file(filepath):
    """Read the content of a file and return it as a list of lines."""
    with open(filepath, 'r') as file:
        return file.readlines()

def write_file(filepath, content):
    """Write a list of lines to a file."""
    with open(filepath, 'w') as file:
        file.writelines(content)

def process_files(altobagmacro_path, items_to_remove_path):
    # Read the contents of both files
    altobagmacro_lines = read_file(altobagmacro_path)
    items_to_remove_lines = read_file(items_to_remove_path)
    
    # Remove trailing newlines and spaces from items to remove
    items_to_remove = set(line.strip() for line in items_to_remove_lines)
    
    # Process each line of AltoBagMacro
    updated_lines = []
    for line in altobagmacro_lines:
        # Split the line by spaces and filter out items that need to be removed
        parts = line.split()
        new_parts = [part for part in parts if part not in items_to_remove]
        updated_lines.append(' '.join(new_parts) + '\n')
    
    # Write the updated lines back to the AltoBagMacro file
    write_file(altobagmacro_path, updated_lines)

# Paths to the files
altobagmacro_path = 'Output/AltoBagMacro.txt'
items_to_remove_path = 'References/ItemsToRemove.txt'

# Process the files
process_files(altobagmacro_path, items_to_remove_path)

print("Processing complete. Items have been removed from AltoBagMacro.")

import re

def remove_37711_from_line(file_path):
  """Removes '37711:(any number)' from each line in the specified file.

  Args:
    file_path: The path to the file to modify.
  """

  with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    file.truncate()

    for line in lines:
      line = re.sub(r' 37711:\d+', '', line)  # Remove leading space
      file.write(line)

if __name__ == '__main__':
  file_path = 'Output/AltoBagMacro.txt'
  remove_37711_from_line(file_path)