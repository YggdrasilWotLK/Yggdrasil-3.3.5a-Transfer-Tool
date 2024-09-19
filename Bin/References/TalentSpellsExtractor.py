def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main():
    # Load contents of Spell.txt and Talent.txt
    spell_lines = load_file('Spell.txt')
    talent_lines = load_file('Talent.txt')

    # Iterate through each line in Spell.txt
    matching_lines = []
    for spell_line in spell_lines:
        spell_data = spell_line.split(',')
        spell_id = spell_data[0]

        # Iterate through each line in Talent.txt
        for talent_line in talent_lines:
            talent_data = talent_line.split(',')
            talent_ids = talent_data[4:9]

            # Check if spell_id is present in any of the talent_ids
            if spell_id in talent_ids:
                matching_lines.append(spell_line)
                break  # No need to continue checking other lines in Talent.txt

    # Write matching lines to TalentSpells.txt
    write_to_file('TalentSpells.txt', matching_lines)

if __name__ == "__main__":
    main()