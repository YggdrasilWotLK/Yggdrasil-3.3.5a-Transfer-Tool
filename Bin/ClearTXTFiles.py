import os

# Get current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Filter out only .txt files
txt_files = [file for file in files if file.endswith('.txt')]

# Delete each .txt file in the current directory
for txt_file in txt_files:
    file_path = os.path.join(current_directory, txt_file)
    os.remove(file_path)

# Define paths for NameOverride.txt and AccountOverride.txt in the parent directory
name_override_path = os.path.join(current_directory, '..', 'NameOverride.txt')
account_override_path = os.path.join(current_directory, '..', 'AccountOverride.txt')

# Delete NameOverride.txt if it exists
if os.path.exists(name_override_path):
    os.remove(name_override_path)

# Delete AccountOverride.txt if it exists
if os.path.exists(account_override_path):
    os.remove(account_override_path)
