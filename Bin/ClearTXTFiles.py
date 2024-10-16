import os

# Get current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Filter out only .txt files
txt_files = [file for file in files if file.endswith('.txt')]

# Delete each .txt file
for txt_file in txt_files:
    file_path = os.path.join(current_directory, txt_file)
    os.remove(file_path)