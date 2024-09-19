#Authored by mostly nick :)
import os

def prepend_to_file(file_path, text_to_prepend):
  """Prepends text to a file if it exists."""
  if os.path.exists(file_path):
    with open(file_path, "r+") as f:
      content = f.read()
      f.seek(0, 0)  # Move the pointer to the beginning of the file
      f.write(text_to_prepend + content)

# Replace with the desired file path and text
file_path = "../MacroTalentsSecondary.txt"
text_to_prepend = ".cheat casttime on\n"

prepend_to_file(file_path, text_to_prepend)