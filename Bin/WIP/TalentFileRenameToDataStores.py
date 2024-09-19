#Authored by mostly nick :)
import os

old_name = "Raw/TalentData.lua"  # Assuming Raw/ is part of the new name
new_name = "Raw/DataStore_TalentData.lua"

# Get the current working directory
cwd = os.getcwd()

# Try deleting the existing file (ignore errors if it doesn't exist)
try:
  os.remove(os.path.join(cwd, new_name))
  #print(f"Deleted existing file: {new_name}")
except FileNotFoundError:
  pass  # Ignore file not found error

# Check if the old file exists
if os.path.exists(os.path.join(cwd, old_name)):
  # Rename the file
  os.rename(os.path.join(cwd, old_name), os.path.join(cwd, new_name))
  #print(f"Successfully renamed {old_name} to {new_name}")
else:
  print(f"File {old_name} not found in {cwd}")