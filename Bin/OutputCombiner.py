import os

def combine_text_files(folder_path, output_file):
    """
    Combines all text files in a folder into a single output file.

    Args:
        folder_path: Path to the folder containing the text files.
        output_file: Path to the output file where the combined content will be written.
    """
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Open the output file in write mode to start with onset commands
    with open(output_file, "w") as output:
        #output.write(".gm on\n")
        output.write("/target [@target,noexists] player\n")
        output.write(".character customize\n")

    # Open the output file in append mode
    with open(output_file, "a") as output:
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Check if it's a text file and not CombinedMacroOutput.txt
            if filename.endswith(".txt") and filename != "CombinedMacroOutput.txt":
                # Open the file in read mode
                with open(os.path.join(folder_path, filename), "r") as file:
                    # Read the content and write it to the output file
                    content = file.read()
                    output.write(content + "\n\n")  # Add a double newline for separation

    #print(f"Combined text files from '{folder_path}' to '{output_file}'.")

    # Write the .additem command to the output file
   # with open(output_file, "a") as output:
       # output.write(".additem 0 -99\n")
       # output.write(".kick\n")
       # output.write('/in 10 /run if UnitIsUnit("target", "player") then Logout() end')

# Get folder path and output file name from user (optional)
# folder_path = input("Enter the folder path containing text files: ")
# output_file = input("Enter the name of the output file: ")

# Example usage with predefined paths
folder_path = "Output"
output_file = "../CombinedMacroOutput.txt"

combine_text_files(folder_path, output_file)


os.remove("temp_output.txt")
os.remove("main_spec.txt")
os.remove("sec_spec.txt")
#os.remove("out_macro_file.txt")

