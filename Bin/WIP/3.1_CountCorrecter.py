#Authored by mostly nick :)
def replace_in_file(filename, old_text, new_text):
  """
  Replaces all occurrences of a string in a file with another string.

  Args:
      filename: The name of the file to modify.
      old_text: The text to be replaced.
      new_text: The text to replace with.
  """
  # Read the file contents
  with open(filename, 'r') as file:
    content = file.read()

  # Replace occurrences of old text with new text
  new_content = content.replace(old_text, new_text)

  # Write the modified content back to the file
  with open(filename, 'w') as file:
    file.write(new_content)

# Specify the filename, old text, and new text
filename = "Output/AltoholicInventoryMacro.txt"
old_text = ":0"
new_text = ":1"

# Call the function to replace the text
replace_in_file(filename, old_text, new_text)

print(f"All items with no count available set to  1.")