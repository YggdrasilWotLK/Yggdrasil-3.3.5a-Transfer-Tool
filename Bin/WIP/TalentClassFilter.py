import csv

def copy_matching_rows(talent_spells_file, class_id_file, output_file):
  """
  Copies rows from talent_spells_file where the value in column 209 matches the contents of class_id_file.

  Args:
      talent_spells_file (str): Path to the "TalentSpells.txt" file.
      class_id_file (str): Path to the "Class-ID.txt" file.
      output_file (str): Path to the output file "TalentSpellsClass.txt".
  """

  with open(talent_spells_file, 'r', newline='') as talent_spells, \
       open(class_id_file, 'r', newline='') as class_ids, \
       open(output_file, 'w', newline='') as output_file:

    talent_reader = csv.reader(talent_spells)
    class_id = class_ids.read().strip()  # Read entire Class-ID.txt file

    writer = csv.writer(output_file)
    for row in talent_reader:
      if row[208] == class_id:  # Check column 209 (index 208)
        writer.writerow(row)

# Replace these with your actual file paths
talent_spells_file = "References/TalentSpells.txt"
class_id_file = "References/Class-ID.txt"
output_file = "References/TalentSpellsClass.txt"

copy_matching_rows(talent_spells_file, class_id_file, output_file)

#print(f"Matching rows copied to {output_file}")
