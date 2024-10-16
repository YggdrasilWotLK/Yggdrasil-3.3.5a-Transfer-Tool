import csv
import shutil

def load_spell_values(spell_file):
    spell_values = []
    with open(spell_file, "r") as spell_f:
        spell_reader = csv.reader(spell_f, delimiter=',')
        for row in spell_reader:
            for col in row:
                if col.strip().isdigit():
                    spell_values.append(int(col.strip()))
    return spell_values

def load_talent_values(talent_file):
    talent_values = set()
    with open(talent_file, "r") as talent_f:
        talent_reader = csv.reader(talent_f, delimiter=',')
        for row in talent_reader:
            for col in row:
                if col.strip().isdigit():
                    talent_values.add(int(col.strip()))
    return talent_values

def match_columns(input_file, spell_file, talent_file, output_file):
    # Load values from Spell.txt into a list
    spell_values = load_spell_values(spell_file)

    # Load values from Talent.txt into a set
    talent_values = load_talent_values(talent_file)

    # Read input file and match values
    temp_output_file = output_file + '.tmp'  # Use a temporary file for writing
    with open(input_file, 'r') as input_f, open(temp_output_file, 'w', newline='') as output_f:
        input_reader = csv.reader(input_f, delimiter=',')
        output_writer = csv.writer(output_f, delimiter=',')

        for row in input_reader:
            if row:  # Check if the row is non-empty
                spell_value_str = row[0].strip()  # Assuming the value to match is in column 1 of talenttemp3.txt (input_file)
                if spell_value_str == "--secondary" or spell_value_str == "--primary":
                    output_writer.writerow(row)
                    continue
                
                matched = False
                original_spell_value = spell_value_str
                index = 0
                while index < len(spell_values):
                    try:
                        spell_value = int(spell_value_str)
                        if spell_value in spell_values and spell_value in talent_values:
                            matched = True
                            output_writer.writerow([spell_value_str] + row[1:])
                            print(f"Success! Match found! ID: {spell_value_str}")
                            break
                        else:
                            print(f"Spell value '{spell_value_str}' not found in Spell.txt or Talent.txt. Skipping.")
                            index += 1  # Move to the next index
                            if index < len(spell_values):
                                spell_value_str = str(int(spell_value_str) + 1)
                                print(f"Trying next value: '{spell_value_str}'")
                                continue
                            else:
                                print(f"No more values to try for '{original_spell_value}'.")
                                break  # Exit the loop if no more values to try
                    except ValueError:
                        print(f"Invalid literal '{spell_value_str}' with base 10. Skipping.")
                        break

                if not matched:
                    print(f"No valid match found for '{original_spell_value}' in Spell.txt. Skipping.")

            else:
                output_writer.writerow(row)  # Write empty lines if any

    shutil.move(temp_output_file, output_file)

match_columns('talenttemp3.txt', 'References/TalentSpells.txt', 'output_talenttemp3.txt')