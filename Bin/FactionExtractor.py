def extract_info(input_file, temp_file):
    """
    Extracts words between first two quotation marks and only digits from the last number per line,
    skipping lines without a number between -43000 and 43000, and removes all apostrophes.
    The output format separates the first and second entries (excluding "lastupdate") with a colon (:).

    Args:
        input_file: Path to the input file.
        temp_file: Path to the temporary file (previously output_file).
    """
    with open(input_file, 'rb') as f_in, open(temp_file, 'w') as f_temp:
        lines = f_in.readlines()
        
        for line in lines:
            line = line.decode('utf-8')  # Decode for potential hidden characters
            
            # Check if the line contains a number between -43000 and 43000
            if not "lastUpdate" in line:
                # Split the line based on quotes
                parts = line.strip().split('"')
                
                # Check if there are at least 3 parts (2 quotes and content)
                if len(parts) >= 3:
                    # Extract text between first two quotes and remove apostrophes
                    text = parts[1].replace("'", "")
                    
                    # Split the line by pipe (|) and get the last part
                    last_part = line.split("|")[-1]
                    
                    # Extract the number from the last part while preserving the negative sign if present
                    number = ''.join(c for c in last_part if c.isdigit() or c == '-')
                    
                    # Check if the extracted number is within the range -43000 to 43000
                    if number:
                        number_value = int(number)
                        if -43000 <= number_value <= 43000:
                            # Remove "lastupdate" from the second column (digits)
                            number_without_update = number.rsplit('lastupdate', 1)[0].strip()
                            
                            # Combine text and number with colon separator
                            temp_line = f"{text}:{number_without_update}\n"
                            f_temp.write(temp_line)

# Example usage
input_file = "Input/DataStore_Reputations.lua"
temp_file = "temp.txt"
extract_info(input_file, temp_file)
