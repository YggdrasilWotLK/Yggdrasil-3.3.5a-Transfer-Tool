#Authored by mostly nick :)
import csv

# Define file paths
mounts_file = '50-Mounts.txt'
pets_file = '51-Pets.txt'
spell_file = 'Resources/Spell.txt'
mounts_output_file = '52-MountSpellIDs.txt'
pets_output_file = '52-PetSpellIDs.txt'

def read_lines_from_file(file_path):
    """Read lines from a given file and return as a list of strings."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def read_spell_data(file_path):
    """Read data from the spell file and return it as a list of rows, where each row is a list of columns."""
    print("Cleaning out invalid mounts and pets from later expansions...")
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def find_matching_spell_ids(lines, spell_data):
    """Find matching spell IDs based on the lines and spell data."""
    spell_ids = []
    for line in lines:
        for row in spell_data:
            if line in row[1:]:  # Skip the first column, which is the spell ID
                spell_ids.append(row[0])
                break  # No need to check further columns if we found a match
    return spell_ids

def write_ids_to_file(file_path, ids):
    """Write the list of IDs to a file, one per line."""
    with open(file_path, 'w') as file:
        file.write('\n'.join(ids))

def main():
    # Read data from files
    mounts_lines = read_lines_from_file(mounts_file)
    pets_lines = read_lines_from_file(pets_file)
    spell_data = read_spell_data(spell_file)
    
    # Find matching spell IDs for mounts and pets
    mount_spell_ids = find_matching_spell_ids(mounts_lines, spell_data)
    pet_spell_ids = find_matching_spell_ids(pets_lines, spell_data)
    
    # Write results to output files
    write_ids_to_file(mounts_output_file, mount_spell_ids)
    write_ids_to_file(pets_output_file, pet_spell_ids)

if __name__ == "__main__":
    main()
