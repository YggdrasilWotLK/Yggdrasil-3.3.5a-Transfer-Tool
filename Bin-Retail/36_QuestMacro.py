#Authored by mostly nick :)
import os
import glob

# Define the source file, destination file, and output folder
source_filename = '33-QuestIDs.txt'
output_folder = 'Output'
destination_filename = '36-QuestMacro.txt'

def prepend_and_write_file(source_file, output_folder, dest_file):
    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Open the source file for reading
        with open(source_file, 'r') as file:
            # Read all lines from the source file
            lines = file.readlines()

        # Prepare the path for the destination file
        destination_path = os.path.join(output_folder, dest_file)

        # Open the destination file for writing
        with open(destination_path, 'w') as file:
            for line in lines:
                # Strip any existing whitespace and prepend '#qc '
                modified_line = '/s #qc ' + line.strip() + '\n'
                file.write(modified_line)

        #print(f"File '{destination_path}' has been created and written successfully.")

    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to process the file
prepend_and_write_file(source_filename, output_folder, destination_filename)

def delete_txt_files(directory):
    # Construct the search pattern for .txt files
    pattern = os.path.join(directory, '*.txt')
    
    # Use glob to find all .txt files
    txt_files = glob.glob(pattern)
    
    # Delete each .txt file
    for file_path in txt_files:
        try:
            os.remove(file_path)
            #print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"ALERT! Quest part 36, cleanup - Error deleting {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    delete_txt_files(current_directory)