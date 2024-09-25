#Authored by mostly nick :)
def process_entries(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('["Bag'):
            bag_name = line.split('"]')[0] + '"]'

            # Find the end of the current ["BagX"] entry
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('["Bag'):
                j += 1

            # Extract the entire entry content
            entry_lines = lines[i:j]

            # Check for '["counts"]' in the entry content
            counts_found = any('["counts"]' in entry_line for entry_line in entry_lines)

            if not counts_found:
                # Write the entire entry to a separate file
                with open('1-BagsNoCount.txt', 'a') as no_count_file:
                    no_count_file.writelines(entry_lines)

                # Remove the lines of the current ["BagX"] entry from the original list
                lines[i:j] = []
                continue

            # Move i to the end of the current ["BagX"] entry
            i = j - 1

        i += 1

    # Write back the modified content (excluding removed entries) to the original file
    with open(filename, 'w') as file:
        file.writelines(lines)

# Usage example:
filename = "prepped.txt"
process_entries(filename)