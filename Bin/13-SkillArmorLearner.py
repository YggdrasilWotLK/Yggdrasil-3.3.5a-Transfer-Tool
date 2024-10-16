def extract_armor(filename, output_file):

  armor_codes = {
      "Plate Mail": 293,
      "Mail": 413,
      "Shield": 433,
  }
  with open(filename, 'r') as f, open(output_file, 'w') as out_file:
    for line in f:
      written_armor = False
      for armor_type in armor_codes:
        if armor_type in line and not written_armor:
          code = armor_codes[armor_type]
          if code is not None:
            out_file.write(".setskill " + str(code) + " 1\n")
          written_armor = True
          break  
          
input_file = "10-skills.txt"
output_file = "Output/Armor.txt"

extract_armor(input_file, output_file)

#print(f"Extracted armor codes written to '{output_file}'.")