#Authored by mostly nick :)
import os
import shutil

def ensure_folder_exists(folder_path):
    """Creates the folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def delete_folder_contents(folder_path):
    """Deletes all files and subdirectories within the given folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

# Path to the folders to be cleaned
folders_to_clean = ['Input/CharSplit', 'References']

for folder in folders_to_clean:
    ensure_folder_exists(folder)  # Create the folder if it doesn't exist
    delete_folder_contents(folder)