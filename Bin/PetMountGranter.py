#Authored by Zyyn
def extract_numbers(input_file, output_file):
    seen_numbers = set()  # Set to track seen numbers
    
    # Set of numbers to skip
    skip_numbers = {
        '70613', '69002', '61773', '44841', '44842', '44843', 
        '60025', '59961', '40990', '68187', '68188', '60119', 
        '60118', '72808', '72807', '63956', '63963', '60024', 
        '61472'
    }
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.split('|')
            if len(parts) > 2:
                try:
                    second_number = parts[2].strip().split()[0]
                    # Check if the number is not in the skip list and not already seen
                    if second_number not in skip_numbers and second_number not in seen_numbers:
                        seen_numbers.add(second_number)
                        outfile.write(f".learn {second_number}\n")
                except IndexError:
                    print(f"Skipping line due to unexpected format: {line}")
                except ValueError:
                    print(f"Skipping line due to value conversion issue: {line}")

if __name__ == "__main__":
    input_file = 'Input/DataStore_Pets.lua'  # Input file name
    output_file = 'Output/PetImport.txt'  # Output file name with .txt extension
    extract_numbers(input_file, output_file)
