#Authored by mostly nick :)
import os
import re
import requests

def check_file_content(file_path):
    """Check if the file has content."""
    if os.path.exists(file_path):
        # Read the file and check if it has content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                return True
    return False

def download_html(url, output_file):
    """Download the HTML content from the URL and save it to the specified file."""
    print(f"Fetching data from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        
        # Save the HTML content to the specified file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML content saved to '{output_file}'")
    except requests.RequestException as e:
        print(f"Failed to retrieve data. Error: {e}")

def extract_reputation_data(html_file, output_file):
    """Extract the reputation data from the HTML file and save it to the output file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Define the regex pattern to extract the relevant part
        pattern = re.compile(r'Wrath of the Lich King","reputations":(.*?)}]}]}]}', re.DOTALL)
        match = pattern.search(html_content)
        
        if match:
            reputation_data = match.group(1).strip()
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(reputation_data)
            print(f"Reputation data saved to '{output_file}'")
        else:
            print("No reputation data found.")
    except FileNotFoundError as e:
        print(f"Error reading HTML file: {e}")

def format_reputation_file(input_file):
    """Format the reputation file to insert new lines before each {'id':."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace each {"id": with a new line before it
        formatted_content = re.sub(r'\{"id":', '\n{"id":', content)
        
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(formatted_content)
        print(f"Formatted reputation data saved to '{input_file}'")
    except FileNotFoundError as e:
        print(f"Error reading the file for formatting: {e}")

def remove_single_quotes(input_file):
    """Remove all single quotes from the file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove all single quotes
        content_no_quotes = content.replace("'", "")
        
        with open(input_file, 'w', encoding='utf-8') as file:
            file.write(content_no_quotes)
        print(f"Single quotes removed from '{input_file}'")
    except FileNotFoundError as e:
        print(f"Error reading the file for removing quotes: {e}")

def main():
    file_path = "Output/41-ReputationMacro.txt"
    url_template = "https://worldofwarcraft.blizzard.com/en-us/character/{region}/{realm}/{character}/reputation"
    html_file = "Output/reputation_page.html"
    reputation_file = "Output/42-ArmoryReputations.txt"
    
    # Read input values from files
    try:
        with open("References/4-Region.txt", "r") as file:
            region = file.read().strip().lower()
        
        with open("References/3-Realm.txt", "r") as file:
            realm = file.read().strip().lower().replace(" ", "-")
        
        with open("References/2-RetailChar.txt", "r") as file:
            character = file.read().strip().lower()
        
        # Construct the URL
        url = url_template.format(region=region, realm=realm, character=character)
    except FileNotFoundError as e:
        print(f"Error reading input files: {e}")
        return

    # Check if the file has content
    if check_file_content(file_path):
        print("Reputation macro OK!")
    else:
        print("Initiating reputation failover...")
        download_html(url, html_file)
        extract_reputation_data(html_file, reputation_file)
        format_reputation_file(reputation_file)
        remove_single_quotes(reputation_file)

if __name__ == "__main__":
    main()

import re

# Define the standing values
standing_values = {
    'hated': -63000,
    'hostile': -6000,
    'unfriendly': -3000,
    'neutral': 0,
    'friendly': 3000,
    'honored': 6000,
    'revered': 9000,
    'exalted': 43000
}

# Function to process the files
def process_files():
    # Read the faction IDs from the FactionID.txt file
    faction_id_map = {}
    with open('Resources/FactionID.txt', 'r') as faction_file:
        for line in faction_file:
            parts = line.strip().split(';')
            if len(parts) == 2:
                id_str, name = parts
                faction_id_map[name.strip()] = id_str.strip()

    # Check if the reputations file exists before processing
    reputations_path = 'Output/42-ArmoryReputations.txt'
    if not os.path.exists(reputations_path):
        return  # Skip processing if the file does not exist

    # Process the reputations file
    with open(reputations_path, 'r') as reputations_file, \
         open('Output/43-ArmoryReputationMacro.txt', 'w') as output_file:
        
        for line in reputations_file:
            # Extract the data from the line using regex
            match = re.match(r'.*"name":"([^"]+)".*"standing":"([^"]+)".*"value":(\d+).*', line)
            if match:
                name, standing, value = match.groups()
                value = int(value)
                
                # Get the corresponding faction ID
                faction_id = faction_id_map.get(name.strip())
                
                if faction_id:
                    # Get the numeric standing value
                    standing_numeric = standing_values.get(standing.lower())
                    
                    if standing_numeric is not None:
                        # Write to the output file in the required format
                        output_file.write(f".mod reputation {faction_id} {value + standing_numeric}\n")

if __name__ == '__main__':
    process_files()

import re

# Function to process the files
def process_exalted_reputations():
    # Read the faction IDs from the FactionID.txt file
    faction_id_map = {}
    with open('Resources/FactionID.txt', 'r') as faction_file:
        for line in faction_file:
            parts = line.strip().split(';')
            if len(parts) == 2:
                id_str, name = parts
                faction_id_map[name.strip()] = id_str.strip()

    # Check if the reputations file exists before processing
    reputations_path = 'Output/42-ArmoryReputations.txt'
    if not os.path.exists(reputations_path):
        return  # Skip processing if the file does not exist

    # Process the reputations file
    with open(reputations_path, 'r') as reputations_file, \
         open('Output/43-ArmoryReputationExalted.txt', 'w') as output_file:
        
        count_exalted = 0
        for line in reputations_file:
            # Extract the data from the line using regex
            match = re.search(r'"name":"([^"]+)".*"standing":"(Exalted|EXALTED|exalted)".*', line, re.IGNORECASE)
            if match:
                name = match.group(1).strip()
                
                # Get the corresponding faction ID
                faction_id = faction_id_map.get(name)
                
                if faction_id:
                    # Write to the output file in the required format
                    output_file.write(f".mod reputation {faction_id} 43000\n")
                    count_exalted += 1
                else:
                    print(f"Faction name '{name}' not found in FactionID.txt.")
        
        print(f"Found {count_exalted} 'EXALTED' standings. Results written to 43-ArmoryReputationExalted.txt.")

if __name__ == '__main__':
    process_exalted_reputations()

def combine_files():
    # File paths
    file_exalted = 'Output/43-ArmoryReputationExalted.txt'
    file_macro = 'Output/43-ArmoryReputationMacro.txt'
    output_file = 'Output/41-ReputationMacro.txt'
    reputations_path = 'Output/42-ArmoryReputations.txt'
    
    # Check if the reputations file exists before proceeding
    try:
        with open(reputations_path, 'r'):
            pass
    except FileNotFoundError:
        return

    # Read the content of the Exalted file
    try:
        with open(file_exalted, 'r') as f_exalted:
            exalted_lines = f_exalted.readlines()
    except FileNotFoundError:
        exalted_lines = []
    
    # Read the content of the Macro file
    try:
        with open(file_macro, 'r') as f_macro:
            macro_lines = f_macro.readlines()
    except FileNotFoundError:
        print(f"Error: {file_macro} not found.")
        macro_lines = []

    # Write combined content to the output file
    try:
        with open(output_file, 'w') as f_output:
            # Write the content from the Exalted file
            for line in exalted_lines:
                f_output.write(line)
            # Write the content from the Macro file
            for line in macro_lines:
                f_output.write(line)
        
        print(f"Combined content written to {output_file}.")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == '__main__':
    combine_files()

if os.path.isfile('Output/42-ArmoryReputations.txt'):
    os.remove('Output/42-ArmoryReputations.txt')

if os.path.isfile('Output/43-ArmoryReputationExalted.txt'):
    os.remove('Output/43-ArmoryReputationExalted.txt')

if os.path.isfile('Output/43-ArmoryReputationMacro.txt'):
    os.remove('Output/43-ArmoryReputationMacro.txt')
    
if os.path.isfile('Output/reputation_page.html'):
    os.remove('Output/reputation_page.html')