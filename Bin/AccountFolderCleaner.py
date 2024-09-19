import os
import shutil

def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) and not filename.endswith(".lua"):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

def move_lua_files(source_dir, dest_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith(".lua"):
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            try:
                shutil.move(source_file, dest_file)
            except Exception as e:
                print(f"Failed to move {source_file} to {dest_file}: {e}")

def main():
    # 1. Go back to the RawData folder
    raw_data_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "RawData"))

    # 2. Delete all files in RawData folder except .lua files
    delete_files_in_directory(raw_data_dir)

    # 3. Check if SavedVariables folder exists
    saved_variables_dir = os.path.join(raw_data_dir, "SavedVariables")
    if os.path.exists(saved_variables_dir):
        # Move .lua files from SavedVariables folder to RawData folder
        move_lua_files(saved_variables_dir, raw_data_dir)
        
        # 4. Delete the SavedVariables folder
        try:
            shutil.rmtree(saved_variables_dir)
            #print("Deleted SavedVariables folder.")
        except Exception as e:
            print(f"Failed to delete SavedVariables folder: {e}")
    #else:
        #print("No account identified. Skipping to character identification.")

if __name__ == "__main__":
    main()