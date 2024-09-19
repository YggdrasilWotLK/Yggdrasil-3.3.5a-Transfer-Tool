#Authored by mostly nick :)
def main():
    spell_file = 'References/Spell.txt'
    class_id_file = 'References/Class-ID.txt'
    output_file = 'References/SpellsNotClass.txt'
    
    # Read Class-ID.txt to get the IDs to skip
    with open(class_id_file, 'r') as f:
        class_ids_to_skip = {line.strip() for line in f}
    
    # Open Spell.txt and SpellsNotClass.txt for processing
    with open(spell_file, 'r') as spells, open(output_file, 'w') as output:
        for line in spells:
            # Check if the row contains "Rank" and skip rows with Class-ID in column 153
            if "Rank" in line and should_write_row(line, class_ids_to_skip):
                output.write(line)

    # Replace "Rank " with ""
    replace_rank(output_file)

def should_write_row(line, class_ids_to_skip):
    # Assuming columns are separated by commas
    columns = line.split(',')
    
    if len(columns) > 153:  # Check if column 154 exists (1-based index)
        class_id = columns[153].strip()  # Column 154 in 1-based index (153 in 0-based index)
        
        if class_id in class_ids_to_skip:
            return False  # Skip the row if class_id should be skipped
    
    return True

def replace_rank(file):
    # Read the content of SpellsNotClass.txt
    with open(file, 'r') as f:
        lines = f.readlines()

    # Replace "Rank " with ""
    lines = [line.replace("Rank ", "") for line in lines]

    # Write back to SpellsNotClass.txt
    with open(file, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()
