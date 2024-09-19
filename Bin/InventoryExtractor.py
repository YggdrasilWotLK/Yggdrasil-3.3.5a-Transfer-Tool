import re
import os

def extract_number(line):
    # Regex pattern to match 5-digit number
    five_digit_pattern = r"(?<![.\d])\d{5}(?!\d)"
    # Regex pattern to match 4-digit number (if no 5-digit found)
    four_digit_pattern = r"(?<![.\d])\d{4}(?!\d)"
  
    # Check for lines containing ["lastUpdate"] or ["averageItemLvl"]
    if '["lastUpdate"]' in line or '["averageItemLvl"]' in line:
        return None
    
    # List of numbers to exclude
    excluded_numbers = ["6948", "70613", "59569", "54729", "10677", "73313", "76154", "49379", "72286"]

    five_digit_match = re.search(five_digit_pattern, line)
    if five_digit_match:
        extracted_number = five_digit_match.group()
        if extracted_number not in excluded_numbers and int(extracted_number) <= 90000:
            return extracted_number
        return None
    
    four_digit_match = re.search(four_digit_pattern, line)
    if four_digit_match:
        extracted_number = four_digit_match.group()
        if extracted_number not in excluded_numbers:
            return extracted_number
    
    return None


def write_formatted_output(output_file, entries, playername):
    """Writes the list of entries to the output file, separated by spaces and limited to 12 per line, with a prefix at the beginning. Skips blank entries.

    Args:
        output_file: The opened file object for writing.
        entries: A list of strings to be written.
        playername: The player name to substitute in the output prefix.
    """
    prefix = f".send items {playername} \"Items\" \"items\""
    # Limit to 12 entries per line
    for i in range(0, len(entries), 12):
        # Only include non-empty entries in the output
        filtered_entries = [entry for entry in entries[i:i+12] if entry]
        if filtered_entries:  # Check if there are any non-empty entries
            # Join entries with spaces and add newline
            output_file.write(prefix + " " + " ".join(filtered_entries) + "\n")


# Specify the filename for input and output files
input_filename = "Input/DataStore_Inventory.lua"
output_filename = "Output/InventoryOutput.txt"

# Function to read playername from Recipient.txt or prompt user for input
def get_playername():
    if os.path.exists('References/Recipient.txt'):
        with open('References/Recipient.txt', 'r') as player_file:
            playername = player_file.read().strip()
        
        if not playername:
            playername = input("Please enter the player name: ").strip()
            with open('References/Recipient.txt', 'w') as player_file:
                player_file.write(playername)
                print(f"Player name '{playername}' written to References/Recipient.txt.")
    else:
        playername = input("Please enter the player name: ").strip()
        with open('References/Recipient.txt', 'w') as player_file:
            player_file.write(playername)
            print(f"Player name '{playername}' written to References/Recipient.txt.")
    
    return playername

try:
    # Open the input file in read mode
    with open(input_filename, "r") as input_file:
        # Open the output file in write mode (overwrite existing content)
        with open(output_filename, "w") as output_file:
            entries = []  # List to store extracted numbers/messages
            for line in input_file:
                extracted_number = extract_number(line.strip())
                if extracted_number:
                    entries.append(f"{extracted_number}")
            # Get playername
            playername = get_playername()
            # Write formatted output
            write_formatted_output(output_file, entries, playername)
except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
