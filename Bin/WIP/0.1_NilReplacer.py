#Authored by mostly nick :)
import os
import re

def replace_nil_with_zero(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            modified_content = content.replace('nil', '0')
        
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        #print("Successfully replaced all occurrences of 'nil' with '0' in the file.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
file_path = 'prepped.txt'
replace_nil_with_zero(file_path)