#Authored by mostly nick :)
import os

input_file_path = "Output/TalentMacro.txt"
output_primary_file_path = "Output/X1-PrimarySpec.txt"
output_secondary_file_path = "Output/X2-SecondarySpec.txt"

def split_spec(input_path, output_primary_path, output_secondary_path):
  try:
    with open(input_path, 'r') as input_file, \
         open(output_primary_path, 'w') as output_primary_file, \
         open(output_secondary_path, 'w') as output_secondary_file:
      
      is_primary = False
      is_secondary = False
      
      # Write ".gm on" to the primary output file
      output_primary_file.write(".gm on\n")
      
      for line in input_file:
        line = line.strip()
        if line.startswith('--primary'):
          is_primary = True
          is_secondary = False
        elif line.startswith('--secondary'):
          is_primary = False
          is_secondary = True
        elif is_primary:
          output_primary_file.write(line + '\n')
        elif is_secondary:
          output_secondary_file.write("/in 13 " + line + '\n')  # Adding "/in 13" prefix to each line

      # Check for "#learn" in the secondary file
      contains_learn = False
      with open(output_secondary_path, 'r') as secondary_file:
        for line in secondary_file:
          if "#learn" in line:
            contains_learn = True
            break  # Exit loop if #learn is found
            print("Talents divided into main spec and off spec.")

      # Clear secondary file contents if it doesn't contain "#learn"
      if not contains_learn:
        # Open the file in append mode ('a') to overwrite existing content
        with open(output_secondary_path, 'a') as secondary_file:
          secondary_file.truncate(0)  # Truncate the file to erase existing content
        #print(f"Cleared contents of {output_secondary_file_path} as it doesn't contain '#learn'") 
      else:
        print(f"{output_secondary_file_path} kept as it contains '#learn'")

    # Delete the input file after processing
    os.remove(input_path)
      
  except FileNotFoundError:
    print("File not found!")
  except Exception as e:
    print("An error occurred:", e)
    

try:
    os.remove('talenttemp1.txt')
#    print("'talenttemp1.txt' deleted successfully.")
except FileNotFoundError:
    print("'talenttemp1.txt' not found.")

try:
    os.remove('talenttemp2.txt')
#    print("'talenttemp2.txt' deleted successfully.")
except FileNotFoundError:
    print("'talenttemp2.txt' not found.")

try:
    os.remove('talenttemp3.txt')
#    print("'talenttemp3.txt' deleted successfully.")
except FileNotFoundError:
    print("'talenttemp3.txt' not found.")

try:
    os.remove('talenttemp4.txt')
#    print("'talenttemp4.txt' deleted successfully.")
except FileNotFoundError:
    print("'talenttemp4.txt' not found.")


split_spec(input_file_path, output_primary_file_path, output_secondary_file_path)
