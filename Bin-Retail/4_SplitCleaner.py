import os
import shutil

# Define the source and destination directories
source_dir = '.'
destination_dir = 'RawData/Split/'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Loop through the files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        # Construct full file paths
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.move(source_file, destination_file)
        #print(f"Moved: {filename}")

#print("All .txt files have been moved.")

def read_number_from_file(filepath):
    """Reads a single integer from a text file."""
    with open(filepath, 'r') as file:
        number = file.read().strip()
        return int(number)  # Convert the read string to an integer

def copy_files_with_number(src_dir, dest_dir, number):
    """Copies files from src_dir to dest_dir that contain the specified number in their filenames."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # Create destination directory if it doesn't exist

    for filename in os.listdir(src_dir):
        if str(number) in filename:
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.copy(src_file, dest_file)
            #print(f'Copied: {filename}')

def main():
    # Paths to the files and directories
    selection_file = 'References/1-Selection.txt'
    source_directory = 'RawData/Split'
    destination_directory = 'Input/CharSplit'

    # Read the number from the file
    number = read_number_from_file(selection_file)
    
    # Copy files that contain the number in their filename
    copy_files_with_number(source_directory, destination_directory, number)

if __name__ == "__main__":
    main()
