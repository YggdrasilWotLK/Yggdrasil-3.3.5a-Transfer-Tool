import os
import shutil

def clear_and_copy(source_folder, destination_folder):
    # Clear the contents of the destination folder
    for filename in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    # Copy files from source to destination
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        try:
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
        except Exception as e:
            print(f"Failed to copy {source_file} to {destination_file}. Reason: {e}")

if __name__ == "__main__":
    source_folder = "../RawData"
    destination_folder = "Raw"
    clear_and_copy(source_folder, destination_folder)