#Authored by mostly nick :)
import os
import shutil

def copy_files_to_parent_directories(source_dir):
    # Get the absolute path of the current directory
    current_dir = os.getcwd()
    
    # Define the paths of the target directories
    target_dir1 = os.path.abspath(os.path.join(current_dir, 'Output/'))

    # Define the source directory
    source_dir = os.path.abspath(source_dir)

    # Define the filename to copy
    filename = "CombinedMacroOutput.txt"

    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Check if the source directory is indeed a directory
    if not os.path.isdir(source_dir):
        print(f"'{source_dir}' is not a directory.")
        return

    # Check if the target directories exist, if not, create them
    for target_dir in [target_dir1]:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    # Iterate over the files in the source directory
    for file in os.listdir(source_dir):
        # Check if the file is named "CombinedMacroOutput"
        if file == filename:
            # Construct the source and target file paths
            source_file = os.path.join(source_dir, file)
            target_file1 = os.path.join(target_dir1, file)

            # Copy the file to the target directories
            shutil.copyfile(source_file, target_file1)
            #print(f"File '{file}' copied to '{target_dir1}'.")

# Define the source directory
source_directory = '..'

# Call the function to copy files
copy_files_to_parent_directories(source_directory)