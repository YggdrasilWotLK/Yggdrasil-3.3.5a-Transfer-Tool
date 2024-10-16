import os
import shutil

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        # Iterate over all the files and folders in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The folder {folder_path} does not exist.')

# Paths to the folders
input_folder = 'Input'
output_folder = 'Output'

# Clear the folders
clear_folder(input_folder)
clear_folder(output_folder)

#print("Input and Output folders have been cleared!")