#Authored by mostly nick :)
import os
import shutil
import subprocess

file_path_terminate = 'TERMINATERETAIL.txt'

# Check if the file exists and delete it
if os.path.exists(file_path_terminate):
    os.remove(file_path_terminate)
    #print(f"{file_path_terminate} has been deleted.")

def find_file(root_dir, filename):
    """Search for a file with the specified name in the given directory and its subdirectories."""
    for dirpath, _, files in os.walk(root_dir):
        if filename in files:
            return dirpath
    return None

def find_account_folder(root_dir):
    """Recursively search for an 'ACCOUNT' folder in the given directory and its subdirectories."""
    for dirpath, dirs, _ in os.walk(root_dir):
        if 'Account' in dirs:
            return os.path.join(dirpath, 'ACCOUNT')
    return None

def list_directories(root_dir):
    """List all directories in the specified root directory, excluding 'SavedVariables'."""
    return [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d != 'SavedVariables']

def copy_files(src_dir, dest_dir):
    """Copy all files from the source directory to the destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)

def main():
    root_path = '../RawData'
    search_file = 'Blizzard_GlueSavedVariables.lua'
    retail_folder = '../Bin-Retail/RawData'
    
    # Use absolute path for the batch script
    batch_script = os.path.abspath('../Bin-Retail/0_Run.bat')
    
    #print(f"Searching for '{search_file}' in {root_path}...")

    file_location = find_file(root_path, search_file)
    
    if file_location:
        print("Welcome to Yggdrasil's retail to WotLK 3.3.5a toon transfer utility!")
        print(" ")
        
        account_folder_path = find_account_folder(root_path)
        
        if account_folder_path:
            #print(f"ACCOUNT folder found at: {account_folder_path}")
            print("Please select a retail account to continue with:")
            directories = list_directories(account_folder_path)
            
            if not directories:
                print("No account folders found.")
                return
            
            for i, folder in enumerate(directories, start=1):
                print(f"{i}. {folder}")
            
            choice = 1  # Default choice
            try:
                user_input = input("Enter account number: ")
                choice = int(user_input)
                if not (1 <= choice <= len(directories)):
                    print("Choice out of range. Defaulting to 1.")
                    choice = 1
            except ValueError:
                print("Invalid input. Defaulting to 1.")
                
            selected_folder = directories[choice - 1]
            selected_folder_path = os.path.join(account_folder_path, selected_folder, 'SavedVariables')
            
            if os.path.isdir(selected_folder_path):
                copy_files(selected_folder_path, retail_folder)
                
                with open(file_path_terminate, "w") as file:
                    file.write("")

                batch_dir = os.path.dirname(batch_script)
                os.chdir(batch_dir)
                
                try:
                    print(" ")
                    subprocess.run([os.path.basename(batch_script)], shell=True, check=True)
                    #print("Batch script executed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error executing batch script: {e}")
                
            else:
                print(f"Folder {selected_folder_path} does not exist.")
        else:
            print(f"ACCOUNT folder not found in {root_path}.")

if __name__ == "__main__":
    main()