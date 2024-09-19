#Authored by mostly nick :)
import re

def replace_playername(file_path):
  """
  Replaces occurrences of "Playername" (uppercase) and "playername" (lowercase)
  in a file with a user-provided player name (first letter capitalized).

  Args:
    file_path: Path to the file where the replacement needs to be done.

  Returns:
    None
  """
  # Prompt user for player name (on a new line)
  print("What will the name of the character be on Yggdrasil?")
  player_name = input().strip()  # Read input from a new line and remove leading/trailing whitespace

  # Capitalize only the first letter
  player_name = player_name.title()

  # Read the file content
  with open(file_path, "r") as file:
    content = file.read()

  with open("References/Argument.txt","r") as char_file:
    character_name=char_file.read()
  # Replace all variations (case-insensitive) with the provided name
  new_content = re.sub(character_name, player_name, content)

  # Write the updated content back to the file
  with open(file_path, "w") as file:
    file.write(new_content)

  #print(f"Assigned '{player_name}' as recipient of item transfers. Macro prepared in {file_path}.")


# Specify the file path for replacement
file_path = "../CombinedMacroOutput.txt"

# Call the function with the file path
replace_playername(file_path)
