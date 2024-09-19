#Authored by mostly nick :)
import os
import glob

def get_bits(value, start, end):
    """Extract bits from 'start' to 'end' from 'value'."""
    mask = (1 << (end - start + 1)) - 1
    return (value >> start) & mask

def right_shift(value, shift_amount):
    """Right shift the 'value' by 'shift_amount' bits."""
    return value >> shift_amount

def test_bit(value, bit_position):
    """Test if a specific bit is set in 'value'."""
    return (value & (1 << bit_position)) != 0

def get_limits(earned):
    """Placeholder function for limits. Customize if needed."""
    # Default limits: Example values for normal ranges
    bottom = 0
    top = 21000000  # Arbitrary upper limit for demonstration
    return bottom, top

def get_reputation_info(raw_value):
    # Extract faction type (bits 0-2)
    faction_type = get_bits(raw_value, 0, 2)
    
    # Check if faction type is normal
    if faction_type == 0:  # Assuming FACTION_TYPE_NORMAL == 0
        # Extract isNegative (bit 3)
        is_negative = test_bit(raw_value, 3)
        
        # Extract standing (bits 4-7)
        standing = get_bits(raw_value, 4, 7)
        
        # Extract earned value (bits 8+)
        earned = right_shift(raw_value, 8)
        
        # Adjust for negative reputation
        earned = -earned if is_negative else earned
        
        # Get limits (you can customize this part)
        bottom, top = get_limits(earned)
        
        return bottom, top, earned
    
    return None

def read_reputation_file(file_path):
    """Read the input file and parse the faction data."""
    faction_reputations = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split()
                faction_id = int(parts[0])
                raw_value = int(parts[1])
                faction_reputations[faction_id] = raw_value
    return faction_reputations

def main():
    # Path to the input file
    input_file = '40-ReputationsInput.txt'
    output_file = 'Output/41-ReputationMacro.txt'
    
    # Create the Output directory if it doesn't exist
    if not os.path.exists('Output'):
        os.makedirs('Output')
    
    # Read the faction reputation data from the file
    faction_reputations = read_reputation_file(input_file)
    
    # Write the interpreted reputation values to the output file
    with open(output_file, 'w') as file:
        for faction, raw_value in faction_reputations.items():
            result = get_reputation_info(raw_value)
            if result:
                bottom, top, reputation = result
                file.write(f".mod reputation {faction} {reputation}\n")
            else:
                file.write(f"ALERT! Reputation script section 41 - Faction ID {faction}: Invalid or unsupported faction type\n")

if __name__ == "__main__":
    main()

# Define the file path
file_path = 'Output/41-ReputationMacro.txt'

# Read the file and process it
try:
    # Open the file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines containing " 0"
    filtered_lines = [line for line in lines if " 0" not in line]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    #print(f"Lines containing ' 0' have been deleted from {file_path}")

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
def delete_txt_files(directory):
    # Construct the search pattern for .txt files
    pattern = os.path.join(directory, '*.txt')
    
    # Use glob to find all .txt files
    txt_files = glob.glob(pattern)
    
    # Delete each .txt file
    for file_path in txt_files:
        try:
            os.remove(file_path)
            #print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"ALERT! Reputation macro part 41, cleanup - Error deleting {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    delete_txt_files(current_directory)