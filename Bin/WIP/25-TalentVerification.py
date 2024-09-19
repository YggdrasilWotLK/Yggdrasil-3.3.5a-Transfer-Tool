#Authored by mostly nick :)
import shutil
import os

def copy_file_to_output_directory():
    # Define the paths
    original_file = "talenttemp4.txt"
    output_directory = "Output"
    new_file_name = "TalentMacro.txt"
    
    # Check if the Output directory exists, create it if not
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Construct the full path for both original and destination files
    original_path = os.path.abspath(original_file)
    destination_path = os.path.join(output_directory, new_file_name)
    
    try:
        # Copy the file
        shutil.copyfile(original_path, destination_path)
        #print(f"File '{original_file}' successfully copied to '{destination_path}'")
    except FileNotFoundError:
        print(f"Error: File '{original_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{original_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the function to copy the file
copy_file_to_output_directory()
