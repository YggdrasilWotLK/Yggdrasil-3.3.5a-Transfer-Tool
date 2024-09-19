#Authored by mostly nick :)
import requests
import re

def extract_collected_pet_names(region, realm, character):
    # Construct the URL
    url = f"https://worldofwarcraft.blizzard.com/en-us/character/{region}/{realm}/{character}/collections/pets"
    
    # Print the full URL
    print("")
    print("Gathering pets...")
    print(f"Fetching data from: {url}")
    
    # Fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
    # Get the raw HTML content
    html_content = response.text
    
    # Save the raw HTML content to a file for reference
    with open("page_content.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("HTML content saved to 'page_content.html'")
    
    # Regex pattern to find collected pet names
    pattern = re.compile(r'"collected":true,.*?"level":\d+,"name":"(.*?)"')
    
    # Find all matches
    matches = pattern.findall(html_content)
    
    if matches:
        print("Collected Pets:")
        with open("51-Pets.txt", "w", encoding="utf-8") as output_file:
            for name in matches:
                print(name)
                output_file.write(name + "\n")
        print(f"\nCollected pet names have been saved to '51-Pets.txt'")
        return matches
    else:
        print("No collected pets found.")
        return None

def read_input_from_files():
    # Read inputs from files
    try:
        with open("References/4-Region.txt", "r") as file:
            region = file.read().strip().lower()
        with open("References/3-Realm.txt", "r") as file:
            realm = file.read().strip().lower().replace(" ", "-")
        with open("References/2-RetailChar.txt", "r") as file:
            character = file.read().strip().lower()
        return region, realm, character
    except FileNotFoundError as e:
        print(f"Error reading files: {e}")
        return None, None, None

if __name__ == "__main__":
    # Read input values from files
    region, realm, character = read_input_from_files()
    
    if region and realm and character:
        # Extract and print pet names
        extract_collected_pet_names(region, realm, character)
    else:
        print("Error: Could not read one or more input files.")