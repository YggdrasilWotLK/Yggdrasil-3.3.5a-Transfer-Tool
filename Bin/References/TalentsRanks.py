#Authored by mostly nick :)
import csv

# Path to input files
talent_file = "Talent.txt"
spell_file = "Spell.txt"

# Read Spell IDs and Column 209 from Spell.txt into dictionaries for fast lookup
spell_ids = {}
spell_column_209 = {}
with open(spell_file, 'r', newline='', encoding='utf-8') as spell_f:
    spell_reader = csv.reader(spell_f, delimiter=',')
    for spell_row in spell_reader:
        spell_ids[spell_row[0]] = spell_row[136]  # Mapping Spell ID to column 137 value
        spell_column_209[spell_row[0]] = spell_row[208]  # Mapping Spell ID to column 209 value

# Path to combined output file
combined_output_file = "CombinedTalentRank.txt"

# Indices for spell_id_talent in Talent.txt
indices = [4, 5, 6, 7, 8]

# Process each index and write to combined output file
with open(combined_output_file, 'w', newline='', encoding='utf-8') as combined_f:
    combined_writer = csv.writer(combined_f, delimiter=',')

    # Write header row
    combined_writer.writerow(['Column 1', 'Spell.txt Column 137', 'Index', 'Spell.txt Column 209'])

    # Iterate through each index
    for index in indices:
        with open(talent_file, 'r', newline='', encoding='utf-8') as talent_f:
            talent_reader = csv.reader(talent_f, delimiter=',')

            # Iterate through Talent.txt for current index
            for row in talent_reader:
                if index < len(row):
                    spell_id_talent = row[index]
                    if spell_id_talent in spell_ids:
                        # Write to combined output file
                        combined_writer.writerow([row[0], spell_ids[spell_id_talent], str(index - 3), spell_column_209[spell_id_talent]])

print(f"Processed data written to {combined_output_file}")
